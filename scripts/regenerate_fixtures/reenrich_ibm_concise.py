"""Re-enrich the IBM annual report with concise (one-line) section summaries.

This monkey-patches DoclingEnrichingAgent._generate_summary to produce a short
topical phrase per section instead of the default 2-3 sentences. Saves the
result as ibm_annual_report_enriched_concise.json.
"""
import os
import importlib
import time
from pathlib import Path

from docling_core.types.doc.document import DoclingDocument
from mellea import MelleaSession
from mellea.backends import model_ids
from mellea.backends.litellm import LiteLLMBackend
from mellea.stdlib.components import Message
from mellea.stdlib.context import ChatContext

import docling_agent.agent_models as _am
from docling_agent.agents import DoclingEnrichingAgent

MODEL_ID = model_ids.IBM_GRANITE_4_HYBRID_SMALL

# --- Replicate backend monkey-patch ---
def _make_backend(model_id):
    return LiteLLMBackend(model_id=f"replicate/{model_id.hf_model_name}")

def _patched_setup_local_session(*, model_id, system_prompt="You are a helpful assistant."):
    ctx = ChatContext().add(Message(role="system", content=system_prompt))
    m = MelleaSession(ctx=ctx, backend=_make_backend(model_id))
    return _am._LoggingSession(m)

_am.setup_local_session = _patched_setup_local_session
for modname in ("docling_agent.agent.rag", "docling_agent.agent.enricher", "docling_agent.agent.editor"):
    mod = importlib.import_module(modname)
    if hasattr(mod, "setup_local_session"):
        mod.setup_local_session = _patched_setup_local_session

# --- Concise summary monkey-patch ---
def _patched_generate_summary(self, *, m, text, loop_budget=2):
    def _validate(content):
        c = content.strip()
        # Accept one-liner phrases up to ~150 chars, no line breaks
        return 5 < len(c) <= 200 and "\n" not in c

    return self._generate_content(
        m=m,
        text=text,
        task_prompt=(
            "In a single short phrase of at most 15 words, describe the topic of the following section. "
            "Use plain text only — no markdown, no trailing punctuation."
        ),
        requirement_description=(
            "Return one short phrase (at most 15 words) describing the section's topic. "
            "Plain text only, no line breaks, no markdown."
        ),
        validation_fn=_validate,
        loop_budget=loop_budget,
    )

DoclingEnrichingAgent._generate_summary = _patched_generate_summary

# --- Go ---
assert os.environ.get("REPLICATE_API_TOKEN"), "Set REPLICATE_API_TOKEN first"

src = Path("/Users/mingxuanzhao/scratch/chunkless-rag-tutorial/ibm_annual_report_parsed.json")
dst = Path("/Users/mingxuanzhao/scratch/chunkless-rag-tutorial/ibm_annual_report_enriched_concise.json")

doc = DoclingDocument.load_from_json(src)

enricher = DoclingEnrichingAgent(model_id=MODEL_ID, tools=[])
t0 = time.time()
# Skip _fix_heading_levels — it spins up the editor for extra LLM calls we don't need.
result = enricher._summarize_items(document=doc, fix_heading_levels=False, loop_budget=2)
elapsed = time.time() - t0

print(f"\nEnrichment completed in {elapsed/60:.1f} min")

# Save
result.save_as_json(dst)
print(f"Saved: {dst}")

# Quick stats
summaries = []
for t in result.texts:
    meta = getattr(t, 'meta', None)
    if meta and getattr(meta, 'summary', None):
        summaries.append(meta.summary.text)
print(f"\nSections with summaries: {len(summaries)}")
if summaries:
    lens = [len(s) for s in summaries]
    import statistics
    print(f"Summary char length — min {min(lens)}, median {statistics.median(lens):.0f}, max {max(lens)}, total {sum(lens):,}")
