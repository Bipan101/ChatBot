import pyautogui
import time
import pyperclip
import google.generativeai as genai
import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv('Gemini_APiKey')) #You can modify the model name if you want to use any other AI's API key.

# Memory functions
def load_memory():
    try:
        with open('memory.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
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

def save_memory(memory_data):
    with open('memory.json', 'w', encoding='utf-8') as f:
        json.dump(memory_data, f, indent=2, ensure_ascii=False)

def update_conversation_memory(memory_data, new_message, response):
    # Add new conversation to memory
    memory_data["conversation_memory"].append({
        "timestamp": datetime.now().isoformat(),
        "message": new_message,
        "response": response
    })
    
    # Keep only last 10 conversations to avoid too much data
    if len(memory_data["conversation_memory"]) > 10:
        memory_data["conversation_memory"] = memory_data["conversation_memory"][-10:]
    
    # Update last response time
    memory_data["last_response_time"] = datetime.now().isoformat()
    
    # Set bot start timestamp if this is the first response
    if memory_data["bot_start_timestamp"] is None:
        memory_data["bot_start_timestamp"] = datetime.now().isoformat()
    
    return memory_data

def is_last_message_from_sender(chat_log, sender_name="Person's_Name") : #Enter your name here.
    # Split the chat log into individual messages
    print(f"DEBUG: Checking for sender '{sender_name}' in chat log")
    print(f"DEBUG: Chat log length: {len(chat_log)}")
    print(f"DEBUG: Last part of chat log: {repr(chat_log[-200:])}")  # Show last 200 chars
    
    messages = chat_log.strip().split("/2025] ")[-1]
    print(f"DEBUG: Last message part: {repr(messages)}")
    
    if sender_name in messages:
        print(f"DEBUG: Found sender '{sender_name}' in last message!")
        return True 
    else:
        print(f"DEBUG: Sender '{sender_name}' NOT found in last message")
        return False
    
    

    # Step 1: Click on the chrome icon to open/focus browser
pyautogui.click(1043, 1054)  # Chrome icon in taskbar

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    print("Starting text selection...")
    
    # Step 2: Select chat history area by dragging
    print(f"Moving to start position: (745, 191)")
    pyautogui.moveTo(711, 221)  # Start position - top-left of chat area
    time.sleep(0.5)  # Small pause
    
    print(f"Dragging to end position: (1798, 917)")
    pyautogui.dragTo(1798, 917, duration=2.0, button='left')  # End position - bottom-right of chat area
    time.sleep(0.5)  # Wait for selection to complete
    
    print("Text should be selected now...")

    # Step 3: Copy the selected chat history
    print("Copying selected text...")
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for copy command to complete
    
    print("Clicking to deselect...")
    pyautogui.click(685, 773)  # Click somewhere to deselect text (likely outside chat area)
    time.sleep(0.5)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    print("Checking clipboard content...")
    chat_history = pyperclip.paste()
    
    # Check if we actually got any text
    if not chat_history or len(chat_history.strip()) == 0:
        print("WARNING: No text copied! Trying alternative method...")
        
        # Try a different approach - triple click to select all text in the area
        pyautogui.click(1000, 500)  # Click in the middle of chat area
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')  # Select all
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')  # Copy
        time.sleep(1)
        chat_history = pyperclip.paste()
        
        if not chat_history:
            print("STILL NO TEXT! Check your coordinates and chat window position.")
            continue  # Skip this iteration and try again

    print("="*50)
    print("CHAT HISTORY CAPTURED:")
    print(chat_history)
    print("="*50)
    print("CHECKING IF LAST MESSAGE IS FROM SENDER:")
    print(is_last_message_from_sender(chat_history))
    print("="*50)
    
    if is_last_message_from_sender(chat_history):
        print("GENERATING RESPONSE...")
        
        # Load memory
        memory_data = load_memory()
        
        try:
            # Create Gemini model
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            
            # Build context from memory
            memory_context = ""
            if memory_data["conversation_memory"]:
                memory_context = "\n\nPrevious conversation context:\n"
                for conv in memory_data["conversation_memory"][-3:]:  # Last 3 conversations
                    memory_context += f"Previous message: {conv['message']}\nYour response: {conv['response']}\n\n"
            
            # Create enhanced prompt with memory and add your name as well as describe about you.
            prompt = f"""You are a person named YourName who speaks Nepali as well as english. You are from Nepal and you are a coder and a student of CSIT. 

Your relationship context: {memory_data['conversation_context']['relationship']}
Your communication style: {memory_data['conversation_context']['communication_style']}
Your personality: {', '.join(memory_data['conversation_context']['personality_traits'])}

{memory_context}

Current Chat History:
{chat_history}

Based on your previous conversations and personality, reply naturally as Bipan (text message only, don't use emojis). Remember your conversation history and respond contextually.

Do not start like this [21:02, 12/6/2025] Bipan Neupane:

Reply as YourName (EG: Bipan Neupane):"""
            
            print("SENDING TO GEMINI...")
            # Generate response
            response_obj = model.generate_content(prompt)
            response = response_obj.text.strip()
            print(f"GEMINI RESPONSE: {response}")
            
            # Extract just the last message from user for memory
            last_message = chat_history.split('\n')[-1] if chat_history else ""
            
            # Update memory with new conversation
            memory_data = update_conversation_memory(memory_data, last_message, response)
            save_memory(memory_data)
            print("MEMORY UPDATED!")
            
            pyperclip.copy(response)
            
        except Exception as e:
            print(f"ERROR GENERATING RESPONSE: {e}")
            response = "Sorry, I couldn't generate a response right now."
            pyperclip.copy(response)

        # Step 5: Click on the message input field to focus it
        pyautogui.click(1475, 975)  # Message input box coordinates
        time.sleep(1)  # Wait for click to register

        # Step 6: Paste the AI response
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for paste to complete

        # Step 7: Send the message
        pyautogui.press('enter')
        print("MESSAGE SENT!")
    else:
        print("SKIPPING - Last message was not from the target sender")