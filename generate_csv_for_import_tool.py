import csv
import random

with open('users.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['id:ID(Person)', 'name', ':LABEL'])
    for i in range(1,101):
        wr.writerow([str(i), str(i), 'Person'])

with open('relations.csv', 'wb') as myfile:
    even_nodes = [id for id in range(1,101) if id % 2 == 0]
    random.seed(100)
    wr = csv.writer(myfile)
    wr.writerow(['TYPE', ':START_ID(Person)', ':END_ID(Person)'])
    for i in range(1,101):
        if random.random() > 0.5:
            for even_node in even_nodes:
                if even_node != i:
                    wr.writerow(['Knows', str(i), str(even_node)])