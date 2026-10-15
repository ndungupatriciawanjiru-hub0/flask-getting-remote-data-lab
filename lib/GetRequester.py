import requests
import json


class GetRequester:
    def __init__(self, url):
        # Store the endpoint this instance will query
        self.url = url

    def get_response_body(self):
        # Send an HTTP GET request and return the raw response body (bytes)
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # Parse the raw body into Python data structures (list of dicts)
        return json.loads(self.get_response_body())