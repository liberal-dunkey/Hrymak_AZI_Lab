import random

# Функція для зчитування частот букв з файлу
def read_letter_frequencies(filename):
    letter_frequencies = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                letter, frequency = parts
                letter_frequencies[letter.strip()] = float(frequency.strip())
    # Додаємо частоту пробіла
    letter_frequencies[' '] = 0.17
    return letter_frequencies

# Функція для збереження таблиці заміни у файл
def save_substitution_table(substitution_table, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for letter, code in substitution_table.items():
            if letter == ' ':
                file.write(" ")
            else:
                file.write(f"{letter}: ")
            file.write(f"{code}\n")

# Функція для завантаження таблиці заміни з файлу
def load_substitution_table(filename):
    substitution_table = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                letter, code = parts
                substitution_table[letter.strip()] = code.strip()
    return substitution_table

# Функція для шифрування тексту
def encrypt(text, substitution_table):
    encrypted_text = ''
    for char in text:
        if char.upper() in substitution_table:
            # Вибираємо випадковий код для кожної букви з таблиці заміни
            code = random.choice(substitution_table[char.upper()].split())
            encrypted_text += code
        else:
            encrypted_text += char
    return encrypted_text.rstrip()

# Функція для створення та збереження таблиці заміни у файл
def create_and_save_substitution_table(letter_frequencies, filename):
    substitution_table = {}
    numbers = list(range(100, 1000))
    random.shuffle(numbers)

    for letter, frequency in sorted(letter_frequencies.items(), key=lambda x: x[1], reverse=True):
        count = int(frequency * 100)
        if count < 1:
            count = 1
        codes = [str(numbers.pop()) for _ in range(count)]
        code_str = ' '.join(codes)
        substitution_table[letter] = code_str

    # Зберігаємо таблицю заміни у файл
    save_substitution_table(substitution_table, filename)

    print("Таблиця заміни:")
    for letter, code in substitution_table.items():
        print(f"{letter}: {code}")

    return substitution_table

# Зчитуємо частоти букв з файлу 'letter_frequencies.txt'
letter_frequencies = read_letter_frequencies('letter_frequencies.txt')

# Створюємо та зберігаємо таблицю заміни у файл 'substitution_table.txt'
substitution_table = create_and_save_substitution_table(letter_frequencies, 'substitution_table.txt')

# Вхідний текст для шифрування
text = "Привіт мене звуть Ярема і мої батьки живуть на вулиці Степана Бандери Вулиця названа на честь великого Степана Бандери Героя України"

# Записуємо відкритий текст у файл 'open_text.txt'
with open('open_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)

# Шифруємо текст та записуємо його у файл 'encrypted_text.txt'
encrypted_text = encrypt(text, substitution_table)
with open('encrypted_text.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)

print("Текст успішно зашифровано та збережено у файлах.")
