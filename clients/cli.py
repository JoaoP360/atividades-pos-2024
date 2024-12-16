import user_wrapper as users

def list_users_cli():
    users_list = users.list_users()
    print("\nLista de usuários:")
    for user in users_list:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")

def create_user_cli():
    name = input("Digite o nome: ")
    username = input("Digite o nome de usuário: ")
    email = input("Digite email: ")
    new_user = users.create_user(name, username, email)
    print("Usuário criado com sucesso:", new_user)

def read_user_cli():
    user_id = input("Digite ID de Usuário: ")
    user = users.read_user(user_id)
    if user:
        print("Detalhes do Usuário:")
        print(user)
    else:
        print("Usuário não achado.")

def update_user_cli():
    user_id = input("Digite ID de Usuário: ")
    name = input("Novo nome (deixe em branco para manter atualizado): ")
    username = input("Novo nome de usuário (deixe em branco para se manter atualizado): ")
    email = input("Novo e-mail (deixe em branco para se manter atualizado): ")
    updated_user = users.update_user(user_id, name, username, email)
    print("Usuário atualizado com sucesso:", updated_user)

def delete_user_cli():
    user_id = input("Digite ID de Usuário: ")
    result = users.delete_user(user_id)
    if result:
        print("Usuário excluído com sucesso.")
    else:
        print("Usuário não encontrado.")

def main():
    while True:
        print("\nOpições:")
        print("1. Listar todos os Usuários")
        print("2. Criar novo Usuário")
        print("3. Ler detahes do Usuário")
        print("4. Atualizar Usuário")
        print("5. Deleter um uUsuário")
        print("6. Exit")
        
        choice = input("Digite sua escolha: ")
        if choice == "1":
            list_users_cli()
        elif choice == "2":
            create_user_cli()
        elif choice == "3":
            read_user_cli()
        elif choice == "4":
            update_user_cli()
        elif choice == "5":
            delete_user_cli()
        elif choice == "6":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
