# 'a' - записывает и полезен, когда необходимо дописывать какое-то логи
# 'x' - записывает, но запрещает запись, если файл уже существует
# 'w' - записывает или перезаписывает, если файл уже существует

with open('hello', 'a') as file:
    file.write('Hello world\n')