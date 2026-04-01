# ⚔️ Discord Bot

A lightweight Discord bot built with `discord.py` that handles member management,
auto-moderation, role assignment, and community engagement tools.

---

## ✨ Features

- 👋 **Welcome Messages** – Greets new members via DM when they join the server
- 🚫 **Auto-Moderation** – Automatically deletes messages containing prohibited language
- 🎭 **Role Assignment** – Grants the `CODER` role to eligible members via command
- 📊 **Poll System** – Creates embedded polls with emoji reactions
- 💬 **Custom Commands** – Simple and extensible command structure using `discord.ext.commands`

---

## 🤖 Commands

| Command | Description |
|---------|-------------|
| `!hello` | Bot greets the user |
| `!coder` | Assigns the `CODER` role to the user |
| `!poll <question>` | Creates a poll embed with 😀 / 😡 reactions |

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies
```bash
pip install discord.py python-dotenv
```

### 3. Configure environment variables
Create a `.env` file in the root directory:
```env
DISCORD_TOKEN=your_discord_bot_token_here
```

### 4. Run the bot
```bash
python bot.py
```

---

## 📋 Requirements

- Python 3.8+
- `discord.py`
- `python-dotenv`

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `DISCORD_TOKEN` | Your Discord bot token from the [Developer Portal](https://discord.com/developers/applications) |

---

## 📁 Project Structure

```
├── bot.py            # Main bot file
├── .env              # Environment variables (never commit this!)
├── .gitignore        # Git ignore file
├── discord.log       # Log output (auto-generated)
└── README.md         # Project documentation
```

---

## 🛡️ Intents Required

Make sure the following **Privileged Gateway Intents** are enabled in your Discord Developer Portal:

- ✅ `MESSAGE CONTENT INTENT`
- ✅ `SERVER MEMBERS INTENT`

---

## 🚀 Deployment Notes

- Keep your `.env` file **out of version control** — add it to `.gitignore`
- Logs are saved to `discord.log` with `DEBUG` level for troubleshooting

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
