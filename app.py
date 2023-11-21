from flask import Flask, request, jsonify
import csv
import os
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
arquivo = 'dados.csv'

def csvCriar():
    if not os.path.exists(arquivo):
        with open(arquivo, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Tarefa", "Status"])

def csvEscrever(tarefaList):
    with open(arquivo, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Tarefa", "Status"])
        for tarefa in tarefaList:
            writer.writerow([tarefa["ID"], tarefa["Tarefa"], tarefa["Status"]])


def csvLer():
    with open(arquivo, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        tarefaList = []
        for row in reader:
            if len(row) >= 3:
                tarefaList.append({
                    "ID": int(row[0]),
                    "Tarefa": row[1],
                    "Status": row[2]
        })
    return tarefaList

csvCriar()

tarefaList = csvLer()

@app.route("/", methods=["GET"])
def index():
    tarefas = csvLer()
    tarefas_visiveis = [
        tarefa for tarefa in tarefas if tarefa["Status"] != "Deletada"
    ]
    return tarefas_visiveis

if __name__ == '__main__':
    app.run(debug=True)