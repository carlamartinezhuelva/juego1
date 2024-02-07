import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memoria Numérica")

# Fonts
font = pygame.font.Font(None, 36)

class MemoryGame:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.sequence = []
        self.user_sequence = []

        self.text_input = ""

        self.running = True
        self.start_game()

    def start_game(self):
        self.generate_sequence()

        while self.running:
            self.handle_events()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.check_answer()
                elif event.key == pygame.K_BACKSPACE:
                    self.text_input = self.text_input[:-1]
                else:
                    self.text_input += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.running:
                    if event.button == 1 and self.quit_button_rect.collidepoint(event.pos):
                        self.running = False
                    elif event.button == 1 and self.restart_button_rect.collidepoint(event.pos):
                        self.restart_game()

    def generate_sequence(self):
        self.sequence = [random.randint(1, 9) for _ in range(self.level)]
        self.display_sequence()

    def display_sequence(self):
        screen.fill(WHITE)
        self.draw_text("Memoriza la secuencia", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        pygame.display.flip()
        pygame.time.delay(1500)  # Breve retraso antes de mostrar la secuencia

        for num in self.sequence:
            screen.fill(WHITE)
            self.draw_text("Memoriza la secuencia", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
            self.draw_text(str(num), font, BLUE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(1000)
            screen.fill(WHITE)
            pygame.display.flip()
            pygame.time.delay(500)

    def check_answer(self):
        self.user_sequence = [int(digit) for digit in self.text_input if digit.isdigit()]

        if self.user_sequence == self.sequence:
            self.score += 1
            self.level += 1
            self.text_input = ""
            self.generate_sequence()
        else:
            self.draw_error_message()

    def draw_error_message(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.quit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif event.button == 1 and self.restart_button_rect.collidepoint(event.pos):
                        self.restart_game()

            screen.fill(WHITE)
            self.draw_text("¡Te has equivocado!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
            self.draw_quit_button()
            self.draw_restart_button()
            pygame.display.flip()

    def restart_game(self):
        self.level = 1
        self.score = 0
        self.text_input = ""
        self.start_game()  # Llamar al método start_game nuevamente para reiniciar el juego

    def draw_quit_button(self):
        quit_button_text = font.render("Salir", True, BLACK)
        quit_button_rect = quit_button_text.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT - 50))
        screen.blit(quit_button_text, quit_button_rect)
        self.quit_button_rect = quit_button_rect

    def draw_restart_button(self):
        restart_button_text = font.render("Reiniciar", True, BLACK)
        restart_button_rect = restart_button_text.get_rect(center=(3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT - 50))
        screen.blit(restart_button_text, restart_button_rect)
        self.restart_button_rect = restart_button_rect

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def draw(self):
        screen.fill(WHITE)
        self.draw_text("Nivel: " + str(self.level), font, BLACK, 100, 50)
        self.draw_text("Puntaje: " + str(self.score), font, BLACK, 300, 50)
        input_text = font.render(self.text_input, True, BLACK)
        input_rect = input_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(input_text, input_rect)
        
        # Dibujar botones de salir y reiniciar
        self.draw_quit_button()
        self.draw_restart_button()
        
        pygame.display.flip()

# Run the game
if __name__ == "__main__":
    game = MemoryGame()

# Quit Pygame
pygame.quit()
sys.exit()