"""
Configuration checker for AI ChatBot
Verifies that all necessary components are properly configured.
"""

import os
import json
from dotenv import load_dotenv

def check_files():
    """Check if all required files exist"""
    required_files = [
        'bot.py',
        'memory_manager.py',
        'coordinate_helper.py',
        '.env',
        'requirements.txt'
    ]
    
    print("📁 Checking required files...")
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING!")
            missing_files.append(file)
    
    return len(missing_files) == 0

def check_env():
    """Check environment configuration"""
    print("\n🔧 Checking environment configuration...")
    
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        return False
    
    load_dotenv()
    api_key = os.getenv('Gemini_APiKey')
    
    if not api_key:
        print("❌ Gemini_APiKey not found in .env file!")
        return False
    
    if api_key == "your_gemini_api_key_here":
        print("❌ Please replace the placeholder API key with your actual key!")
        return False
    
    if len(api_key) < 30:
        print("⚠️  API key seems too short. Please verify it's correct.")
        return False
    
    print("✅ API key configured")
    return True

def check_bot_config():
    """Check bot configuration in bot.py"""
    print("\n🤖 Checking bot configuration...")
    
    try:
        with open('bot.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check sender name
        if 'sender_name="Person\'s_Name"' in content:
            print("⚠️  Please update the sender name in bot.py (line ~57)")
            print("   Change 'Person's_Name' to the actual sender's name")
        else:
            print("✅ Sender name appears to be configured")
        
        # Check bot name
        if 'YourName' in content:
            print("⚠️  Please update your bot name in bot.py (lines ~140-141)")
            print("   Replace 'YourName' with your actual name")
        else:
            print("✅ Bot name appears to be configured")
        
        return True
        
    except FileNotFoundError:
        print("❌ bot.py file not found!")
        return False

def check_memory():
    """Check memory system"""
    print("\n🧠 Checking memory system...")
    
    if os.path.exists('memory.json'):
        try:
            with open('memory.json', 'r', encoding='utf-8') as f:
                memory = json.load(f)
            
            required_keys = ['conversation_memory', 'bot_start_timestamp', 'conversation_context']
            for key in required_keys:
                if key in memory:
                    print(f"✅ {key}")
                else:
                    print(f"❌ {key} missing in memory.json")
                    return False
            
            return True
            
        except json.JSONDecodeError:
            print("❌ memory.json is corrupted!")
            return False
    else:
        print("⚠️  memory.json not found - will be created on first run")
        return True

def main():
    print("🔍 AI ChatBot Configuration Checker")
    print("=" * 50)
    
    checks = [
        ("Files", check_files),
        ("Environment", check_env),
        ("Bot Configuration", check_bot_config),
        ("Memory System", check_memory)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    
    if all_passed:
        print("🎉 All checks passed! Your bot is ready to run.")
        print("\n🚀 To start the bot, run: python bot.py")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        print("\n📚 See README.md for detailed setup instructions")

if __name__ == "__main__":
    main()
