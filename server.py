#!/usr/bin/env python
from json import dumps
from flask import Flask, g, Response, request
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

app = Flask(__name__,)
gdb = GraphDatabase("http://localhost:8081/db/data/")

@app.route("/")
def get_index():
    return "Please access /api/{id}/connections or /api/are_connected?id1={id}" +\
        "&id2={id}"

@app.route("/api/<id>/connections")
def get_connections(id):
    q = "match (a)-->(x)-->(b) where a.name = {id} and b.name <> {id} "+\
        "return distinct b.name"
    second_degree = gdb.query(q, params={'id': str(id)}, returns=(int))
    
    q = "match (a)-->(x)-->(y)-->(b) where a.name = {id} and b.name <> {id}" +\
        " and y.name <> {id} and b.name <> x.name return distinct b.name"
    third_degree = gdb.query(q, params={'id': str(id)}, returns=(int))
    
    sec_nodes = []
    thrd_nodes = []
    
    for node in second_degree:
        sec_nodes.append(node[0])
    
    for node in third_degree:
        thrd_nodes.append(node[0])
        
    return Response(dumps({"second_degree_connections": sec_nodes,
        "third_degree_connections": thrd_nodes}), mimetype="application/json")

@app.route("/api/are_connected")
def get_are_connected():
    try:
        id1 = str(request.args["id1"])
        id2 = str(request.args["id2"])
    except KeyError:
        return "Please inform uri parameters id1 and id2"
    else:
        q = "match (a)-->(x)-->(b) where a.name = {id1} and b.name = " +\
        "{id2} return count(b)"
        result = gdb.query(q, params={'id1': id1, 'id2': id2}, returns=(int))
        second_degree = "true" if result[0][0] > 0 else "false"
        
        q = "match (a)-->(x)-->(y)-->(b) where a.name = {id1} and b.name = " +\
            "{id2} and y.name <> {id1} and b.name <> x.name return count(b)"
        result = gdb.query(q, params={'id1': id1, 'id2': id2}, returns=(int))
        third_degree = "true" if result[0][0] > 0 else "false"
        
        return Response(dumps({"second_degree": second_degree,
            "third_degree": third_degree}), mimetype="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)