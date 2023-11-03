import requests


def get_groups():
    r = requests.get("http://localhost:8000/group/")
    data = r.json()

    return data


