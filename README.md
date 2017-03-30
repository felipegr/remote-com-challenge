# remote-com-challenge
A Flask API that uses a Neo4j database made for a Remote.com's challenge

The challenge was to create a graph database of connected Users using Neo4j and then an API using Flask with two endpoints,
one to retrieve the 2nd and 3rd degree connections of a User and one to answer *true* or *false* if two user ids are
2nd/3rd degree connections.

The necessary installations are:
```
pip install neo4jrestclient
pip install flask
pip install locustio
```

To database is populated by the creation and import of a CSV file, for performance's sake. The first file to be executed is
`generate_csv.py`, that will create two CSV files, `users.csv` and `relations.csv`. The files are then imported into the database
by `import_csv.py` (yes, the file names are hardcoded).

The API is in the `server.py` file, the endpoints are:
- `/api/{user-id}/connections`: returns the 2nd/3rd degree connections of a user
- `/api/are_connected?id1={user1-id}&id2={user2-id}`: checks if user2 is a 2nd/3rd degree connection of user1
It is executed by `python server.py`.

Finally, Locust is used to test the API, the execution is `locust -f server_stress_test.py --host=http://0.0.0.0:8080`.
The Locust interface must be accessed at `http://localhost:8089` and the instructions must be followed.
