from bs_lib.repositories.HttpClient import HttpClient


class BlueprintsClient(HttpClient):
    def __init__(self):
        super(BlueprintsClient, self).__init__()

    def get_blueprints(self):
        pass