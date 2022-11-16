from flask import Flask
import pickle
#importing the inputScript file used to analyze the URL


#load model
app = Flask(__name__)
model = pickle.load(open('Phishing_Website.pkl', 'rb'))
