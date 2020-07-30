from locust import HttpLocust, TaskSet, task, events

class MyTaskSet(TaskSet):
    @task(1)
    def ibm(self):
        self.client.get("/stocks/IBM")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
