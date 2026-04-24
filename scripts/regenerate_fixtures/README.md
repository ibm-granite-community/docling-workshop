# Regenerate fixture JSONs for Lab 4 (Chunkless RAG)

This directory contains the maintainer-only scripts that produce the
enriched `DoclingDocument` JSON fixtures used by `notebooks/Chunkless_RAG.ipynb`.
Learners never run these scripts — the notebook downloads the pre-built
artifacts from the `fixtures/v1` release.

## When to regenerate

- `docling-core` changes the `DoclingDocument` on-disk JSON schema in a way
  that breaks `DoclingDocument.load_from_json`.
- You want to re-enrich with a different model or a revised summary prompt.

Regeneration takes ~2.5 hours on Replicate for the IBM annual report.
The Docling tech report fixture is currently not regenerable from this
repo — it ships as test data in the `docling-agent` repo at
`tests/data/2408.09869v5-hierarchical-with-summaries.json`. If you need a
fresh copy, pull it from there and re-upload as the `fixtures/v1` asset.

## Scripts

- `reenrich_ibm_concise.py` — parses the IBM 2025 annual report PDF with
  Docling, then runs `DoclingEnrichingAgent` with a one-phrase summary
  prompt. Produces `ibm_annual_report_enriched_concise.json`.

## Regeneration workflow

Prerequisites: `REPLICATE_API_TOKEN` exported, `uv` installed, current
`docling-core`/`docling-agent`/`mellea` pins matching `notebooks/Chunkless_RAG.ipynb`.

```shell
uv pip install \
    "docling>=2.40" \
    "docling-core>=2.70,<3" \
    "docling-agent==0.1.0" \
    "mellea[litellm]==0.4.*"

python scripts/regenerate_fixtures/reenrich_ibm_concise.py
```

Note: the script uses hardcoded source and destination paths (see the script for details).
If you need to regenerate from a different source PDF or write to a different location,
edit the script's `src` and `dst` variables before running.

Upload the new asset, overwriting the existing `fixtures/v1` release:

```shell
gh release upload fixtures/v1 ibm_annual_report_enriched_concise.json --clobber
```

Note: overwriting an asset means every deployed copy of the notebook
immediately starts fetching the new version. If the new JSON is
incompatible with older notebook code, bump to `fixtures/v2` instead
and update the notebook URLs.

## Model used for summaries

Current: `IBM Granite 4.0 Hybrid Small` via Replicate. If you change
the model, note it in the commit message so future maintainers can
correlate answer-quality changes to model changes.
