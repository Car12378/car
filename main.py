import pygame
import random

# Pygame başlatma
pygame.init()

# Ekran ayarları
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Basit Araba Yarışı Oyunu')

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Araba sınıfı
class Car(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
                    self.image = pygame.image.load('car.png').convert_alpha()
                            self.rect = self.image.get_rect()
                                    self.rect.center = (width // 2, height - 50)
                                        
                                            def update(self):
                                                    keys = pygame.key.get_pressed()
                                                            if keys[pygame.K_LEFT]:
                                                                        self.rect.x -= 5
                                                                                if keys[pygame.K_RIGHT]:
                                                                                            self.rect.x += 5

                                                                                            # Düşman araba sınıfı
                                                                                            class EnemyCar(pygame.sprite.Sprite):
                                                                                                def __init__(self):
                                                                                                        super().__init__()
                                                                                                                self.image = pygame.image.load('enemy_car.png').convert_alpha()
                                                                                                                        self.rect = self.image.get_rect()
                                                                                                                                self.rect.x = random.randrange(width - self.rect.width)
                                                                                                                                        self.rect.y = random.randrange(-150, -50)
                                                                                                                                            
                                                                                                                                                def update(self):
                                                                                                                                                        self.rect.y += 5
                                                                                                                                                                if self.rect.y > height:
                                                                                                                                                                            self.rect.y = random.randrange(-150, -50)
                                                                                                                                                                                        self.rect.x = random.randrange(width - self.rect.width)

                                                                                                                                                                                        # Sprite grupları
                                                                                                                                                                                        all_sprites = pygame.sprite.Group()
                                                                                                                                                                                        enemies = pygame.sprite.Group()

                                                                                                                                                                                        # Oyuncu arabası
                                                                                                                                                                                        player = Car()
                                                                                                                                                                                        all_sprites.add(player)

                                                                                                                                                                                        # Düşman arabaları
                                                                                                                                                                                        for i in range(5):
                                                                                                                                                                                            enemy = EnemyCar()
                                                                                                                                                                                                all_sprites.add(enemy)
                                                                                                                                                                                                    enemies.add(enemy)

                                                                                                                                                                                                    # Oyun döngüsü
                                                                                                                                                                                                    running = True
                                                                                                                                                                                                    while running:
                                                                                                                                                                                                        for event in pygame.event.get():
                                                                                                                                                                                                                if event.type == pygame.QUIT:
                                                                                                                                                                                                                            running = False
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                    # Güncellemeler
                                                                                                                                                                                                                                        all_sprites.update()
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                # Çarpışma kontrolü
                                                                                                                                                                                                                                                    if pygame.sprite.spritecollide(player, enemies, False):
                                                                                                                                                                                                                                                            running = False
                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                    # Ekranı temizleme
                                                                                                                                                                                                                                                                        screen.fill(BLACK)
                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                # Tüm sprite'ları çizme
                                                                                                                                                                                                                                                                                    all_sprites.draw(screen)
                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                            # Ekranı güncelleme
                                                                                                                                                                                                                                                                                                pygame.display.flip()

                                                                                                                                                                                                                                                                                                # Pygame kapatma
                                                                                                                                                                                                                                                                                                pygame.quit()

                                                                                                                                                                                                                                                                                                
