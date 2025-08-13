---
title: Docling Workshop Lab 2
description: Chunking and Vectorization with Docling
logo: images/DoclingDuck.png
---

# Chunking with Docling

[Chunking](https://www.ibm.com/architectures/papers/rag-cookbook/chunking) is the process of splitting large texts into smaller, manageable segments before feeding them into a model. This is an important step because models have a maximum context length, and chunking ensures that relevant information fits within this limit while preserving coherence, improving retrieval accuracy, and avoiding loss of important content during processing.

In this lab we will explore the importance of chunking and the capabilities Docling has to create more valuable chunks.

## Prerequisites

This lab is a [Jupyter notebook](https://jupyter.org/). Please follow the instructions in [pre-work](../pre-work/README.md) to run the lab.

## Lab

[![# Enhanced Chunking and Vectorization with Docling Notebook](https://badgen.net/badge/icon/github?icon=github&label=View%20on "View on GitHub")]({{ config.repo_url }}/blob/{{ git.commit }}/notebooks/Chunking.ipynb){:target="_blank"}
[![# Enhanced Chunking and Vectorization with Docling Notebook](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")]({{ extra.colab_url }}/blob/{{ git.commit }}/notebooks/Chunking.ipynb){:target="_blank"}

To run the notebook from your command line in Jupyter using the active virtual environment from the [pre-work](../pre-work/README.md#install-jupyter), run:

```shell
jupyter notebook notebooks/Chunking.ipynb
```

The path of the notebook file above is relative to the `docling-workshop` folder from the git clone in the [pre-work](../pre-work/README.md#clone-the-docling-workshop-repository).
