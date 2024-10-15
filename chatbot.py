# app.py

from flask import Blueprint, render_template, request, jsonify
import datetime
chatbot = Blueprint('chatbot',__name__)

# Define responses for the chatbot
responses = {
                "hi": "Hello!",
                "cs":"computer science",
                "hello": "Hi there!",
                "how are you": "I'm a chatbot, so I'm always good.",
                "what is your name": "I am a chatbot created by OpenAI.",
                "bye": "Goodbye! Have a great day!",
                "tomato":"is good",
                "time":datetime.datetime.now().strftime("%H:%M:%S"),
                
                
                
                "date":datetime.datetime.now().strftime("%Y-%m-%d"),
                "15-20 litre":"apple,peach tree,corn",
                "8-12 litre":"wheat,soybeans,potatoes",
                "20-30 litre":"banana,lemon trees",
                "rice":"2000-3000 liters per kg",
                "w1heat":"1000-1500 liters per kg",
                "maize":"1000-1500 liters per kg",
                "2000-3000 litre":"cotton,sugarcane",
                "clay soil":"rice,wheat,barley,sugarcane,cotton",
                "sandy soil":"maize,sunflower,safflower,groundnut,potato",
                "alkline soil":"cotton,sugarcane,wheat,barley,rice",
                "5-8 litre":"spinach,rose",
                "10 litre lessthan":"TOMATO,CUCUMBER,",
                "5 litre":"lettuce,basil,daisies,tulips",
                "algorithm using":"knn,decision tree, random forest,gradient boosting",
                "weather app":"weather app is a used for analysis climate condition and prediction weather because planning good for best crop growthing condition previews historical data for best farming agriculture",
                
}

def get_response(user_input):
    # Normalize the user input to lower case to handle case insensitivity
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

@chatbot.route('/current_datetime', methods=['GET'])
def current_datetime():
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"response": f"The current date and time is {current_datetime}"})

@chatbot.route('/chatbot')
def show_chatbot():
    return render_template('chatbot.html')

@chatbot.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({'response': response})


