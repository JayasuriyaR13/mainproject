from flask import Blueprint, Flask

from crop import crop
from crop1 import crop1
from crop2 import crop2
from crop3 import crop3
from crop4 import crop4
from auth import auth
from weather import weather
from chatbot import chatbot






app = Flask(__name__)



app.register_blueprint(crop1)
app.register_blueprint(crop2)
app.register_blueprint(crop3)
app.register_blueprint(crop4)
app.register_blueprint(crop)
app.register_blueprint(weather)
app.register_blueprint(auth)
app.register_blueprint(chatbot)

if __name__=="__main__":
    app.run("0.0.0.0",port=5000,debug=True)