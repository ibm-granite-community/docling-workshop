---
title: Lab 7. Docling + MCP for AI Agents
description: Use Docling as a tool for AI agents via the Model Context Protocol
logo: images/DoclingDuck.png
notebook: notebooks/MCP_Agents.ipynb
---

# Docling + MCP for AI Agents

In this lab, you'll learn how to expose Docling's document processing capabilities to AI agents using the **Model Context Protocol (MCP)** with the official `docling-mcp` package.

## Learning Objectives

By the end of this lab, you will:

- Understand what MCP is and how it enables AI agents to use tools
- Set up the docling-mcp server with Continue and Granite via Ollama
- Use Docling tools through natural language in an AI agent
- Compare MCP-based integration with REST API integration (Lab 4)

## Prerequisites

- Python 3.10 or later
- [VS Code](https://code.visualstudio.com/) installed
- [Ollama](https://ollama.ai/) installed
- Completed Labs 1-4 (recommended)

## Why MCP?

In Lab 4, *you* wrote code to call the Docling REST API. With MCP, the *AI agent* discovers and calls Docling tools autonomously based on your natural language requests.

| Feature | REST API (Lab 4) | MCP (Lab 6) |
| :--- | :--- | :--- |
| Consumer | Your application code | AI agents/LLMs |
| Discovery | Read API docs manually | Tools auto-discovered by LLM |
| Invocation | You write HTTP requests | Agent calls tools autonomously |
| Best For | Production pipelines, batch processing | AI-assisted workflows, copilots |

## Running the Lab

/// warning | Local Environment Required
This lab requires VS Code, Ollama, and the Continue extension.
It cannot run on Google Colab.
///

1. Ensure you have completed the [Pre-work](../pre-work/README.md)
2. Start Jupyter and open the notebook:

```shell
jupyter notebook {{ notebook }}
```

## Lab

[![Docling MCP Agents Notebook](https://badgen.net/badge/icon/github?icon=github&label=View%20on "View on GitHub")]({{ config.repo_url }}/blob/{{ git.commit }}/{{ notebook }}){:target="_blank"}

To run the notebook from your command line in Jupyter using the active
virtual environment from the [pre-work](../pre-work/README.md#install-jupyter), run:

```shell
jupyter notebook {{ notebook }}
```

The path of the notebook file above is relative to the `docling-workshop`
folder from the git clone in the
[pre-work](../pre-work/README.md#clone-the-docling-workshop-repository).

## Quick Start

### 1. Pull the Granite Model

```shell
ollama pull granite3.3:8b
```

### 2. Configure Continue

Edit `~/.continue/config.yaml`:

```yaml
name: Docling Workshop
version: 0.0.1
schema: v1

models:
  - name: Granite 3.3
    provider: ollama
    model: granite3.3:8b
    apiBase: http://localhost:11434
    roles:
      - chat
      - edit
      - apply
    capabilities:
      - tool_use

mcpServers:
  - name: Docling
    command: uvx
    args:
      - --from=docling-mcp
      - docling-mcp-server
```

### 3. Use in Agent Mode

Open Continue in VS Code, switch to **Agent** mode, and try:

```text
Convert https://arxiv.org/pdf/2501.17887 and summarize the key findings
```

## Available MCP Tools

| Tool | Description |
| :--- | :--- |
| `convert_document` | Convert a document (URL or local path) to structured JSON |
| `create_new_docling_document` | Create a new empty document |
| `add_title_to_docling_document` | Add a document title |
| `add_section_heading_to_docling_document` | Add a section heading |
| `add_paragraph_to_docling_document` | Add a paragraph |
| `open_list_in_docling_document` | Open a list structure |
| `add_listitem_to_list_in_docling_document` | Add a list item |
| `close_list_in_docling_document` | Close the current list |
| `export_docling_document_to_markdown` | Export the document as Markdown |

## Resources

- [docling-mcp GitHub](https://github.com/docling-project/docling-mcp)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Continue Documentation](https://docs.continue.dev/)
- [Ollama](https://ollama.ai/)
- [Docling Documentation](https://docling-project.github.io/docling/)
- [IBM Granite Models](https://www.ibm.com/granite)
