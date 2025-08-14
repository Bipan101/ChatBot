"""
Setup script for AI ChatBot with Memory System
Run this script to set up the bot for first-time use.
"""

import os
import shutil
import subprocess
import sys

def install_requirements():
    """Install required Python packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements!")
        return False

def setup_env_file():
    """Create .env file from template if it doesn't exist"""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            shutil.copy('.env.example', '.env')
            print("📄 Created .env file from template")
            print("⚠️  Please edit .env file and add your Gemini API key!")
        else:
            print("❌ .env.example file not found!")
            return False
    else:
        print("✅ .env file already exists")
    return True

def create_memory_file():
    """Create initial memory.json file if it doesn't exist"""
    if not os.path.exists('memory.json'):
        memory_template = {
            "conversation_memory": [],
            "bot_start_timestamp": None,
            "last_response_time": None,
            "conversation_context": {
                "relationship": "close friends/romantic interest",
                "communication_style": "casual, affectionate, uses Nepali phrases",
                "personality_traits": ["caring", "student", "coder", "from Nepal"],
                "recent_topics": []
            }
        }
        
        import json
        with open('memory.json', 'w', encoding='utf-8') as f:
            json.dump(memory_template, f, indent=2, ensure_ascii=False)
        print("🧠 Created initial memory.json file")
    else:
        print("✅ memory.json already exists")

def main():
    print("🤖 AI ChatBot Setup Script")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('bot.py'):
        print("❌ Error: bot.py not found. Please run this script from the ChatBot directory.")
        return
    
    success = True
    
    # Install requirements
    if not install_requirements():
        success = False
    
    # Setup environment file
    if not setup_env_file():
        success = False
    
    # Create memory file
    create_memory_file()
    
    print("\n" + "=" * 40)
    if success:
        print("🎉 Setup completed successfully!")
        print("\n📝 Next steps:")
        print("1. Edit .env file and add your Gemini API key")
        print("2. Update bot.py with correct sender name (line 57)")
        print("3. Update bot.py with your bot name (lines 140-141)")
        print("4. Run 'python coordinate_helper.py' to find screen coordinates")
        print("5. Run 'python bot.py' to start the bot")
    else:
        print("❌ Setup completed with errors. Please check the messages above.")

if __name__ == "__main__":
    main()
