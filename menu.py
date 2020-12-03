import pygame
import os

class Menu:
    @staticmethod
    def mainMenu(screen, fps, bg):
        clock = pygame.time.Clock()
        result = "Continue"

        pygame.mouse.set_visible(True)
        menu_elements = pygame.sprite.Group()

        menu_is_open = True
        while menu_is_open:
            # Держим цикл на правильной скорости
            clock.tick(fps)

            # События
            for event in pygame.event.get():
                # Проверяем закрыли ли мы окно
                if event.type == pygame.QUIT:
                    menu_is_open = False
                    result = "Quit"

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu_is_open = False
                        result = "Continue"

            # Обновляем экран
            screen.blit(bg, (0, 0))
            pygame.display.update()

        return result
