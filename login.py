import random
import uuid

# Contador global simple o podrías leer el último ID desde tu DB
PLAYER_COUNT = 0 

def generate_new_player():
    global PLAYER_COUNT
    PLAYER_COUNT += 1
    
    username = f"NewPlayer{PLAYER_COUNT}"
    # Genera un ID único y constante
    user_id = int(uuid.uuid4().int >> 96) 
    
    return {
        "username": username,
        "user_id": user_id
    }

def handle_login(data):
    # Aquí puedes añadir lógica para guardar el usuario en tu DB
    new_user = generate_new_player()
    print(f"Nuevo usuario creado: {new_user['username']} con ID: {new_user['user_id']}")
    
    return {
        "status": "success",
        "user_info": new_user
    }
