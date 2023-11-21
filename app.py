from flask import Flask, request, jsonify
import csv
import os
import random
from flask_cors import CORS

app = Flask(__name__)