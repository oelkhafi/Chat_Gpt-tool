#1 Ввод строки, преобразование в список
g = input()        # Исходная строка 
genome = list(g)   # Исходная строка в виде списка
#2 Проверка соответствия исходных символов алфавиту и регистру 
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
abc = list(ABC)
for i in genome:
    if i not in abc:
        genome = None
#3 Создание вспомогательного списка вида: [[aaaabbcaa],[111111111]]
repeat = [1 for i in range(len(genome))]  # число повторений
code = [genome, repeat]                   # вспомогательный список
#4 Преобразование вспомогательного списка с подсчётом повторений
count = 0
while count <= len(g):
    for i in range(1, len(g)): 
        if i == len(code[1]):
            break
        elif i > len(code[1]):
            break
        elif code[0][i] != code [0][i-1]:
            continue
        elif (code[0][i] == code [0][i-1]):
            code[1][i] += code [1][i-1]
            del code[0][i-1]
            del code[1][i-1]
    count += 1
#5 Подготовка и вывод результата
result = []                                                # Результат         
repeat = [str(repeat[i]) for i in range(len(repeat))]      # [int] -> [str]
result = [genome[i]+repeat[i] for i in range(len(genome))] # объединение списков
result = ''.join(result)  # Преобразование списка в строку
print(result) 