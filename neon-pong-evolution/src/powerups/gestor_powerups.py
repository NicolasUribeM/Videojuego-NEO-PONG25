class GestorPowerUps:
    def __init__(self):
        self.powerups = []
        self.tiempo_activacion = 5  # Tiempo en segundos que un power-up permanece activo

    def crear_powerup(self, tipo, posicion):
        powerup = {
            'tipo': tipo,
            'posicion': posicion,
            'activo': False,
            'tiempo_restante': self.tiempo_activacion
        }
        self.powerups.append(powerup)

    def activar_powerup(self, powerup):
        powerup['activo'] = True
        powerup['tiempo_restante'] = self.tiempo_activacion

    def actualizar_powerups(self, delta_tiempo):
        for powerup in self.powerups:
            if powerup['activo']:
                powerup['tiempo_restante'] -= delta_tiempo
                if powerup['tiempo_restante'] <= 0:
                    self.desactivar_powerup(powerup)

    def desactivar_powerup(self, powerup):
        powerup['activo'] = False
        powerup['tiempo_restante'] = self.tiempo_activacion

    def obtener_powerups_activos(self):
        return [p for p in self.powerups if p['activo']]