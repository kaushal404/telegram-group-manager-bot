Render Dashboard Settings
Jab aapka GitHub update ho jaye, toh Render ki website par jakar ye settings karni hain:

Render par "New Web Service" banayein.

Apne GitHub account se connect karke apna repository select karein.

Build Command me likhein:

pip install -r requirements.txt

4. **Start Command** me likhein:
   ```bash
python __main__.py
Environment Variables (Yeh bohot zaruri hai):
Aapko wahan Environment tab me jaana hai aur apni keys add karni hain:

Key: API_ID | Value: (aapka api id)

Key: API_HASH | Value: (aapka api hash)

Key: BOT_TOKEN | Value: (aapka bot token)

Key: MONGO_URI | Value: (aapka MongoDB link)

Ek Bonus Tip: Render ka free plan 15 minute baad inactive ho jata hai. Isko 24/7 online rakhne ke liye aap apna Render ka link (e.g., [https://your-bot-name.onrender.com](https://your-bot-name.onrender.com)) cron-job.org par daal sakte hain. Wo har 10 minute me aapke link ko ping karega jisse bot kabhi off nahi hoga.
