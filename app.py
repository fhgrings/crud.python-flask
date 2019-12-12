from src.model.Passageiro import Passageiro

from flask import Flask, jsonify
import views


def createApp():
    app = Flask(__name__)
    views.configure(app)
    return app


app = createApp()
app.run(use_reloader=True)



