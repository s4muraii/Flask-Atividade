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
        with open(arquivo, mode="w") as csvArquivo:
            writer = csv.writer(csvArquivo)
            writer.writerow(["ID", "Tarefa", "Status"])

def csvEscrever(tarefaList):
    with open(arquivo, mode="w") as csvArquivo:
        writer = csv.writer(csvArquivo)
        writer.writerow(["ID", "Tarefa", "Status"])
        for tarefa in tarefaList:
            writer.writerow([tarefa["ID"], tarefa["Tarefa"], tarefa["Status"]])

def csvLer():
    with open(arquivo, mode="r") as csvArquivo:
        reader = csv.reader(csvArquivo)
        next(reader)
        listaTarefas = []
        for row in reader:
            if len(row) >= 3:
                tarefaList.append({
                    "ID": int(row[0]),
                    "Tarefa": row[1],
                    "Status": row[2]
        })
    return listaTarefas

csvCriar()

tarefaList = csvLer()

@app.route("/", methods=["GET"])
def index():
    tarefas = csvLer()
    tarefas_visiveis = [
        tarefa for tarefa in tarefas if tarefa["Status"] != "Deletada"
    ]
    return tarefas_visiveis

@app.route("/delete_task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for tarefa in listaTarefas:
        if tarefa["ID"] == task_id:
            tarefa["Status"] = "Deletada"
    csvEscrever(listaTarefas)
    return jsonify({"message": "Tarefa deletada com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)