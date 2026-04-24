---
title: Lab 4. Chunkless RAG with Docling
description: Chunkless RAG with Docling
logo: images/DoclingDuck.png
notebook: notebooks/Chunkless_RAG.ipynb
---

# Chunkless RAG with Docling

Most RAG systems chunk the source document, embed the chunks, and retrieve by vector similarity. When the source is a single long document that Docling has already parsed into a real hierarchical tree, you can skip chunking and embeddings entirely and let the model navigate the structure directly.

In this lab we will build a chunkless RAG system over a Docling-parsed document, compare it to hybrid chunking on the same document, and discuss when each approach is the right tool.

## Prerequisites

This lab is a [Jupyter notebook](https://jupyter.org/). Please follow the instructions in [pre-work](../pre-work/README.md) to run the lab.

[Lab 2. Chunking and Vectorization with Docling](../lab-2/README.md) is a soft prerequisite — the final section of this lab compares chunkless retrieval against `HybridChunker` from Lab 2 and assumes some familiarity with how hybrid chunking works.

This lab requires either [Replicate](https://replicate.com) or [Ollama](https://ollama.com) to serve the Granite models, the same way [Lab 3](../lab-3/README.md) does.

/// note | Running after Lab 2 in the same Colab session
This lab pins `docling-core>=2.70` while Lab 2 pins `docling-core==2.63.*`. If you run both notebooks in the same Colab session, restart the runtime (`Runtime -> Restart runtime`) before opening this one so the pip install takes effect cleanly.
///

## Lab

[![# Chunkless RAG with Docling Notebook](https://badgen.net/badge/icon/github?icon=github&label=View%20on "View on GitHub")]({{ config.repo_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}
[![# Chunkless RAG with Docling Notebook](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")]({{ extra.colab_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}

To run the notebook from your command line in Jupyter using the active virtual environment from the [pre-work](../pre-work/README.md#install-jupyter), run:

```shell
jupyter notebook {{ notebook }}
```

The path of the notebook file above is relative to the `docling-workshop` folder from the git clone in the [pre-work](../pre-work/README.md#clone-the-docling-workshop-repository).
