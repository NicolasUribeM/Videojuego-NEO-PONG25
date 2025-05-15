import pygame
import time
import random

class ModoSupervivencia:
    def __init__(self, jugador, guardar_record_callback):
        self.jugador = jugador
        self.puntuacion_jugador = 0
        self.puntuacion_maquina = 0
        self.ancho_ventana = 800
        self.alto_ventana = 600
        self.color_fondo = (0, 0, 0)
        self.color_bola = (255, 255, 255)
        self.color_paleta_jugador = (0, 0, 255)  # Azul
        self.color_paleta_maquina = (255, 0, 0)  # Rojo
        self.velocidad_bola_base = 6  # Velocidad inicial base
        self.velocidad_bola = [self.velocidad_bola_base, self.velocidad_bola_base]
        self.velocidad_maquina = 5  # Velocidad inicial de la máquina
        self.corriendo = True
        self.tiempo_inicio = time.time()
        self.ultimo_incremento = time.time()  # Para controlar el incremento cada 30 segundos
        self.guardar_record_callback = guardar_record_callback

        # Crear la bola y las paletas
        self.bola = pygame.Rect(self.ancho_ventana // 2 - 10, self.alto_ventana // 2 - 10, 20, 20)
        self.paleta_jugador = pygame.Rect(30, self.alto_ventana // 2 - 60, 10, 100)
        self.paleta_maquina = pygame.Rect(self.ancho_ventana - 40, self.alto_ventana // 2 - 60, 10, 100)

    def reiniciar_bola(self):
        """Reinicia la posición de la bola y establece su dirección aleatoria."""
        self.bola.x = self.ancho_ventana // 2 - 10
        self.bola.y = self.alto_ventana // 2 - 10
        direccion_x = random.choice([-1, 1])  # Izquierda o derecha
        direccion_y = random.choice([-1, 1])  # Arriba o abajo
        self.velocidad_bola = [self.velocidad_bola_base * direccion_x, self.velocidad_bola_base * direccion_y]

    def mover_bola(self):
        self.bola.x += self.velocidad_bola[0]
        self.bola.y += self.velocidad_bola[1]

        # Rebote en los bordes superior e inferior
        if self.bola.top <= 0 or self.bola.bottom >= self.alto_ventana:
            self.velocidad_bola[1] = -self.velocidad_bola[1]

        # Rebote en las paletas
        if self.bola.colliderect(self.paleta_jugador) or self.bola.colliderect(self.paleta_maquina):
            self.velocidad_bola[0] = -self.velocidad_bola[0]

        # Punto para la máquina
        if self.bola.left <= 0:
            self.puntuacion_maquina += 1
            self.reiniciar_bola()

        # Punto para el jugador
        if self.bola.right >= self.ancho_ventana:
            self.puntuacion_jugador += 1
            self.reiniciar_bola()

    def mover_paleta_jugador(self, teclas):
        # Movimiento del jugador (W y S)
        if teclas[pygame.K_w] and self.paleta_jugador.top > 0:
            self.paleta_jugador.y -= 5
        if teclas[pygame.K_s] and self.paleta_jugador.bottom < self.alto_ventana:
            self.paleta_jugador.y += 5

    def mover_paleta_maquina(self):
        """Movimiento de la máquina para seguir la bola de manera más fluida."""
        # La máquina sigue la bola con un pequeño retraso
        if self.bola.centery > self.paleta_maquina.centery + 10 and self.paleta_maquina.bottom < self.alto_ventana:
            self.paleta_maquina.y += self.velocidad_maquina
        elif self.bola.centery < self.paleta_maquina.centery - 10 and self.paleta_maquina.top > 0:
            self.paleta_maquina.y -= self.velocidad_maquina

    def incrementar_dificultad(self):
        """Incrementa la velocidad de la bola y la habilidad de la máquina cada 30 segundos."""
        tiempo_actual = time.time()
        if tiempo_actual - self.ultimo_incremento >= 15:  # Cada 30 segundos
            self.velocidad_bola_base *= 1.1  # Incrementar velocidad base de la bola
            self.velocidad_maquina += 0.5  # Incrementar velocidad de la máquina
            self.ultimo_incremento = tiempo_actual  # Actualizar el tiempo del último incremento

    def dibujar_elementos(self, pantalla):
        pantalla.fill(self.color_fondo)
        # Dibujar líneas de la cancha
        # Dibujar línea central
        pygame.draw.line(pantalla, (255, 255, 255), (self.ancho_ventana // 2, 0), (self.ancho_ventana // 2, self.alto_ventana), 2)
        
        # Dibujar círculo central
        pygame.draw.circle(pantalla, (255, 255, 255), (self.ancho_ventana // 2, self.alto_ventana // 2), 50, 2)
    
        pygame.draw.rect(pantalla, self.color_paleta_jugador, self.paleta_jugador)
        pygame.draw.rect(pantalla, self.color_paleta_maquina, self.paleta_maquina)
        pygame.draw.ellipse(pantalla, self.color_bola, self.bola)

        # Dibujar puntuaciones
        fuente = pygame.font.Font(None, 36)
        texto_puntuacion = fuente.render(f"{self.puntuacion_jugador} - {self.puntuacion_maquina}", True, (255, 255, 255))
        pantalla.blit(texto_puntuacion, (self.ancho_ventana // 2 - texto_puntuacion.get_width() // 2, 20))

        # Dibujar tiempo sobrevivido
        tiempo_transcurrido = int(time.time() - self.tiempo_inicio)
        minutos = tiempo_transcurrido // 60
        segundos = tiempo_transcurrido % 60
        texto_tiempo = fuente.render(f"Tiempo: {minutos:02}:{segundos:02}", True, (255, 255, 255))
        pantalla.blit(texto_tiempo, (10, 10))
    
    def conteo_regresivo(self, pantalla):
        for i in range(5, 0, -1):
            pantalla.fill(self.color_fondo)
            fuente = pygame.font.Font(None, 100)
            texto = fuente.render(str(i), True, (255, 255, 255))
            pantalla.blit(texto, (self.ancho_ventana // 2 - texto.get_width() // 2, self.alto_ventana // 2 - texto.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(1000)  # Esperar 1 segundo

    def verificar_fin_partida(self):
        if self.puntuacion_jugador >= 5 or self.puntuacion_maquina >= 5:
            self.tiempo_final = time.time() - self.tiempo_inicio  # Guardar tiempo final
            return True
        return False

    def mostrar_resultado(self, pantalla):
        pantalla.fill(self.color_fondo)
        fuente = pygame.font.Font(None, 48)
        if self.puntuacion_jugador > self.puntuacion_maquina:
            texto = f"¡Ganaste! Tiempo: {int(time.time() - self.tiempo_inicio)} segundos"
        else:
            texto = "¡Perdiste!"
        texto_renderizado = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(texto_renderizado, (self.ancho_ventana // 2 - texto_renderizado.get_width() // 2, self.alto_ventana // 2 - 50))

        texto_opciones = fuente.render("Presiona R para reiniciar o M para volver al menú", True, (255, 255, 255))
        pantalla.blit(texto_opciones, (self.ancho_ventana // 2 - texto_opciones.get_width() // 2, self.alto_ventana // 2 + 50))
        pygame.display.flip()

    def jugar(self):
        pantalla = pygame.display.get_surface()
        reloj = pygame.time.Clock()
        self.conteo_regresivo(pantalla)

        while self.corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            teclas = pygame.key.get_pressed()
            self.mover_paleta_jugador(teclas)
            self.mover_paleta_maquina()
            self.mover_bola()
            self.incrementar_dificultad()
            self.dibujar_elementos(pantalla)

            if self.verificar_fin_partida():
                self.corriendo = False

            pygame.display.flip()
            reloj.tick(60)

        # Guardar el tiempo sobrevivido en los records
        tiempo_total = int(time.time() - self.tiempo_inicio)
        self.guardar_record_callback(self.jugador, tiempo_total)

        # Mostrar resultado y opciones
        while True:
            self.mostrar_resultado(pantalla)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:  # Reiniciar
                        self.__init__(self.jugador, self.guardar_record_callback)
                        self.jugar()
                    elif evento.key == pygame.K_m:  # Volver al menú
                        return