from random import randint

from locust import HttpUser, task, between


class ErraticUsage(HttpUser):
    wait_time = between(1, 2)
    random_mark = randint(0, 999999)
    fake_username = f"test+{random_mark}"
    fake_password = "wrong_password"
    fake_email = f"test{random_mark}@gmail.com"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    headers = {
        "User-Agent": user_agent
    }

    @task
    def get_blueprint_by_id(self):
        self.client.get(
            f"/blueprint/{randint(999, 1003)}",
            headers=self.headers
        )

    @task
    def get_blueprint_by_name(self):
        self.client.get(
            f"/blueprint/fake",
            headers=self.headers
        )

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