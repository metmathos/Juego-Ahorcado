
# 🎮 Juego del Ahorcado (Versión Pygame)

Este proyecto es una implementación del clásico **Juego del Ahorcado**, desarrollado en **Python** utilizando la biblioteca **Pygame**. Permite al jugador adivinar una palabra oculta, con una interfaz gráfica que representa tanto la horca como el progreso del juego.

## 👨‍💻 Autor

- **Matías Herrera**
- 📅 Fecha de creación: 28-10-2024
- 🧩 Versión: 1.0

## ✨ Características

- 🟢 **Escena de introducción**: Presenta el título del juego y un botón para comenzar. Implementada en el método `intro()`.
- 🟡 **Escena principal**: Muestra la horca, la progresión del ahorcado, la palabra a adivinar, letras erróneas e intentos restantes. Todo se dibuja con `pygame.draw`. Implementada en el método `principal()`.
- 🟣 **Escena de victoria**: Incluye una animación rudimentaria mediante retardos. Método `estado_ganar()`.
- 🔴 **Escena de derrota**: Representa el fracaso con etapas de dibujo animadas por retardos. Método `estado_perder()`.
- 🔁 **Opciones de reinicio y salida**: Disponibles en las escenas de victoria y derrota.

## ⚙️ Requisitos

- 🐍 Python 3.x
- 🎮 Biblioteca Pygame

Para instalar Pygame:

    pip install pygame

▶️ Ejecución

Para ejecutar el juego:

    python main.py


🚧 Mejoras futuras (to-do)

    📖 Base de datos de palabras para adivinar.
    🖼️ Bases de datos de imágenes para las escenas de victoria, derrota, introducción y principal.
    🗂️ Clasificación de palabras por temas (mostrar tema actual en pantalla).
    🏆 Sistema de puntaje.
    💾 Sistema de guardado de puntajes.