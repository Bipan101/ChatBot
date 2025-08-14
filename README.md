# 🤖 AI ChatBot with Memory System

An intelligent WhatsApp/Telegram chatbot that automatically responds to messages using Google's Gemini AI, featuring a sophisticated memory system for contextual conversations.

## ✨ Features

- **🧠 Memory System**: Remembers previous conversations and maintains context
- **🎯 Smart Detection**: Only responds when specific sender sends a message
- **🤖 AI-Powered**: Uses Google Gemini 2.0 Flash for natural responses
- **⚡ Automated**: Automatically selects, copies, and responds to chat messages
- **🎨 Personalized**: Customizable personality and communication style
- **📱 Multi-Platform**: Works with WhatsApp Web, Telegram Web, and other chat platforms

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- Google Gemini API key
- Windows OS (for pyautogui coordinates)

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ChatBot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create environment file**
   ```bash
   copy .env.example .env
   ```

4. **Configure your API key**
   - Edit `.env` file
   - Add your Gemini API key:
     ```
     Gemini_APiKey=your_api_key_here
     ```

5. **Customize the bot**
   - Edit `bot.py` line 57: Replace `"Person's_Name"` with the sender's name
   - Edit lines 140-141: Replace `"YourName"` with your bot's name
   - Adjust coordinates if needed (see Configuration section)

## ⚙️ Configuration

### 1. Screen Coordinates

The bot uses screen coordinates to interact with your chat application. You may need to adjust these based on your screen resolution and chat app layout:

```python
# Chrome/Browser icon (line 74)
pyautogui.click(1043, 1054)

# Chat selection area (lines 81-86)
pyautogui.moveTo(711, 221)  # Top-left of chat area
pyautogui.dragTo(1798, 917, duration=2.0, button='left')  # Bottom-right

# Message input field (line 175)
pyautogui.click(1475, 975)
```

### 2. Find Correct Coordinates

Use coordinate helper by making another python file and copy paste following for it:

```bash
import pyautogui

while True:
    a = pyautogui.position()
    print(a)
```

Follow the prompts to find the correct coordinates for your screen setup.

### 3. Sender Name Configuration

Update the sender name in the `is_last_message_from_sender` function:

```python
def is_last_message_from_sender(chat_log, sender_name="Your_Friend's_Name"):
```

## 🚀 Usage

### Starting the Bot

```bash
python bot.py
```

The bot will:
1. Open your browser/chat application
2. Monitor for new messages from the specified sender
3. Generate contextual responses using AI and memory
4. Automatically send replies

### Memory Management

View conversation history:
```bash
python memory_manager.py
```

Options:
- **1**: View current memory and conversation history
- **2**: Clear all memory (reset the bot)

### Stopping the Bot

Press `Ctrl+C` in the terminal to stop the bot.

## 📁 Project Structure

```
ChatBot/
├── bot.py                 # Main bot script
├── memory.json           # Conversation memory storage
├── memory_manager.py     # Memory management utility
├── .env                 # Environment variables (create from .env.example)
├── .env.example         # Environment template
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🧠 Memory System

The bot maintains intelligent memory through:

- **Conversation History**: Last 10 message-response pairs
- **Context Awareness**: Relationship type, communication style
- **Personality Traits**: Consistent character across conversations
- **Timestamps**: When conversations occurred

### Memory Structure

```json
{
  "conversation_memory": [
    {
      "timestamp": "2025-08-14T14:30:00",
      "message": "Hey, how are you?",
      "response": "I'm good! How about you?"
    }
  ],
  "bot_start_timestamp": "2025-08-14T14:00:00",
  "last_response_time": "2025-08-14T14:30:00",
  "conversation_context": {
    "relationship": "close friends/romantic interest",
    "communication_style": "casual, affectionate, uses Nepali phrases",
    "personality_traits": ["caring", "student", "coder", "from Nepal"]
  }
}
```

## 🎛️ Customization

### Personality & Style

Edit the conversation context in `memory.json` or the default values in `bot.py`:

```python
"conversation_context": {
    "relationship": "your_relationship_type",
    "communication_style": "your_style",
    "personality_traits": ["trait1", "trait2", "trait3"]
}
```

### AI Model

Change the AI model in `bot.py`:

```python
model = genai.GenerativeModel('gemini-2.0-flash-exp')  # Change model here
```

### Response Style

Modify the prompt in `bot.py` around line 131 to change how the bot responds.

## 🔧 Troubleshooting

### Common Issues

1. **No text copied**
   - Check if coordinates are correct for your screen
   - Run `coordinate_helper` to find correct positions
   - Ensure chat window is visible and active

2. **API Errors**
   - Verify your Gemini API key in `.env`
   - Check if you have API quota remaining


3. **Wrong sender detection**
   - Check the exact name format in your chat
   - Update `sender_name` parameter accordingly
   - Look at debug output for actual names found

### Debug Mode

The bot includes extensive debugging. Check the console output for:
- Clipboard content
- Sender detection results
- API responses
- Memory updates

## 🔒 Security & Privacy

- **API Keys**: Never commit `.env` file to version control
- **Chat Data**: Memory is stored locally in `memory.json`
- **Privacy**: Only specified sender's messages trigger responses
- **Data Retention**: Automatically limits to last 10 conversations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This bot is for educational and personal use. Please:
- Use responsibly and ethically
- Respect others' privacy
- Follow platform terms of service
- Don't use for spam or harassment

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) for powerful language model
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for automation capabilities
- [python-dotenv](https://github.com/theskumar/python-dotenv) for environment management

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section
2. Review debug output
3. Test individual components with provided utilities
4. Create an issue with detailed error information

---
