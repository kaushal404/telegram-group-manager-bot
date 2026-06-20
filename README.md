# 🛡️ Telegram Group Management Bot

A powerful, modular, and asynchronous Telegram Group Management Bot built using **Pyrogram (v2)** and **MongoDB**. 
It includes features like moderation, anti-spam, customizable welcome messages, and an advanced warning system.

---

## ✨ Features
* **Moderation:** `/ban`, `/mute`, `/warn`, `/kick` commands with admin permission checks.
* **Warning System:** Auto-ban/mute after a configurable warning limit.
* **Welcome & Leave:** Customizable welcome messages and anti-bot entry checks.
* **Anti-Spam:** Link protection and basic word filters.
* **Database:** MongoDB integration for fast and reliable data storage.
* **Production Ready:** Includes a dummy web server for easy deployment on free cloud platforms like Render.

---

## 📋 Prerequisites
Before you begin, you will need:
1. **Telegram API Keys:** Get `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).
2. **Bot Token:** Get it from [@BotFather](https://t.me/BotFather) on Telegram.
3. **MongoDB URI:** Get a free database cluster from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).

---

## ⚙️ Environment Variables
You need to set the following environment variables to run the bot:

| Variable | Description | Requirement |
| :--- | :--- | :--- |
| `API_ID` | Your Telegram API ID | **Required** |
| `API_HASH` | Your Telegram API Hash | **Required** |
| `BOT_TOKEN` | Bot Token from BotFather | **Required** |
| `MONGO_URI` | Your MongoDB Connection String | **Required** |
| `OWNER_ID` | Your Telegram User ID (for sudo access) | Optional/Recommended |

---

## 🚀 Deployment Guide

### Option 1: Deploy on Render (Free & Recommended)
1. Fork this repository or upload the files to your own GitHub account.
2. Go to [Render](https://render.com) and sign in.
3. Click on **New +** and select **Web Service**.
4. Connect your GitHub account and select this repository.
5. Setup the service with the following details:
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `python __main__.py`
6. Scroll down to **Environment Variables** and add all the required keys mentioned in the table above.
7. Click **Create Web Service**. 
8. *(Optional but Important)*: To keep the bot running 24/7 on Render's free tier, copy your Render web service URL (e.g., `https://your-app.onrender.com`) and set up a free 5-minute ping on [cron-job.org](https://cron-job.org).

---

### Option 2: Local Setup (For PC/VPS)
1. Clone the repository:
```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name

---

## ❤️ Support & Updates

Agar aapko ye bot pasand aaya aur aap aise hi awesome coding tutorials aur projects dekhna chahte hain, toh mere YouTube channel ko zaroor subscribe karein!

[![Subscribe to Dev Kaushal Tech](https://img.shields.io/badge/YouTube-Subscribe_Now-red?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@devkaushaltech?si=gtNgvGMjwgHyBwXY)
