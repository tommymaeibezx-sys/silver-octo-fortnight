import asyncio
import json
from login import handle_login
# Importa tus otros módulos aquí

async def handle_client(reader, writer):
    data = await reader.read(1024)
    message = json.loads(data.decode())
    
    # El APK suele enviar el nombre de la función en un campo llamado 'type' o 'cmd'
    cmd = message.get("type")
    
    # Dispatcher simple
    if cmd == "login":
        response = await handle_login(message)
    elif cmd == "gs_get_friends":
        response = {"status": "success", "friends": []} # Lógica de social.py
    else:
        response = {"status": "error", "message": "Unknown command"}
    
    writer.write(json.dumps(response).encode())
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 9933)
    print("Servidor MSM activo en puerto 9933")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
