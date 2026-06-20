import uuid
from tools.database import get_db

def handle_login(data, ip):
    db = get_db()
    cursor = db.cursor()
    
    # 1. Intentar buscar usuario (ejemplo por nombre de usuario recibido)
    username = data.get("username", "Guest")
    cursor.execute("SELECT * FROM players WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    if user:
        print(f"Login existente: {username} (ID: {user['user_id']})")
        return {"status": "success", "user_id": user['user_id']}
    else:
        # 2. Si no existe, crear usuario nuevo
        new_id = int(uuid.uuid4().int >> 96)
        cursor.execute(
            "INSERT INTO players (user_id, username, ip_last_seen) VALUES (?, ?, ?)",
            (new_id, f"NewPlayer_{new_id}", ip)
        )
        db.commit()
        print(f"Nuevo usuario registrado: {username} con ID {new_id} desde {ip}")
        return {"status": "success", "user_id": new_id, "message": "Account created"}
