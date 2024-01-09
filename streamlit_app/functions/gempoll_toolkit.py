"""
Custom functions for MemGPT at Gempoll

Hardlinked to ~/.memgpt/functions
"""
import json
import requests
import os

with open(os.path.expanduser("~/.memgpt/functions/api.json")) as f:
    api = json.load(f)
    api_url = api["url"]
    api_key = api["key"]


def user_location(self, user_id: str) -> str:
    """
    Get the location of a user from their user ID. You can ask the user for their user ID

    Args:
        user_id (str): The user ID of the user.

    Returns:
        str: The location of the user.
    """
    url = f"{api_url}/user_location"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json={"user_id": user_id})
    return response.json()["用户地址"]


def get_weather(self, address: str) -> str:
    """
    Get the weather for a given address.

    Args:
        address (str): The address to get the weather for.

    Returns:
        str: The weather at the given address.
    """
    url = f"{api_url}/weather"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json={"address": address})
    return str(response.json())


if __name__ == "__main__":
    print(user_location("", "1234567890"))
    print(get_weather("", "北京"))
