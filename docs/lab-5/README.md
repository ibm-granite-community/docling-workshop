---
title: Lab 5. Docling as a Service
description: Learn to deploy Docling as a REST API service
logo: images/DoclingDuck.png
notebook: notebooks/Serving.ipynb
---

# Docling as a Service

In this lab, you'll learn how to deploy Docling as a scalable REST API service using **docling-serve**.

## Learning Objectives

By the end of this lab, you will:

- Deploy Docling as a REST API service
- Make HTTP requests to convert documents
- Use the chunking API for RAG applications
- Batch process multiple documents
- Deploy docling-serve with Docker

## Prerequisites

- Python 3.10 or later
- Completed Labs 1-3 (recommended)
- Basic understanding of REST APIs

## Why docling-serve?

While the Python library is great for scripts and notebooks, **docling-serve** enables:

| Feature | Benefit |
| --------- | --------- |
| REST API | Use Docling from any language |
| Scalability | Handle concurrent requests |
| Microservices | Integrate with existing infrastructure |
| Batch Processing | Process document collections efficiently |

## Running the Lab

### Option 1: Run Locally

1. Ensure you have completed the [Pre-work](../pre-work/README.md)
2. Start Jupyter and open the notebook:

```shell
jupyter notebook {{ notebook }}
```

### Option 2: Run on Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg "Open In Colab")]({{ extra.colab_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}

/// note | Local Server Required
This lab requires running docling-serve locally. Google Colab can be used for learning the API patterns, but you'll need a local environment to run the server.
///

## Quick Start

### Starting the Server

```shell
# Install docling-serve
pip install docling-serve

# Start the server
docling-serve run

# Server runs at http://localhost:5000
```

### Making a Request

```python
import httpx

response = httpx.post(
    "http://localhost:5001/v1/convert/source",
    json={
        "sources": [{"kind": "http", "url": "https://arxiv.org/pdf/2501.17887"}],
        "options": {
            "do_ocr": False,  # Set True if easyocr is installed
            "pdf_backend": "dlparse_v2",
        }
    },
    timeout=120.0
)

result = response.json()
print(result.get('md', '')[:500])
```

## Key API Endpoints

| Endpoint | Method | Description |
| ---------- | -------- | ------------- |
| `/health` | GET | Health check |
| `/v1/convert/source` | POST | Convert from URL |
| `/v1/convert/file` | POST | Convert uploaded file |
| `/docs` | GET | OpenAPI documentation |

## Docker Deployment

```bash
# Run with Docker
docker run -p 5000:5000 quay.io/docling-project/docling-serve
```

## Resources

- [docling-serve GitHub](https://github.com/docling-project/docling-serve)
- [API Documentation](http://localhost:5000/docs) (when server is running)
- [Docling Documentation](https://docling-project.github.io/docling/)
