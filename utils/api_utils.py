# Directory: behave_cerberus/utils/api_utils.py
import requests

class APIUtils:
    def __init__(self):
        self.response = None

    def send_get_request(self, url):
        self.response = requests.get(url, verify=False)

    def get_status_code(self):
        return self.response.status_code

    def get_title(self):
        return self.response.json().get("title")