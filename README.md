# **NEO-PONG25**

¡Bienvenido a **NEO-PONG25**, una evolución moderna del clásico juego Pong! Este proyecto combina mecánicas clásicas con elementos visuales y funcionales modernos, como partículas dinámicas, modos de juego variados y un sistema de records.

---

## **Descripción del Proyecto**

**NEO-PONG25** es un juego desarrollado en Python utilizando la librería **PyGame**. El objetivo principal es ofrecer una experiencia renovada del clásico Pong, con características adicionales como:

- **Modos de Juego**:
  - **Modo Clásico**: Juega contra otro jugador o la IA en un duelo tradicional.
  - **Modo Supervivencia**: Sobrevive el mayor tiempo posible mientras la dificultad aumenta progresivamente.
- **Partículas Dinámicas**: Efectos visuales modernos que mejoran la experiencia del menú principal.
- **Sistema de Records**: Guarda y visualiza los mejores tiempos y puntuaciones en una tabla de records.
- **Interfaz Visual Mejorada**: Incluye un menú principal con un título dinámico y opciones resaltadas con un recuadro RGB.

---

## **Características Principales**

### **1. Menú Principal**
- **Título**: "NEO-PONG25" aparece destacado en la parte superior.
- **Opciones**:
  - Modo Clásico
  - Modo Supervivencia
  - Records
  - Salir
- **Recuadro RGB**: Resalta la opción seleccionada con un recuadro de colores dinámicos.
- **Partículas**: Efectos visuales en el fondo, con partículas pequeñas que se mueven hacia arriba.

### **2. Modos de Juego**
#### **Modo Clásico**
- Juega contra otro jugador o la IA.
- La velocidad de la bola aumenta cada 30 segundos, haciendo el juego más desafiante.

#### **Modo Supervivencia**
- Sobrevive el mayor tiempo posible mientras la dificultad aumenta cada 15 segundos.
- Al finalizar, el tiempo logrado se guarda en el sistema de records.

### **3. Sistema de Records**
- Guarda los mejores tiempos del modo Supervivencia en un archivo (`records_supervivencia.txt`).
- Muestra una tabla de records en el menú de records, ordenada por los mejores tiempos.

### **4. Efectos Visuales**
- **Partículas**: Generadas dinámicamente en el menú principal.
- **Recuadro RGB**: Cambia de color cada 10 frames para resaltar la opción seleccionada.

---

## **Requisitos del Sistema**

- **Python 3.8+**
- **Librerías**:
  - `pygame`

---

## **Instalación**

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu-usuario/neon-pong25.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd neon-pong25
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Cómo Jugar**

1. Ejecuta el archivo principal:
   ```bash
   python src/main.py
   ```
2. En el menú principal:
   - Usa las teclas **Arriba** y **Abajo** para navegar entre las opciones.
   - Presiona **Enter** para seleccionar una opción.
3. Disfruta de los modos de juego:
   - **Modo Clásico**: Juega contra otro jugador o la IA.
   - **Modo Supervivencia**: Sobrevive el mayor tiempo posible.

---

## **Estructura del Proyecto**

```plaintext
neon-pong-evolution/
├── src/
│   ├── main.py                  # Archivo principal del juego
│   ├── configuracion/
│   │   └── ajustes.py           # Configuración general del juego
│   ├── menu/
│   │   ├── menu_principal.py    # Lógica del menú principal
│   │   └── menu_records.py      # Lógica del menú de records
│   ├── modos/
│   │   ├── modo_clasico.py      # Lógica del modo clásico
│   │   └── modo_supervivencia.py# Lógica del modo supervivencia
│   ├── powerups/                # (Opcional) Gestión de power-ups
│   └── assets/                  # Recursos como sonidos y fuentes
├── records_supervivencia.txt    # Archivo para guardar los records
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Documentación del proyecto
```

---

## **Contribuciones**

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad:
   ```bash
   git checkout -b nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```
4. Envía tus cambios:
   ```bash
   git push origin nueva-funcionalidad
   ```
5. Abre un Pull Request.

---

## **Autor**

**Nicolás Uribe**  
Estudiante de ingenieria informatica.
