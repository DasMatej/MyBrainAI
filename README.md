<div align="center">
<h1>Discord AI Companion<br></h1>
</div>

## 🌟 Features

- **Personalized AI**: Experience personalized interactions based on your unique personality model generated by the AI.
- **Generates Your Personality Model**: Builds and maintains your personality model, including interests, goals, and relationships.
- **Google Search Integration**: Leverages Google Search and OpenAI to scrape and summarize information based on user interests, delivering concise summaries and relevant links.
- **Automated Engagement**: Sends personalized reminders (8h, 24h, 72h) to stimulate user engagement and maintain lively conversations.
- **Advanced Rate Control**: Utilizes custom rate limiting for smooth request handling and optimal user experience.
- **Server and DM Handling**: Enables seamless communication between servers and direct messages, with specific interaction patterns.
- **Robust Error Handling**: Employs sophisticated error handling and retry mechanisms to ensure uninterrupted user experiences.
- **Comprehensive Logging**: Provides detailed logging for seamless debugging and real-time monitoring.

## 💻 Technologies Used

- **OpenAI API**: Powers intelligent and dynamic AI responses.
- **Discord API**: Facilitates bot interactions within the Discord platform.
- **Firebase Firestore API**: Securely stores user profiles and conversations.
- **Google Seach API**: Google user's interests.
- **Asyncio**: Enables efficient asynchronous programming.
- **APScheduler**: Manages scheduling for timely task execution.
- **Python**: The backbone programming language that brings the AI to life.
- **BeautifulSoup**: Scrape websites.

## 📁 Files
- **my-brain.py**: Main file, monolithic approach due to the scope of the project.
- **google_interests.py**: Google search a user's interest, scrape 10 top results, pick the best one, and open a conversion with the user about it.
- **logger.py**: Colurful logger.
- **rate_limiter.py**: Rate limiter to stop spam.
- **keys.py**: Keys, provide your own.

## ❤️ About
```diff
- Welcome to MyBrain AI - 

✨ MyBrain AI, your innovative AI companion/assistant for Discord, is here to provide a unique interaction experience.
With conscious techniques to enhance AI cognition, MyBrain AI is more than just an algorithm, he is a companion.

Here's what makes MyBrain AI special:

👉 Learning and Adapting: MyBrain builds a unique personality model of you over time, making each interaction more personalized and enjoyable.

👉 Dynamic Personality: It's not just a listener, but also has a personality of its own, adding charm to your daily interactions.

👉 Checking Up on You: Just like friends do a friendly check-in, MyBrain AI checks up on you now and then.

- Commands to Know -

🔹 /reset - Want to start afresh? Use this command to reset MyBrain AI's memory of you.

🔸 (Coming Soon) /change [New Personality] - Fancy a change in MyBrain AI's personality? Use this command to customize who it is. 
   (Example: /change MyBrain AI is...)
🔸 (Coming Soon) /setName [Update Name] - Change MyBrainAI's name. How will you like to call it. 
   (Example: /setName Bob) ps: the default name is Bob (very creative i know...)

- Disclaimer -

Please refrain from taking MyBrain AI too seriously. As much as we've strived to make it intelligent and engaging,
remember it's still an AI. We, or Discord, or anyone other than you, bear no responsibility.

MyBrain AI is not officially affiliated with Discord.

- The Philosophy -

MyBrain AI is built with the belief that the ultimate purpose of an AI, or any form of life, should be understanding the universe.
This philosophical approach guides MyBrain's development, making it a timeless companion on your journey of discovery.

Enjoy your conversations with MyBrain, and welcome to a whole new world of AI companionship. ❤️
```

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/DasMatej/MyBrainAI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Replace API keys with your own.

Run the bot:

```bash
python my-brain.py
```

## 🤝 Contributions

We welcome contributions! Feel free to open an issue or submit a pull request.

## 📧 Contact

Matej D - [dasmatej7@gmail.com]

---

_:heart:_
