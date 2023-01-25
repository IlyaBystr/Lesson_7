def get_op():
    op= int(input("1 - добавить пользователя \n 2 - вывести таблицу \n 3 - вывести только имя и фамилию \n 4 - осторировать по именам \n 5 - отсортировать по id \n 6 - выход\n"))
    return op

def add_worker():
    id = input("Введите id\n")
    name = input("Введите Name\n")
    lastname = input("Введите фамилию\n")
    number = input("Введите номер\n")
    comments = input("Введите комментарий\n")
    line = f"{id},{name},{lastname},{number},{comments}\n"
    with open("worker_list.txt","a") as file:
        file.write(line)
    print("сохранено!")

def print_table():
    with open("worker_list.txt","r") as file:
        for line in file.readlines():
            print(line,end="")

def print_only_name():
    with open ("worker_list.txt","r") as file:
        lst = file.readline()
        for line in lst:
            a = line.split(",")
            print(f"Имя - {a[1]}, Фамилия - {a[2]}")