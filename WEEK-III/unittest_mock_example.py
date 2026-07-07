import requests
from unittest import mock


def fetch_user_profile(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()


def query_database(query):
    # Simulated database call placeholder
    raise RuntimeError("Database connection not implemented")


def get_product_price(product_id):
    row = query_database(f"SELECT price FROM products WHERE id={product_id}")
    return row[0]['price']


if __name__ == '__main__':
    with mock.patch('unittest_mock_example.requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'id': 1, 'name': 'Alice'}
        mock_get.return_value.raise_for_status.return_value = None
        print(fetch_user_profile(1))

    with mock.patch('unittest_mock_example.query_database') as mock_query:
        mock_query.return_value = [{'price': 99.99}]
        print(get_product_price(42))
