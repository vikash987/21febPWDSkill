from locust import HttpUser, task, between

class MyUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 3)

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_one_post(self):
        self.client.get("/posts/1")
