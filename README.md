# Stock Simulator

This repository contains a toy backtracking system for stock strategies.

## Strategy package

The `strategy` package provides an abstract `Strategy` interface and a
`NaiveStrategy` implementation that uses the OpenAI API. API keys are loaded
via [`python-dotenv`](https://pypi.org/project/python-dotenv/).

## Usage

1. Install dependencies:
   ```bash
   pip install openai python-dotenv
   ```
2. Create a `.env` file with `OPENAI_API_KEY` defined.
3. Run the demo:
   ```bash
   python main.py
   ```

The demo shows both single-stock and market backtracking modes.
