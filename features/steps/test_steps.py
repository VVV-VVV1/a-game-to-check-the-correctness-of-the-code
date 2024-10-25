from behave import given, when, then

@given('игрок видит изображение с кодом и строкой ошибки')
def step_given_image_with_code(context):
    context.current_image_index = 0
    context.error_lines = [5, 5, 5]
    context.input_line = None

@when('игрок вводит правильную строку ошибки')
def step_when_correct_input(context):
    context.input_line = 5  # Введённое значение

@then('игрок получает очко и игра переключается на следующее изображение')
def step_then_score_and_switch(context):
    assert context.input_line == context.error_lines[context.current_image_index]
    context.current_image_index += 1

@when('первый игрок вводит неправильную строку ошибки')
def step_when_incorrect_input(context):
    context.input_line = 3  # Неправильное значение

@then('очередь переходит ко второму игроку')
def step_then_switch_player(context):
    assert context.input_line != context.error_lines[context.current_image_index]
    context.player_turn = 2

@given(u'оба игрока видят изображение с кодом и строкой ошибки')
def step_impl(context):
    context.current_image_index = 0
    context.error_lines = [5, 5, 5]
    context.input_line_player_1 = None
    context.input_line_player_2 = None

@when('оба игрока не угадали строку ошибки')
def step_when_both_incorrect(context):
    context.input_line_player_1 = 3  # Неправильное значение
    context.input_line_player_2 = 4  # Неправильное значение

@then('изображение переключается на следующее')
def step_then_switch_image(context):
    assert context.input_line_player_1 != context.error_lines[context.current_image_index]
    assert context.input_line_player_2 != context.error_lines[context.current_image_index]
    context.current_image_index += 1
