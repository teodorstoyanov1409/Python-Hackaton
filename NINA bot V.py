import datetime
import requests
import pytz
import random

def get_local_time():
    tz = pytz.timezone("Europe/Sofia")
    return datetime.datetime.now(tz).strftime("%H:%M:%S")

def get_simulated_weather():
    weather_options = [
        "☀️ Sunny",
        "⛅ Partly cloudy",
        "🌧️ Rainy",
        "⛈️ Stormy",
        "❄️ Snowy",
        "🌬️ Windy"
    ]
    return random.choice(weather_options)

def get_day_info():
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return days[datetime.datetime.now().weekday()]

print("🎃 Welcome to the NINA Bot!")
print("I can help you find fun activities and answer your questions!")
print("Type 'exit' to quit the bot.")
print("-" * 50)

while True:
    user_input = input("\n💬 What would you like to do? (activities/question/exit): ").lower()
    
    if user_input == "exit":
        print("🖐🎃 Thanks for using NINA! Goodbye!")
        break
    
    elif user_input == "activities":
        print("\n🎯 Let me recommend some activities for you!")
        mood = input("What's your mood? (active/relaxed/creative/social): ").lower()
        
        if mood == "active":
            print("🏃‍♂️ Active recommendations:")
            print("• Go for a run or bike ride")
            print("• Play basketball or tennis")
            print("• Try a new workout video")
            print("• Go hiking or rock climbing")
            
        elif mood == "relaxed":
            print("🧘‍♂️ Relaxed recommendations:")
            print("• Watch a good movie or series")
            print("• Read a book in a cozy spot")
            print("• Take a warm bath with music")
            print("• Do some meditation or yoga")
            
        elif mood == "creative":
            print("🎨 Creative recommendations:")
            print("• Try drawing or painting")
            print("• Write in a journal or start a story")
            print("• Learn to play a musical instrument")
            print("• Do some crafts or DIY projects")
            
        elif mood == "social":
            print("👨‍💻 Social recommendations:")
            print("• Call a friend or family member")
            print("• Organize a game night")
            print("• Go out for coffee with someone")
            print("• Join a local club or meetup")
            
        else:
            print("🎲 Here are some random fun activities:")
            print("• Learn a new skill online")
            print("• Cook a new recipe")
            print("• Organize your room")
            print("• Plan your next adventure")
    
    elif user_input == "question":
        print("\n❓ Ask me anything! I'll do my best to help.")
        question = input("Your question: ")
        
        question_lower = question.lower()
        
        if "time" in question_lower or "clock" in question_lower:
            current_time = get_local_time()
            print("⌚ Current time:", current_time)
            
        elif "date" in question_lower or "day" in question_lower:
            day = get_day_info()
            date = datetime.datetime.now().strftime("%B %d, %Y")
            print(f"📅 Today is {day}, {date}")
    
        elif "weather" in question_lower:
            weather = get_simulated_weather()
            print(f"🌤️ Simulated weather: {weather}")
            print("(Check a real weather app for accurate information!)")
            
        elif "food" in question_lower or "eat" in question_lower:
            foods = ["🍕 Pizza", "🍝 Pasta", "🥗 Salad", "🍜 Soup", "🌮 Tacos", "🍣 Sushi"]
            suggestion = random.choice(foods)
            print(f"🍽️ Food suggestion: {suggestion}")
            
        elif "movie" in question_lower or "film" in question_lower:
            genres = ["😂 Comedy", "🎬 Action", "😢 Drama", "🚀 Sci-fi", "😱 Horror", "💕 Romance"]
            suggestion = random.choice(genres)
            print(f"🎬 Movie suggestion: {suggestion}")
            
        elif "book" in question_lower or "song" in question_lower:
            types = ["📖 Fiction", "📚 Non-fiction", "📝 Poetry", "🕵️ Mystery", "🔬 Science", "📜 History"]
            suggestion = random.choice(types)
            print(f"📚 Book suggestion: {suggestion}")
            
        elif "game" in question_lower:
            games = ["🎮 Video games", "🎲 Board games", "🃏 Card games", "⚽ Sports", "🧩 Puzzles"]
            suggestion = random.choice(games)
            print(f"🎮 Game suggestion: {suggestion}")
            
        elif "help" in question_lower:
            print("👍 I'm here to help! Ask me about activities, entertainment, or general questions.")
            
        else:
            print("🤔 That's an interesting question! While I don't have a specific answer,")
            print("   I suggest searching online or asking friends for their opinions.")
    
    else:
        print("❌ I didn't understand that. Please type 'activities', 'question', or 'exit'.")
        
    if user_input != "exit":
        continue_chat = input("\n🔄 Would you like to do something else? (yes/no): ").lower()
        if continue_chat == "no":
            print("👋🎃 Thanks for using NINA! Goodbye!")
            break
