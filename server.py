import asyncio
import json
from login import handle_login

async def handle_client(reader, writer):
    # Capturar IP para logs
    addr = writer.get_extra_info('peername')
    ip = addr[0] if addr else "0.0.0.0"
    print(f"Client {ip} connected")
    
    try:
        data = await reader.read(2048)
        if not data: return
            
        request = json.loads(data.decode())
        cmd = request.get("type")
        
        # Enrutamiento basado en tus peticiones (gs_...)
        if cmd == "login":
            response = handle_login(request, ip)
        else:
            response = {"status": "error", "message": "Command not found"}
            
        writer.write(json.dumps(response).encode())
        await writer.drain()
        
    except Exception as e:
        print(f"Error procesando a {ip}: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 9933)
    print("Servidor MSM en puerto 9933 iniciado.")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
