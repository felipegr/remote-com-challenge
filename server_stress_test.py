from locust import HttpLocust, TaskSet, task
import random

class UserBehavior(TaskSet):

    @task(1)
    def connections(self):
        user_id = random.randint(1, 2000001)
        self.client.get('/api/' + str(user_id) + '/connections')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior