# filepath: configuracion/ajustes.py
class Ajustes:
    def __init__(self):
        # Configuración de la ventana
        self.ancho_ventana = 800
        self.alto_ventana = 600
        self.tamano_fuente = 30

        # Configuración de colores
        self.color_fondo = (0, 0, 0)  # Fondo negro
        self.color_texto = (255, 255, 255)  # Texto 
        self.color_pala = (0, 255, 0)
        self.color_bola = (255, 255, 255)

        # Configuración de velocidad
        self.velocidad_enemigos = 5
        self.velocidad_bola = 7

        # Configuración de juego
        self.fps = 60
        self.puntuacion_maxima = 10
        self.numero_rondas_torneo = 3

# Constantes globales
MODOS_JUEGO = {
    "clasico": "Modo Clásico",
    "torneo": "Modo Torneo",
    "supervivencia": "Modo Supervivencia"
}

POWERUPS_DISPONIBLES = [
    {"nombre": "Aumento de Velocidad", "duracion": 5},
    {"nombre": "Reducción de Velocidad", "duracion": 5},
    {"nombre": "Vida Extra", "duracion": None}
]