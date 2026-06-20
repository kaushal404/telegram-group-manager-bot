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



2. Install the required dependencies:
      ```bash
      pip install -r requirements.txt
      ```

   3. Open `config.py` and replace the placeholder values with your actual API keys and MongoDB URI. (Alternatively, you can export them to your OS environment).

   4. Start the bot:
      ```bash
      python __main__.py
      ```

---

## 📂 Project Structure
A clean, modular structure designed for easy scaling:
* `__main__.py` : Main entry point and web server for cloud deployment.
* `config.py` : Configuration file for API keys.
* `database/` : MongoDB connection and database handlers.
* `plugins/` : Modular bot commands and handlers (admin, welcome, antispam).

---

## 💡 Important Notes
* Ensure your bot is granted **Administrator** rights in the Telegram groups where it is added. Without admin rights, moderation commands like `/ban` and `/mute` will fail.

---

## 🎥 Full Setup Tutorial Video
Agar aapko deploy ya setup karne mein koi bhi problem aa rahi hai, toh aap **Dev Kaushal Tech** par is bot ka complete step-by-step setup video dekh sakte hain:

👉 **[Watch Full Setup Video Here](https://youtu.be/WgZVdiFhPhc?si=GaVsi0mLrzqvBcNR)** 

---

## ❤️ Support & Updates
Agar aapko yeh bot pasand aaya aur aap aise hi awesome coding tutorials, bot developments, aur tech projects dekhna chahte hain, toh **Dev Kaushal Tech** YouTube channel ko zaroor subscribe karein!

[![Subscribe to Dev Kaushal Tech](https://img.shields.io/badge/YouTube-Subscribe_Now-red?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@devkaushaltech?si=gtNgvGMjwgHyBwXY)
