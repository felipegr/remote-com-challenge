import csv
import random

with open('users.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['name'])
    for i in range(1,2000001):
        user = [i]
        wr.writerow(user)

with open('relations.csv', 'wb') as myfile:
    even_nodes = [id for id in range(1,2000001) if id % 2 == 0]
    random.seed(100)
    wr = csv.writer(myfile)
    wr.writerow(['user1', 'user2'])
    for i in range(1,2000001):
        if random.random() > 0.5:
            for even_node in even_nodes:
                if even_node != i:
                    wr.writerow([i, even_node])