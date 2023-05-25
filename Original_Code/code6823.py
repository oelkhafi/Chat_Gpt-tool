def add_dictionary(text):
    dictionary[text]=0
def find_in_dictionary(lines):
    lines=lines.split()
    for line in lines:
        if line not in dictionary:
            if line not in invalid_dictionary:
                invalid_dictionary[line] = 1
            else:
                invalid_dictionary[line] +=1
def print_invalid_dictionary():
    for key in invalid_dictionary.keys():
        print(key)
def number_of_times (number,what):
    sum=number+1
    for step in range(number):
        if what==0:
            #print('Введите словарное слово №', sum-number,' : ', end='')
            add_dictionary(input().lower())
        elif what==1:
            #print('Введите строку №', number, ' : ', end='')
            find_in_dictionary(input().lower())
        number -= 1
dictionary,invalid_dictionary = {},{}
#print('Зададите количество слов для словаря: ',end='')
number_of_times(int(input()),0)
#print('Зададите количество строк, которые будем сверять со словарём: ',end='')
number_of_times(int(input()),1)
#print('Отсутствующие слова в словаре: ')
print_invalid_dictionary() 