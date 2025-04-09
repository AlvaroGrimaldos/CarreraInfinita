# 🛒 Carrera Infinita

**Carrera Infinita** es un juego arcade en 2D hecho con **Python** y **Pygame**, donde controlas un **carrito de supermercado** desde una vista superior. Tu misión es esquivar una lluvia de **plátanos gigantes** mientras recorres una pista infinita. El juego destaca por su estilo **pixel art chistoso**, controles sencillos, y detección de colisiones precisa.

## 🎮 Características

- Gráficos en pixel art personalizados.
- Obstáculos generados en orden aleatorio pero controlado.
- Detección de colisiones *pixel-perfect*.
- Sonido de colisión personalizado.
- Pantalla de inicio y reinicio tras perder.

## 📆 Requisitos

- Python 3.x  
- Pygame

Instala Pygame con:

```bash
pip install pygame
```

## 🚀 Cómo jugar

1. Ejecuta el archivo del juego:
   ```bash
   python main.py
   ```
2. En la pantalla de inicio, presiona cualquier tecla para comenzar.
3. Usa las flechas **← →** para mover el carrito.
4. Evita los plátanos. Si chocas, puedes reiniciar y volver a intentarlo.

## 📁 Estructura de archivos

```
/carpeta_del_juego
│
├── carrito.png            # Imagen del carrito (vista desde arriba)
├── platano.png            # Imagen del obstáculo
├── pista.png              # Fondo de la pista
├── crash.wav              # Sonido al chocar
├── main.py                # Código principal del juego
```