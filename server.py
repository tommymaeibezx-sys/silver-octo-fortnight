import asyncio
import json
from login import handle_login

async def handle_client(reader, writer):
    # Obtener IP del cliente para logs
    addr = writer.get_extra_info('peername')
    ip = addr[0] if addr else "Desconocida"
    print(f"Client {ip} connected")
    
    try:
        data = await reader.read(2048) # Buffer amplio para las peticiones
        if not data: return
            
        message = json.loads(data.decode())
        cmd = message.get("type")
        
        # Enrutador simple (Dispatcher)
        if cmd == "login":
            response = handle_login(message, ip)
        else:
            # Aquí conectarás tus funciones de logic/ (breeding.py, etc.)
            response = {"status": "error", "message": "Comando no implementado"}
        
        writer.write(json.dumps(response).encode())
        await writer.drain()
    except Exception as e:
        print(f"Error con cliente {ip}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 9933)
    print("Servidor MSM activo en puerto 9933")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
