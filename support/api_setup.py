import requests
import json
import config


class ApiSetUp:

    @staticmethod
    def get_access_token():
        token_request = {
            'grant_type': 'client_credentials',
            'client_id': config.client_id,
            'client_secret': config.client_secret
        }

        response = requests.post(config.token_endpoint, data=token_request)

        if response.status_code == 200:
            token_data = response.json()
            return token_data.get('access_token')
        else:
            print(f"Error getting access token: {response.status_code}")
            return None

    @staticmethod
    def send_post_request(api_path, access_token, payload):
        request_url = config.api_url + api_path

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        }

        response = requests.post(request_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            print("POST Response:", response.text)
        else:
            print(f"Error making POST request: {response.status_code}")

    @staticmethod
    def send_delete_request(api_path, access_token):
        request_url = config.api_url + api_path

        headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        }

        response = requests.delete(request_url, headers=headers)

        if response.status_code == 204:
            print("DELETE Response:", response.text)
        else:
            print(f"Error making DELETE request: {response.status_code}")