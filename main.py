import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carrera Infinita")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Cargar sonidos
crash_sound = pygame.mixer.Sound("audio/crash.mp3")

# Cargar imágenes
pista_img = pygame.image.load("media/pista.png")  # Cargar imagen de la pista
pista_img = pygame.transform.scale(pista_img, (WIDTH, HEIGHT * 2))  # Duplicar altura para efecto de desplazamiento
carrito_img = pygame.image.load("media/carrito.png")  # Cargar imagen del carrito
carrito_img = pygame.transform.scale(carrito_img, (150, 200))  # Ajustar tamaño más grande
platano_img = pygame.image.load("media/platano.png")  # Cargar imagen del plátano
platano_img = pygame.transform.scale(platano_img, (80, 160))  # Ajustar tamaño más grande

# Fuente para mensajes
font = pygame.font.Font(None, 50)

# Crear máscaras para colisión pixel-perfect
carrito_mask = pygame.mask.from_surface(carrito_img)
platano_mask = pygame.mask.from_surface(platano_img)

# Variables de desplazamiento de la pista
pista_y = 0
pista_speed = 5

# Dimensiones del auto
car_width, car_height = 150, 200
player_car = pygame.Rect(WIDTH // 2 - car_width // 2, HEIGHT - 200, car_width, car_height)

# Obstáculos
obstacle_width, obstacle_height = 80, 160
obstacles = []
obstacle_speed = 5
obstacle_positions = [50, 150, 250, 350]  # Posiciones fijas en X
obstacle_spawn_timer = 0
obstacle_spawn_delay = 30  # Aparece un obstáculo cada 60 fotogramas

# Velocidad del auto
car_speed = 10

# Reloj
clock = pygame.time.Clock()

# Estado del juego
running = True
crashed = False

# Bucle principal
while running:
    screen.fill(WHITE)
    
    if not crashed:
        # Mover la pista
        pista_y += pista_speed
        if pista_y >= HEIGHT:
            pista_y = 0
        
        # Dibujar la pista en movimiento
        screen.blit(pista_img, (0, pista_y - HEIGHT))
        screen.blit(pista_img, (0, pista_y))
        
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Controles del auto
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_car.x > 0:
            player_car.x -= car_speed
        if keys[pygame.K_RIGHT] and player_car.x < WIDTH - car_width:
            player_car.x += car_speed
        
        # Generar obstáculos en orden predefinido
        obstacle_spawn_timer += 1
        if obstacle_spawn_timer >= obstacle_spawn_delay:
            x_pos = random.choice(obstacle_positions)  # Elegir una posición fija
            obstacles.append(pygame.Rect(x_pos, 0, obstacle_width, obstacle_height))
            obstacle_spawn_timer = 0
        
        # Mover obstáculos
        for obs in obstacles[:]:
            obs.y += obstacle_speed
            if obs.y > HEIGHT:
                obstacles.remove(obs)
        
        # Dibujar auto con imagen
        screen.blit(carrito_img, (player_car.x, player_car.y))
        
        # Dibujar obstáculos con imagen
        for obs in obstacles:
            screen.blit(platano_img, (obs.x, obs.y))
        
        # Colisión pixel-perfecto
        for obs in obstacles:
            offset_x = obs.x - player_car.x
            offset_y = obs.y - player_car.y
            if carrito_mask.overlap(platano_mask, (offset_x, offset_y)):
                pygame.mixer.Sound.play(crash_sound)
                crashed = True
    else:
        # Mostrar mensaje de fin del juego
        text = font.render("¡Sigue Intentandolo CRACK ;-)!", True, RED)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()

