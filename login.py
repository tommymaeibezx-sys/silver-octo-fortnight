import uuid
import random

# Simulador de persistencia de conteo (deberías leer esto de tu DB)
last_player_num = 0

def handle_login(data, ip):
    global last_player_num
    last_player_num += 1
    
    player_data = {
        "username": f"NewPlayer{last_player_num}",
        "user_id": int(uuid.uuid4().int >> 96), # ID único de 64 bits
        "ip_last_seen": ip
    }
    
    print(f"Login exitoso: {player_data['username']} (ID: {player_data['user_id']}) desde {ip}")
    
    return {
        "status": "success",
        "user_info": player_data
    }
