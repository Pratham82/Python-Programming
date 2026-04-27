# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
uv venv && source .venv/bin/activate
uv pip install -e .
```

## Commands

```bash
# Start the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_pdf
```

## Architecture

This is an MCP (Model Context Protocol) server built with `FastMCP`. The entry point is `main.py`, which creates a `FastMCP` instance and registers tools by passing Python functions to `mcp.tool()()`.

**Tools** live in `tools/` as plain Python functions. They are imported in `main.py` and registered with the MCP server. Each tool function uses `pydantic.Field` for parameter descriptions (not traditional docstring param docs).

**Tool docstring convention** — docstrings must include: one-line summary, detailed explanation, "When to use" section, and examples with expected input/output.

**`tools/document.py`** provides `binary_document_to_markdown(binary_data, file_type)` which uses `markitdown` to convert binary document bytes (PDF, DOCX) into markdown text via `StreamInfo`.

Tests in `tests/` use pytest with fixture files in `tests/fixtures/`.
