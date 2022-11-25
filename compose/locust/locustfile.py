import time
from random import randint

from locust import HttpUser, task, between


class BasicUsage(HttpUser):
    wait_time = between(1, 2)
    random_mark = randint(0, 999999)
    fake_username = f"test+{random_mark}"
    fake_password = "test"
    fake_email = f"test{random_mark}@gmail.com"
    headers = dict()

    @task
    def get_blueprints(self):
        self.client.get("/blueprints", headers=self.headers)

    @task
    def post_blueprint(self):
        self.client.post(
            "/blueprint",
            headers=self.headers,
            json={
                "name": "Test",
                "description": "First Blueprint"
            }
        )

    @task
    def get_blueprint_by_id(self):
        self.client.get(
            f"/blueprint/{randint(1, 10)}"
        )

    @task
    def post_token(self):
        pass

    def on_start(self):
        with self.client.post(
            "/users/",
            json={
                "username": self.fake_username,
                "password": self.fake_password,
                "email": self.fake_email
            }
        ) as response:
            print(response.content)
        with self.client.post(
            "/token",
            data={
                "username": self.fake_username,
                "password": self.fake_password,
            }
        ) as response:
            print(response.json())
            self.headers.update({
                "Authorization": f"Bearer {response.json()['access_token']}"
            })
