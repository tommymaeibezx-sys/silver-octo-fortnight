class RoomManager:
    def __init__(self):
        self.active_rooms = {}

    def get_island_data(self, island_id):
        # Carga desde tu base de datos central
        # La estructura aquí es clave para la compatibilidad
        return {
            "island_id": island_id,
            "monsters": [],
            "structures": [],
            "version": "v1.0" # Añadir versión ayuda a la compatibilidad
        }

room_manager = RoomManager()
