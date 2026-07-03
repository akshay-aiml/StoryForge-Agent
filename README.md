# StoryCraft Agent

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/downloads/release/python-3120/)
[![Streamlit](https://img.shields.io/badge/Streamlit-✅-orange)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-API-purple)](https://www.groq.ai/)
[![uv](https://img.shields.io/badge/uv-package_manager-brightgreen)](https://uv.run/)

## Overview

StoryCraft Agent is a Python-powered knowledge assistant that combines real-time search with modern generative AI. It provides both:

- a Streamlit web app for interactive exploration,
- an MCP server endpoint for programmatic access.

The app accepts a topic or question, fetches current information through the Tavily Search API, summarizes the results with Groq, and optionally creates a short-form video script in a YouTube Shorts / Instagram Reels style.

## Features

- Real-time information retrieval via **Tavily Search API**
- Summarization using **Groq** with `llama-3.3-70b-versatile`
- Optional short video script generation
- Streamlit front-end for interactive querying
- MCP server for integration and tooling
- Clean separation of core logic, UI, and MCP interface

## Project Structure

```text
StoryCraft Agent/
├── .env
├── pyproject.toml
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── researcher.py
│   │   └── scriptwriter.py
│   ├── app/
│   │   └── streamlit_app.py
│   └── mcp/
│       └── server.py
```

## Installation

1. Clone the repository or open it in your workspace.
2. Install dependencies using `uv`:

```bash
uv sync
```

3. Create a `.env` file at the project root with API credentials.

## Environment Variables

Create a `.env` file in the repository root with the following values:

```bash
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

> Keep your keys private and do not commit `.env` to source control.

## Run the Streamlit App

Start the interactive web app with:

```bash
PYTHONPATH=. uv run streamlit run src/app/streamlit_app.py
```

Then open the local Streamlit URL in your browser.

## Run the MCP Server

Launch the MCP development server with:

```bash
PYTHONPATH=. uv run mcp dev src/mcp/server.py
```

This exposes the same functionality as the Streamlit app through MCP tooling.

## MCP Tools

The MCP server includes these tools:

- `fetch_news_mcp(query)` — fetches and summarizes real-time information.
- `generate_video_script_mcp(query)` — fetches information and generates a short-format video script.

## Using MCP Inspector

To inspect MCP tools and calls, use the MCP inspector available with FastMCP or your preferred MCP client. The inspector helps you:

- browse available tools,
- view tool signatures,
- test queries interactively.

## Architecture

Story Craft Agent is organized for clarity and reuse:

- `src/core/` contains the application logic:
  - `config.py` loads API keys and environment configuration,
  - `researcher.py` handles real-time search and summarization,
  - `scriptwriter.py` generates short video scripts.
- `src/app/streamlit_app.py` provides the user-facing interface.
- `src/mcp/server.py` exposes the same workflows as MCP tools.

This separation ensures that UI and integration layers remain thin, while the core logic stays reusable and testable.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
