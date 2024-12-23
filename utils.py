import requests
import json
import os
from apis import api_config
import uuid


def payload_handler(using_: list, data: list = None):

    if data is None:
        return using_['payload']

    if isinstance(data, str):
        data = [data]

    key_value = dict(zip(using_['required_values'], data))

    return {**using_['payload'], **key_value}


def generate_file_name(file_path: str = None, extention: str = 'json'):
    if os.path.isdir(file_path):
        value = uuid.uuid1()
        file_path = os.path.join(file_path, str(value)+"."+extention)

        return file_path
    return file_path


def return_values(which_: str, data: dict | list | str = None):
    """
    Retrieves API configuration details such as method, URL, payload, and headers.

    Args:
        which_ (str): The key to identify the specific API configuration in the `api` dictionary.

    Returns:
        tuple: A tuple containing the HTTP method (str), URL (str), payload (dict), and headers (dict).
    """
    using_ = api_config[which_]

    payload = payload_handler(using_, data)
    return using_['method'], using_['url'], payload, using_['headers']


def request_method(method: str = "GET", url: str = '', payload: dict = {}, headers: dict = {}, isJson: bool = False):
    """
    Sends an HTTP request using the specified method, URL, payload, and headers.

    Args:
        method (str): The HTTP method to use for the request (e.g., 'GET', 'POST').
        url (str): The URL to which the request is sent.
        payload (dict): The parameters or payload to send with the request.
        headers (dict): The headers to include in the request.

    Returns:
        requests.Response: The response object from the request.
    """
    if isJson:
        response = requests.request(method=method, url=url, data=payload, headers=headers)
    else:
        response = requests.request(method=method, url=url, params=payload, headers=headers)
    return response


def _save(result: list, file_path: str = "temp.json"):
    """
    Saves the provided data to a JSON file.

    Args:
        result (list): The data to be saved in the JSON file.
        file_path (str): The file path where the JSON data will be saved. Default is "temp.json".

    Returns:
        None
    """

    file_path = generate_file_name(file_path)

    temp_data = file_exists(file_path)

    temp_data.append(result)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(temp_data, f, ensure_ascii=False, indent=4)


def file_exists(file_path: str):
    """
    Checks if a JSON file exists and loads its content if it does.

    Args:
        file_path (str): The file path to check for existence.

    Returns:
        list: The loaded JSON data if the file exists, otherwise an empty list.
    """
    json_data = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as rf:
            try:
                json_data = json.load(rf)
            except Exception as exp:
                print(exp)
                json_data = []

    return json_data


def read_file(path: str):
    """
    Reads and loads JSON data from a file.

    Args:
        path (str): The file path to read the JSON data from.

    Returns:
        dict: The JSON data loaded from the file.
    """
    with open(path, 'r') as rf:
        json_data = json.load(rf)
    return json_data


def generate_name(name: str):
    name = "_".join(name.split(" "))
    name = name.replace(".", "_")
    name = name.replace("/", "_")
    name = name.lower()
    return name
