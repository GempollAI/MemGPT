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
    用 ID 获取用户地址。你可以问用户 ID 是什么

    Args:
        user_id (str): 用户的 ID

    Returns:
        str: 用户的地址
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
    获取中国大陆某个地址的天气。你可以问地址是什么，或者使用 ID 获取地址

    Args:
        address (str): 中国大陆某个地址，可以模糊匹配；应该从大区到小区的顺序给出，例如：北京市海淀区

    Returns:
        str: 天气信息
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
