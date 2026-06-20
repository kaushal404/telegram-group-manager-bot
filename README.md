# 🛡️ Telegram Group Management Bot by Dev Kaushal

Welcome to the ultimate, highly modular, and asynchronous Telegram Group Management Bot! Built using **Pyrogram (v2)** and **MongoDB**, this project is optimized for speed and reliability. Whether you're managing a small community or a massive group, this bot handles it all.

*Developed and maintained by **Dev Kaushal**.*

---

## ✨ Premium Features
* **Advanced Moderation:** `/ban`, `/mute`, `/warn`, `/kick` commands with strict admin permission checks.
* **Automated Warning System:** Auto-ban/mute after a configurable warning limit to keep your groups clean.
* **Smart Welcome & Leave:** Customizable welcome messages and anti-bot entry checks.
* **Anti-Spam Shield:** Link protection and basic word filters to prevent spam and raids.
* **Robust Database:** MongoDB integration for fast and reliable data storage.
* **Cloud-Ready Architecture:** Includes a dummy web server specifically configured for easy deployment on free cloud platforms like Render.

---

## 📋 Prerequisites
Before deploying **Dev Kaushal's Group Manager Bot**, make sure you have:
1. **Telegram API Keys:** Get your `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).
2. **Bot Token:** Generate a new bot and get the token from [@BotFather](https://t.me/BotFather).
3. **MongoDB URI:** Create a free database cluster on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

---

## ⚙️ Environment Variables
You need to set the following environment variables to run the bot smoothly:

| Variable | Description | Requirement |
| :--- | :--- | :--- |
| `API_ID` | Your Telegram API ID | **Required** |
| `API_HASH` | Your Telegram API Hash | **Required** |
| `BOT_TOKEN` | Bot Token from BotFather | **Required** |
| `MONGO_URI` | Your MongoDB Connection String | **Required** |
| `OWNER_ID` | Your Telegram User ID (for sudo access) | Optional/Recommended |

---

## 🚀 Deployment Guide

### Option 1: Deploy on Render (Recommended by Dev Kaushal)
This codebase is specially modified to run 24/7 on Render's free tier!
1. Fork this repository to your own GitHub account.
2. Go to [Render](https://render.com) and sign in.
3. Click on **New +** and select **Web Service**.
4. Connect your GitHub account and select this repository.
5. Set up the service with these exact commands:
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `python __main__.py`
6. Scroll down to **Environment Variables** and add all the required keys mentioned in the table above.
7. Click **Create Web Service**. 
8. *(Pro Tip from Dev Kaushal)*: To keep the bot running 24/7 on Render's free tier, copy your Render web service URL (e.g., `https://your-app.onrender.com`) and set up a free 5-minute ping on [cron-job.org](https://cron-job.org).

---

### Option 2: Local Setup (For PC/VPS)
Want to run it locally on your own machine? Follow these steps:

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
