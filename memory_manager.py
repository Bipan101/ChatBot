import json
from datetime import datetime

def view_memory():
    try:
        with open('memory.json', 'r', encoding='utf-8') as f:
            memory = json.load(f)
        
        print("="*60)
        print("BOT MEMORY VIEWER")
        print("="*60)
        
        if memory["bot_start_timestamp"]:
            start_time = datetime.fromisoformat(memory["bot_start_timestamp"])
            print(f"Bot started replying: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        if memory["last_response_time"]:
            last_time = datetime.fromisoformat(memory["last_response_time"])
            print(f"Last response: {last_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        print(f"\nTotal conversations stored: {len(memory['conversation_memory'])}")
        
        print("\nRECENT CONVERSATIONS:")
        print("-" * 40)
        
        for i, conv in enumerate(memory["conversation_memory"][-5:], 1):
            timestamp = datetime.fromisoformat(conv["timestamp"])
            print(f"\n{i}. {timestamp.strftime('%H:%M:%S')}")
            print(f"Message: {conv['message']}")
            print(f"Response: {conv['response']}")
        
        print("\nCONTEXT:")
        print(f"Relationship: {memory['conversation_context']['relationship']}")
        print(f"Style: {memory['conversation_context']['communication_style']}")
        
    except FileNotFoundError:
        print("No memory file found yet!")

def clear_memory():
    confirm = input("Are you sure you want to clear all memory? (yes/no): ")
    if confirm.lower() == 'yes':
        memory = {
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
        with open('memory.json', 'w', encoding='utf-8') as f:
            json.dump(memory, f, indent=2, ensure_ascii=False)
        print("Memory cleared!")
    else:
        print("Memory not cleared.")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. View memory")
    print("2. Clear memory")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        view_memory()
    elif choice == "2":
        clear_memory()
    else:
        print("Invalid choice!")
