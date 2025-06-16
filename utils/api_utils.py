# C:\Users\singh\PycharmProjects\Cerberus\utils\api_utils.py

import requests
import logging

class APIUtils:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session() # Use a session for persistent parameters across requests
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info(f"APIUtils initialized with base_url: {self.base_url}")

    def _send_request(self, method, endpoint, params=None, data=None, json=None, headers=None):
        """Internal method to send an API request."""
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"Sending {method} request to: {url} with params: {params}, data: {data}, json: {json}")
        try:
            response = self.session.request(method, url, params=params, data=data, json=json, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            self.logger.info(f"{method} response received. Status: {response.status_code}")
            return response
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTP Error for {method} {url}: {e.response.status_code} - {e.response.text}")
            raise
        except requests.exceptions.ConnectionError as e:
            self.logger.error(f"Connection Error for {method} {url}: {e}")
            raise
        except requests.exceptions.Timeout as e:
            self.logger.error(f"Timeout Error for {method} {url}: {e}")
            raise
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An unexpected error occurred for {method} {url}: {e}")
            raise

    def get(self, endpoint, params=None, headers=None):
        """Sends a GET request."""
        return self._send_request('GET', endpoint, params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        """Sends a POST request."""
        return self._send_request('POST', endpoint, data=data, json=json, headers=headers)

    def put(self, endpoint, data=None, json=None, headers=None):
        """Sends a PUT request."""
        return self._send_request('PUT', endpoint, data=data, json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        """Sends a DELETE request."""
        return self._send_request('DELETE', endpoint, headers=headers)

    def head(self, endpoint, headers=None):
        """Sends a HEAD request."""
        return self._send_request('HEAD', endpoint, headers=headers)

    def options(self, endpoint, headers=None):
        """Sends an OPTIONS request."""
        return self._send_request('OPTIONS', endpoint, headers=headers)