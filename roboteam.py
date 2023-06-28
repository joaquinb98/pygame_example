import pygame

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 700

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


TEXT_X = WIDTH/2 + 75
TEXT_Y = HEIGHT/2

SPEED = 1
class Animation:
    def __init__(self):
        self.moving_drone = True
        self.slide = 0
        self.running = True
        self.frames = []

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("RoboTeam UseCase")
        self.clock = pygame.time.Clock()
        

        self.drone_image = pygame.image.load("drone.png")
        self.drone_image = pygame.transform.scale(self.drone_image, (50, 50))
        self.marker_image = pygame.image.load("marker23.png")
        self.marker_image = pygame.transform.scale(self.marker_image, (20, 20))

        # Definir los pasillos
        self.hallway1 = pygame.Rect(100, 200, 100, 400)
        self.hallway2 = pygame.Rect(300, 50, 400, 100)
        self.obstacle = pygame.Rect(100, 390, 40, 20)

        self.drone_home_x = WIDTH/2 - self.drone_image.get_width()/2 + 10 
        self.drone_home_y = HEIGHT -50

        self.x = self.drone_home_x
        self.y = self.drone_home_y
        # Fuente del texto
        self.font = pygame.font.Font(None, 20)


    def dibujar_texto(self, texto, x, y):
        text_surface = self.font.render(texto, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def move_drone(self, x_final, y_final):
        
        distance_x = x_final - self.x
        distance_y = y_final - self.y

        # Calcular la magnitud del vector de distancia
        distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

        if distance == 0:
            self.x = x_final
            self.y = y_final
            return False

        # Calcular las velocidades en las direcciones X e Y
        vel_x = (distance_x / distance) * SPEED
        vel_y = (distance_y / distance) * SPEED

        # Actualizar la posición del cubo
        self.x += vel_x
        self.y += vel_y

        # Verificar si el cubo ha alcanzado la posición final
        if abs(x_final - self.x) <= SPEED and abs(y_final - self.y) <= SPEED:
            self.x = x_final
            self.y = y_final
        return True
    
    def main_loop(self):
        while self.running:
            # Dibujar elementos estáticos
            self.screen.fill(WHITE)
            pygame.draw.rect(self.screen, GRAY, self.hallway1)
            pygame.draw.rect(self.screen, GRAY, self.hallway2)
            pygame.draw.rect(self.screen, BLACK, self.obstacle)
            self.screen.blit(self.marker_image, (self.hallway1.right, self.hallway1.bottom - self.marker_image.get_height()))
            self.screen.blit(self.marker_image, (self.hallway2.left , self.hallway2.bottom))
            self.screen.blit(self.marker_image, (WIDTH/2  , HEIGHT - 100))
            font = pygame.font.Font(None, 24)
            text_surface = font.render("Pasillo 1", True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = (45, HEIGHT/2 + 20)
            self.screen.blit(text_surface, text_rect)

            text_surface = font.render("Pasillo 2", True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = (WIDTH/2 + 40, 20)
            self.screen.blit(text_surface, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.slide += 1

            if self.slide == 1:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y) 
                self.screen.blit(self.drone_image, (self.drone_home_x    , self.drone_home_y))

            elif self.slide == 2:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y) 
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.screen.blit(self.drone_image, (self.drone_home_x    , self.drone_home_y))

            elif self.slide==3:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                if self.moving_drone:
                    self.moving_drone = self.move_drone(self.hallway1.right - 20 , self.hallway1.bottom - self.marker_image.get_height() +50 )
                else:
                    self.moving_drone = True
                    self.slide += 1
                self.screen.blit(self.drone_image, (self.x, self.y))
            elif self.slide==4:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                self.dibujar_texto("4. Nueva Referencia aruco", TEXT_X, TEXT_Y + 60)
                pygame.time.delay(1000)
                self.slide += 1
                self.screen.blit(self.drone_image, (self.x, self.y))
            elif self.slide==5:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                self.dibujar_texto("4. Nueva Referencia aruco", TEXT_X, TEXT_Y + 60)
                if self.moving_drone :
                    self.moving_drone = self.move_drone(self.hallway1.right - 75 , self.hallway1.bottom - self.marker_image.get_height() +50 )
                else:
                    self.slide += 1
                    self.moving_drone = True
                self.screen.blit(self.drone_image, (self.x, self.y))
            elif self.slide==6:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                self.dibujar_texto("4. Nueva Referencia aruco", TEXT_X, TEXT_Y + 60)
                if self.moving_drone :
                    self.moving_drone = self.move_drone(self.hallway1.right - 75 , self.obstacle.bottom + 25 )
                else:
                    self.slide += 1
                    self.moving_drone = True
                self.screen.blit(self.drone_image, (self.x, self.y))        
            elif self.slide==7:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                self.dibujar_texto("4. Nueva Referencia aruco", TEXT_X, TEXT_Y + 60)
                self.dibujar_texto("5. Detectamos obstáculo", TEXT_X, TEXT_Y + 80)
                self.dibujar_texto("6. Replanificamos", TEXT_X, TEXT_Y + 100)
                pygame.time.delay(1000)
                self.slide +=1
                self.screen.blit(self.drone_image, (self.x, self.y))
            elif self.slide==8:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                self.dibujar_texto("4. Nueva Referencia aruco", TEXT_X, TEXT_Y + 60)
                self.dibujar_texto("5. Detectamos obstáculo", TEXT_X, TEXT_Y + 80)
                self.dibujar_texto("6. Replanificamos", TEXT_X, TEXT_Y + 100)
                if self.moving_drone :
                    self.moving_drone = self.move_drone(self.obstacle.right , self.obstacle.bottom -35 )
                else:
                    self.slide += 1
                    self.moving_drone = True
                self.screen.blit(self.drone_image, (self.x, self.y))  

            elif self.slide==9:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                self.dibujar_texto("4. Nueva Referencia aruco", TEXT_X, TEXT_Y + 60)
                self.dibujar_texto("5. Detectamos obstáculo", TEXT_X, TEXT_Y + 80)
                self.dibujar_texto("6. Replanificamos", TEXT_X, TEXT_Y + 100)
                if self.moving_drone :
                    self.moving_drone = self.move_drone(self.hallway1.right - 75  , 75)
                else:
                    self.slide += 1
                    self.moving_drone = True
                self.screen.blit(self.drone_image, (self.x, self.y))
            elif self.slide==10:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                self.dibujar_texto("4. Nueva Referencia aruco", TEXT_X, TEXT_Y + 60)
                self.dibujar_texto("5. Detectamos obstáculo", TEXT_X, TEXT_Y + 80)
                self.dibujar_texto("6. Replanificamos", TEXT_X, TEXT_Y + 100)
                self.dibujar_texto("7. Navegamos hacia el pasillo 2", TEXT_X, TEXT_Y + 120)
                pygame.time.delay(1000)
                self.slide +=1
            elif self.slide==11:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                self.dibujar_texto("4. Nueva Referencia aruco", TEXT_X, TEXT_Y + 60)
                self.dibujar_texto("5. Detectamos obstáculo", TEXT_X, TEXT_Y + 80)
                self.dibujar_texto("6. Replanificamos", TEXT_X, TEXT_Y + 100)
                self.dibujar_texto("7. Navegamos hacia el pasillo 2", TEXT_X, TEXT_Y + 120)
                if self.moving_drone :
                    self.moving_drone = self.move_drone(self.hallway2.right  + 25  , 75)
                else:
                    self.slide += 1
                    self.moving_drone = True
                self.screen.blit(self.drone_image, (self.x, self.y))
            elif self.slide==12:
                self.dibujar_texto("1. El UAV despega haciendo uso de los algoritmos de odometría (localización local)", TEXT_X, TEXT_Y)
                self.dibujar_texto("2. Se reconoce el primer aruco. UAV estima la posición global", TEXT_X, TEXT_Y + 20)
                self.dibujar_texto("3. Navegamos hasta el pasillo 1", TEXT_X, TEXT_Y + 40)
                self.dibujar_texto("4. Nueva Referencia aruco", TEXT_X, TEXT_Y + 60)
                self.dibujar_texto("5. Detectamos obstáculo", TEXT_X, TEXT_Y + 80)
                self.dibujar_texto("6. Replanificamos", TEXT_X, TEXT_Y + 100)
                self.dibujar_texto("7. Navegamos hacia el pasillo 2", TEXT_X, TEXT_Y + 120)
                self.dibujar_texto("8. Volvemos a casa", TEXT_X, TEXT_Y + 140)
                self.move_drone(self.drone_home_x  , self.drone_home_y)
                self.screen.blit(self.drone_image, (self.x, self.y))  

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

animation = Animation()
animation.main_loop()