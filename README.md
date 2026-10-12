# My AI Agent

Personal AI agent for research, software development and SHINE project support.

## First version
- Phone-friendly setup using GitHub Codespaces.
- Terminal chat and optional Telegram chat.
- SQLite conversation memory stored locally.
- Configurable OpenAI-compatible model provider.
- Optional DuckDuckGo web research.
- Safety-first: no arbitrary shell execution or automatic external actions.

## Run in GitHub Codespaces
1. Open this repository, tap **Code** → **Codespaces** → **Create codespace on main**.
2. In the terminal run:
   ```bash
   pip install -r requirements.txt
   cp .env.example .env
   ```
3. Edit `.env` with an API key and model from a provider that currently offers a free tier. Never commit real secrets.
4. Start: `python main.py`

## Optional Telegram
1. Create a bot with Telegram's official @BotFather.
2. Add the bot token to `.env` as `TELEGRAM_BOT_TOKEN`.
3. Run: `python main.py --telegram`

## Configuration
See `.env.example`. Free model availability and usage limits can change by provider. Codespaces also has usage limits on free accounts.

## Planned roadmap
1. Get this starter running and verify the chosen model.
2. Add a research specialist that returns source links and summaries.
3. Add planning, coding-support, and SHINE workflow specialists.
4. Add a task queue, approvals for consequential actions, and richer long-term memory.
5. Add deployment only after the core has been tested.
