def show_all():
    file = open('phone_book\sample.txt', 'r', encoding = 'UTF-8')
    data = file.readlines()
    for i in data:
        print(i, end='')
    file.close
    print()
    

def add_contact():
    file = open('phone_book\sample.txt', 'a', encoding = 'UTF-8')
    data = input("Введите фамилию, телефон, комментраий (разделяя ';'): ")
    file.write(data)
    data +='\n'
    file.close
    

def change_contact():
    old_name = input('Что хотим переименовать?: ')
    new_name = input('Как хотим переименовать?: ')
    search_text = old_name
    replace_text = new_name
    with open('phone_book\sample.txt', 'r', encoding = 'UTF-8') as file:
        data = file.read()
        data = data.replace(search_text, replace_text)
    with open('phone_book\sample.txt', 'w', encoding = 'UTF-8') as file:
        file.write(data)
    print("Text replaced")
    file.close
    

def find_contact():
    find_ctring = input("Введите поисковый запрос: ")
    file = open('phone_book\sample.txt', 'r', encoding = 'UTF-8')
    data = file.readlines()
    for data_str in data:
        if find_ctring in data_str:
            print("Вы искали = ", data_str)
    file.close


def delete_contact():
    try:
        name = input('Введите текст строки, которую хотим удалить?: ')
        with open('phone_book\sample.txt', 'r', encoding = 'UTF-8') as fr:
            lines = fr.readlines()
        with open('phone_book\sample.txt', 'w', encoding = 'UTF-8') as fw:
            for line in lines: 
                if line.strip('\n') != name:
                    fw.write(line)
        print("Удалено")
    except:    
        print("Ошибка, что-то пошло не так")
          

def main_menu():
    print("Main menu")
    print("1. Посмотреть контакты")
    print("2. Добавить новый контакт")
    print("3. Редактировать контакт")
    print("4. Поиск контакта")
    print("5. Удалить контакт")
    print("6. Вернутся в main menu")

if __name__ == "__main__":
    main_menu()

    while True:
        choose = int(input("Введите пункт меню: "))
        if choose == 1:
            show_all()
        if choose == 2:
            add_contact()
        if choose == 3:
            change_contact()
        if choose == 4:
            find_contact()
        if choose == 5:
            delete_contact()
        if choose == 6:
            main_menu()
