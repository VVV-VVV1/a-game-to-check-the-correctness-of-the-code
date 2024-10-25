import pygame
import sys


# Функция для проверки, указал ли игрок правильную строку с ошибкой
def check_error_line(input_line, correct_line):
    return input_line == correct_line


# Функция для переключения между игроками
def switch_player(current_player):
    return 2 if current_player == 1 else 1


# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра: Найди ошибку в коде")

# Загрузка нескольких изображений с кодом
code_images = [
    pygame.image.load('assets/image1.png'),
    pygame.image.load('assets/image2.png'),
    pygame.image.load('assets/image3.png'),
]

# Строки с ошибками для каждого изображения
error_lines = [
    5, 5, 5
]

# Настройка шрифта для текста
font = pygame.font.SysFont("Arial", 24)
input_box = pygame.Rect(50, 500, 140, 32)
color_inactive = pygame.Color('gray')
color_active = pygame.Color('dodgerblue')
color = color_inactive
active = False
text = ''
message = ''  # Сообщение о результате (верно/неверно)

# Начальные параметры игры
current_image_index = 0  # Индекс текущего изображения
error_line = error_lines[current_image_index]  # Строка с ошибкой для текущего изображения
player_turn = 1  # Текущий игрок
failed_attempts = 0  # Счётчик неудачных попыток

# Счетчики очков для игроков
score_player_1 = 0
score_player_2 = 0

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Если клик по текстовому полю
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    # Проверка правильности введенной строки
                    if text.isdigit() and check_error_line(int(text), error_line):
                        if player_turn == 1:
                            score_player_1 += 1
                        else:
                            score_player_2 += 1
                        message = f"Игрок {player_turn} угадал!"

                        # Сбрасываем счетчик неудачных попыток и переключаем картинку
                        failed_attempts = 0
                        current_image_index += 1
                        if current_image_index < len(code_images):
                            error_line = error_lines[
                                current_image_index]  # Обновление строки с ошибкой для нового изображения
                        else:
                            message = "Игра завершена!"
                            current_image_index = len(code_images) - 1  # Останавливаемся на последнем изображении
                    else:
                        message = f"Игрок {player_turn} не угадал."
                        failed_attempts += 1

                        # Если оба игрока не угадали, переключаем картинку
                        if failed_attempts == 2:
                            failed_attempts = 0  # Сбрасываем счетчик неудачных попыток
                            current_image_index += 1
                            if current_image_index < len(code_images):
                                error_line = error_lines[
                                    current_image_index]  # Обновление строки с ошибкой для нового изображения
                            else:
                                message = "Игра завершена!"
                                current_image_index = len(code_images) - 1  # Останавливаемся на последнем изображении

                        # Переключение игроков, если ещё не угадали оба
                        player_turn = switch_player(player_turn)

                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Заливка экрана
    screen.fill((255, 255, 255))

    # Отображение текущего изображения с кодом
    screen.blit(code_images[current_image_index], (50, 50))

    # Отображение сообщения (угадал/не угадал)
    result_text = font.render(message, True, (255, 0, 0) if "не угадал" in message else (0, 255, 0))
    screen.blit(result_text, (50, 450))

    # Отображение счета
    score_text = font.render(f"Игрок 1: {score_player_1} | Игрок 2: {score_player_2}", True, (0, 0, 0))
    screen.blit(score_text, (50, 550))

    # Рендеринг поля ввода
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
