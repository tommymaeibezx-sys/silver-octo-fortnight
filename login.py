def handle_login(data):
    username = data.get("username")
    # Aquí consultarías tu player_data_prod.db
    # Si el usuario es nuevo, crea su entrada básica
    print(f"Login intentado para: {username}")
    
    return {
        "status": "success",
        "user_id": 12345,
        "token": "a1b2c3d4e5",
        "game_state": {"level": 1, "currency": 1000}
    }
