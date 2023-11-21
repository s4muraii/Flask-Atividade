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

def escrever_csv(tarefaList):
    with open(arquivo, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Tarefa", "Status"])
        for tarefa in tarefaList:
            writer.writerow([tarefa["ID"], tarefa["Tarefa"], tarefa["Status"]])


def ler_csv():
    with open(arquivo_csv, mode="r", newline="") as file:
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

tarefaList = ler_csv()

@app.route('/', methods=['GET'])
def get():
    with open(arquivo, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return jsonify(data)

@app.route('/api', methods=['POST'])
def post():
    data = request.json
    with open(arquivo, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    return jsonify(data)

@app.route('/api/<int:id>', methods=['PUT'])
def put(id):
    data = request.json
    with open(arquivo, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    with open(arquivo, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data[id])
    return jsonify(data[id])

@app.route('/api/<int:id>', methods=['DELETE'])
def delete(id):
    with open(arquivo, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    with open(arquivo, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data[id])
    return jsonify(data[id])

if __name__ == '__main__':
    app.run(debug=True)