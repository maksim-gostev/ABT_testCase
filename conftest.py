import json

import pytest


@pytest.fixture()
def get_path():
    path = './test'
    return path

@pytest.fixture()
def get_data():
    filename = 'test.json'
    with open(filename) as f:
        data = json.load(f)
    return data