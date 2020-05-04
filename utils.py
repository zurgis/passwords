from string import ascii_letters, digits
import random

# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890
allowed_chars = ascii_letters + digits

def generate_password(min_length=None, max_length=None, 
    allowed_chars=allowed_chars
):
    """Генерирует пароль для приложения"""
    if not max_length or max_length < min_length:
        max_length = 12

    if not min_length or min_length < 8 or min_length > max_length:
        min_length = 8

    # Случайная длина пароля от минимального, до максимального значения
    pass_length = random.randint(min_length, max_length)
    return ''.join(random.choices(allowed_chars, k=pass_length))