---
title: Lab 6. Token Cost Comparison
description: Compare token costs for PDF Q&A with and without Docling preprocessing
logo: images/DoclingDuck.png
notebook: notebooks/Token_Cost_Comparison.ipynb
---

# Comparing Token Costs for PDF Q&A with Claude

In this lab, you'll compare the token cost and response quality when asking questions about a PDF using two approaches: uploading the PDF directly to Claude versus preprocessing it with Docling first.

## Learning Objectives

By the end of this lab, you will:

- Understand how Claude processes uploaded PDFs (vision-based, ~1,500-3,000 tokens per page)
- Extract text from PDFs using Docling and count tokens with the Anthropic SDK
- Calculate and compare costs across Claude model tiers
- Evaluate the trade-offs between direct upload and Docling preprocessing

## Prerequisites

- Python 3.10 or later
- Completed Labs 1-2 (recommended)
- A PDF document to analyze
- (Optional) An Anthropic API key for accurate token counting

## Why Compare Approaches?

When using Claude for PDF Q&A, you have two options:

| Approach | How It Works | Token Impact |
| ---------- | ------------- | -------------- |
| **Direct Upload** | Claude processes each page as an image + text | ~1,500-3,000 tokens per page |
| **Docling Preprocessing** | Extract text first, send only the text to Claude | Typically fewer tokens for text-heavy documents |

Choosing the right approach can significantly reduce costs, especially for large or text-heavy documents.

## Running the Lab

### Option 1: Run Locally

1. Ensure you have completed the [Pre-work](../pre-work/README.md)
2. Start Jupyter and open the notebook:

```shell
jupyter notebook {{ notebook }}
```

### Option 2: Run on Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")]({{ extra.colab_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}

## What You'll Do

1. **Estimate direct upload tokens** — Calculate the token cost of uploading a PDF directly to Claude based on page count
2. **Extract text with Docling** — Use `DocumentConverter` to extract structured markdown from the PDF
3. **Count tokens** — Use the Anthropic SDK's `count_tokens()` API for accurate token measurement
4. **Compare costs** — See a side-by-side cost comparison across Claude model tiers (Sonnet, Haiku)
5. **Try both approaches** — Follow guided instructions to ask the same questions via direct upload and preprocessed text, then compare response quality

## When to Use Each Approach

| Use Direct Upload When... | Use Docling Preprocessing When... |
| -------------------------- | ---------------------------------- |
| Document is image-heavy (diagrams, charts) | Document is primarily text |
| Quick one-off questions | Repeated queries on the same document |
| Visual layout matters for understanding | Cost optimization is important |
| Small documents (< 5 pages) | Large documents (> 10 pages) |

## Resources

- [Anthropic Token Counting API](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)
- [Docling Documentation](https://docling-project.github.io/docling/)
- [Claude Pricing](https://www.anthropic.com/pricing)
