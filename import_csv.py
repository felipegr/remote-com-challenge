from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

gdb = GraphDatabase("http://localhost:8081/db/data/")

q="""USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:////home/ubuntu/workspace/project/users.csv" AS row
CREATE (:Person {name: row.name})"""
gdb.query(q)

q="CREATE INDEX ON :Person(name);"
gdb.query(q)

q="""USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:////home/ubuntu/workspace/project/relations.csv" AS row
MATCH (user1:Person {name: row.user1})
MATCH (user2:Person {name: row.user2})
MERGE (user1)-[:Knows]->(user2)"""
gdb.query(q)