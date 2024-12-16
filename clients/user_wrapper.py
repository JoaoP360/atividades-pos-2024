import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def list_users():
    "Listar todos os usuários."
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status() 
    return response.json()

def create_user(name, username, email):
    "Crie um novo usuário."
    user_data = {"name": name, "username": username, "email": email}
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    response.raise_for_status()
    return response.json()

def read_user(user_id):
    "Leia os detalhes de um usuário por ID."
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 404:
        return None 
    response.raise_for_status()
    return response.json()

def update_user(user_id, name=None, username=None, email=None):
    "Atualizar detalhes do usuário por ID."
    user_data = {k: v for k, v in {"name": name, "username": username, "email": email}.items() if v}
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=user_data)
    response.raise_for_status()
    return response.json()

def delete_user(user_id):
    "Excluir um usuário por ID."
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 404:
        return None 
    response.raise_for_status()
    return response.status_code == 200
