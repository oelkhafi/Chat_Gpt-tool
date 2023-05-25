def func(check: str, err: str):  # проверка необходимости вызова ошибки
    if err in backlog:  # проверка на наличие в backlog вызова ошибки
        return True
    if errors[err] is False:  # если мы дошли до верхней точки
        if err == check:
            backlog.add(check)  # добавляем в backlog, если эту ошибку мы и проверяем
        else:
            return  # делаем возврат для прохода в ширину
    for i in errors[err]:  # цикл для проверки всех предков
        if func(check, i):
            return True  # если где-нибудь в backlog встречалась ошибка-предок - функция возвращает True
    backlog.add(check)  # добавление ошибки в backlog, т.к. ничего из вышеперечисленного не было выполнено
backlog = set()  # множество вызванных функций
errors = {}  # граф ошибок-наследников и ошибок-предков
for i in range(int(input())):   # цикл, формирующий граф
    err = input()  # err - ошибки, из которых мы составляем граф
    if ':' in err:
        err = err.split()
        for j in err[2:]:
            if err[0] not in errors:
                errors[err[0]] = []
            errors[err[0]].append(j)
            if j not in errors:
                errors[j] = []
    else:
        errors[err] = []
for i in range(int(input())): # цикл проверки необходимости вызова ошибки
    err_str = input()
    if func(err_str, err_str):
        print(err_str) 