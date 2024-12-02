import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

def list_users():
    response = requests.get(f"{BASE_URL}/users")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
    else:
        print("Failed to retrieve users.")

def list_user_todos(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}/todos")
    if response.status_code == 200:
        todos = response.json()
        for todo in todos:
            status = "Completed" if todo['completed'] else "Pending"
            print(f"ID: {todo['id']}, Title: {todo['title']}, Status: {status}")
    else:
        print("Failed to retrieve todos for the user.")

def create_user():
    name = input("Enter name: ")
    username = input("Enter username: ")
    email = input("Enter email: ")
    user_data = {"name": name, "username": username, "email": email}

    response = requests.post(f"{BASE_URL}/users", json=user_data)
    if response.status_code == 201:
        print("User created successfully:", response.json())
    else:
        print("Failed to create user.")

def read_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        user = response.json()
        print(json.dumps(user, indent=2))
    else:
        print("User not found.")

def update_user(user_id):
    print("Enter new details (leave blank to keep current value):")
    name = input("Name: ")
    username = input("Username: ")
    email = input("Email: ")

    user_data = {}
    if name: user_data['name'] = name
    if username: user_data['username'] = username
    if email: user_data['email'] = email

    response = requests.put(f"{BASE_URL}/users/{user_id}", json=user_data)
    if response.status_code == 200:
        print("User updated successfully:", response.json())
    else:
        print("Failed to update user.")

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        print("User deleted successfully.")
    else:
        print("Failed to delete user.")

def main():
    while True:
        print("\nOpções:")
        print("1. Listar todos os usuários")
        print("2. Listar tarefas de um usuário específico")
        print("3. Criar um novo usuário")
        print("4. Ler detalhes de usuário")
        print("5. Alterar usuário")
        print("6. Deletar usuário")
        print("7. Sair")

        choice = input("Escolha uma das opções: ")
        if choice == "1":
            list_users()
        elif choice == "2":
            user_id = input("Insira o ID do usuário: ")
            list_user_todos(user_id)
        elif choice == "3":
            create_user()
        elif choice == "4":
            user_id = input("Insira o ID do usuário: ")
            read_user(user_id)
        elif choice == "5":
            user_id = input("Insira o ID do usuário: ")
            update_user(user_id)
        elif choice == "6":
            user_id = input("Insira o ID do usuário: ")
            delete_user(user_id)
        elif choice == "7":
            print("Saindo...")
            break
        else:
            print("Opção invalida.")
2
if __name__ == "__main__":
    main()
