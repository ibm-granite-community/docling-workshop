---
title: Docling Workshop Lab 3
description: Multimodal RAG with Docling
logo: images/DoclingDuck.png
---

# Multimodal RAG with Docling

[Retrieval Augmented Generation (RAG)](https://research.ibm.com/blog/retrieval-augmented-generation-RAG) is an architectural pattern that can be used to augment the performance of language models by recalling factual information from a knowledge base, and adding that information to the model query.

In this lab we will combine the skills we learned in the two previous labs to build a Docling-enhanced RAG system.

## Prerequisites

This lab is a [Jupyter notebook](https://jupyter.org/). Please follow the instructions in [pre-work](../pre-work/README.md) to run the lab.

## Lab

[![# Multimodal RAG with Docling Notebook](https://badgen.net/badge/icon/github?icon=github&label=View%20on "View on GitHub")]({{ config.repo_url }}/blob/{{ git.commit }}/notebooks/RAG.ipynb){:target="_blank"}
[![# Multimodal RAG with Docling Notebook](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")]({{ extra.colab_url }}/blob/{{ git.commit }}/notebooks/RAG.ipynb){:target="_blank"}

To run the notebook from your command line in Jupyter using the active virtual environment from the [pre-work](../pre-work/README.md#install-jupyter), run:

```shell
jupyter notebook notebooks/RAG.ipynb
```

The path of the notebook file above is relative to the `docling-workshop` folder from the git clone in the [pre-work](../pre-work/README.md#clone-the-docling-workshop-repository).