import pygame
from configuracion.ajustes import Ajustes
from menu.menu_principal import MenuPrincipal
from menu.menu_records import MenuRecords
from modos.modo_clasico import ModoClasico
from modos.modo_supervivencia import ModoSupervivencia

def iniciar_juego():
    pygame.init()
    ajustes = Ajustes()
    pantalla = pygame.display.set_mode((ajustes.ancho_ventana, ajustes.alto_ventana))
    pygame.display.set_caption("NEO-PONG25")

    # Inicializar records
    menu_records = MenuRecords(pantalla, [])
    menu_records.cargar_records("records_supervivencia.txt")

    corriendo = True
    while corriendo:
        # Mostrar el menú principal
        menu_principal = MenuPrincipal(pantalla, ajustes)
        modo_seleccionado = menu_principal.mostrar_menu()

        # Ejecutar el modo seleccionado
        if modo_seleccionado == 'clasico':
            print("Iniciando Modo Clásico...")
            modo_clasico = ModoClasico("Jugador 1", "Jugador 2")
            modo_clasico.jugar()
        elif modo_seleccionado == 'supervivencia':
            print("Iniciando Modo Supervivencia...")
            modo_supervivencia = ModoSupervivencia("Jugador", menu_records.guardar_record_supervivencia)
            modo_supervivencia.jugar()

if __name__ == "__main__":
    iniciar_juego()