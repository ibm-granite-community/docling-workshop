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
- Compare MCP-based integration with REST API integration (Lab 5)

## Prerequisites

- Python 3.11 or later
- [VS Code](https://code.visualstudio.com/) installed
- [Ollama](https://ollama.ai/) installed
- docling-serve from [Lab 5](../lab-5/README.md) running (`docling-serve run`)
- Completed Labs 1-5 (recommended)

## Why MCP?

In Lab 5, *you* wrote code to call the Docling REST API. With MCP, the *AI agent* discovers and calls Docling tools autonomously based on your natural language requests.

| Feature | REST API (Lab 5) | MCP (Lab 7) |
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
ollama pull granite4.2:8b
```

### 2. Configure Continue

Edit `~/.continue/config.yaml`:

```yaml
name: Main Config
version: 1.0.0
schema: v1

models:
  - name: Granite 4.2
    provider: ollama
    model: granite4.2:8b
    requestOptions:
      extraBodyProperties:
        options:
          num_ctx: 16384
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
      - --transport=stdio
    env:
      DOCLING_MCP_SERVICE_URL: http://localhost:5001
```

docling-mcp sends conversions to the Docling service at `DOCLING_MCP_SERVICE_URL`, here the docling-serve instance from Lab 5. `--transport=stdio` is required because otherwise the server starts as an HTTP server instead.

### 3. Use in Agent Mode

Open Continue in VS Code, switch to **Agent** mode, and try the following prompts one at a time:

```text
Use Docling to convert https://arxiv.org/pdf/2501.17887 and tell me the document key.
```

```text
Use Docling to save that document, and tell me the file paths it was saved to.
```

```text
Export that document as markdown with a max_size of 6000 characters, then give me a concise 3-bullet executive summary.
```

## Available MCP Tools

| Tool | Description |
| :--- | :--- |
| `convert_document_into_docling_document` | Convert a document (URL or local path) and return its document key |
| `create_new_docling_document` | Create a new empty document |
| `add_title_to_docling_document` | Add a document title |
| `add_section_heading_to_docling_document` | Add a section heading |
| `add_paragraph_to_docling_document` | Add a paragraph |
| `open_list_in_docling_document` | Open a list structure |
| `add_list_items_to_list_in_docling_document` | Add items to an open list |
| `close_list_in_docling_document` | Close the current list |
| `export_docling_document_to_markdown` | Export a cached document as Markdown |

The notebook lists the full set, including the document manipulation tools.

## Resources

- [docling-mcp GitHub](https://github.com/docling-project/docling-mcp)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Continue Documentation](https://docs.continue.dev/)
- [Ollama](https://ollama.ai/)
- [Docling Documentation](https://docling-project.github.io/docling/)
- [IBM Granite Models](https://www.ibm.com/granite)
