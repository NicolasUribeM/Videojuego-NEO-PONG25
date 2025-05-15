import pygame

def cargar_imagen(ruta):
    """Carga una imagen desde la ruta especificada."""
    try:
        return pygame.image.load(ruta)
    except pygame.error as e:
        print(f"Error al cargar la imagen: {ruta}")
        raise SystemExit(e)

def cargar_sonido(ruta):
    """Carga un sonido desde la ruta especificada."""
    sonido = pygame.mixer.Sound(ruta)
    return sonido

def dibujar_texto(superficie, texto, tamano_fuente, posicion, color):
    """Dibuja texto en la superficie especificada."""
    fuente = pygame.font.Font(None, tamano_fuente)  # Usa la fuente predeterminada
    texto_superficie = fuente.render(texto, True, color)
    texto_rect = texto_superficie.get_rect(center=posicion)
    superficie.blit(texto_superficie, texto_rect)

def colision(rect1, rect2):
    """Verifica si hay colisión entre dos rectángulos."""
    return rect1.colliderect(rect2)

def reiniciar_juego():
    """Reinicia el estado del juego a su configuración inicial."""
    # Aquí se pueden agregar las instrucciones para reiniciar el juego
    pass