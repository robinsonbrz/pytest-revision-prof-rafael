import requests

def get_user_data(user_id):
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

if __name__ == '__main__':
    get_user_data(1)