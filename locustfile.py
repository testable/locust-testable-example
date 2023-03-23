from locust import HttpUser, between, task, events

class MyLocust(HttpUser):
    wait_time = between(5, 15)

    @task
    def ibm(self):
        self.client.get("/stocks/IBM")
        
    @task
    def aapl(self):
        self.client.get("/stocks/AAPL")
