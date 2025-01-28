from clases import *

#ex 3
def Appler():
    apple1 = Apple(1)
    apple2 = Apple(2)
    apple3=Apple(3)
    print(apple1)
    print(apple2)
    print(apple3)

    apple1.grow()
    print(apple1)

    tree = AppleTree(5)
    Gardener.apple_base(tree)

    gardener = Gardener("Грегор", tree)
    gardener.work()
    Gardener.apple_base(tree)

    gardener.harvest()

    gardener.work()
    gardener.work()
    Gardener.apple_base(tree)

    gardener.harvest()
    Gardener.apple_base(tree)


def ex4():
    KmrWork.cat = 'plots'
    kmr1 = KmrWork('marks.lab6.csv', 1)
    kmr2 = KmrWork('marks2.lab11.csv', 2)

    kmr2.analyze()
    KmrWork.set_cat('plots')

    kmr2.avg_plot(kmr2.get_avg_correct())
    kmr2.marks_plot(kmr2.get_score_distribution())

    KmrWork._compare_csv(1, 2)
    KmrWork._compare_avg_plots(1, 2)

    best_marks = kmr2.get_top_5_scores()
    kmr2.best_marks_plot(best_marks)
    print("Аналіз завершено\n")


while True:
    os.system('cls')
    print("\nМеню:")
    print("a. Клас Alphabet")
    print("b. Клас EngAlphabet")
    print("c. Завдання з Human та House")
    print("d. Apple")
    print("e. KmrWork")
    print("q. Вихід\n")
    choice = input("Введіть дію (a-e або q для виходу): ").lower()

    match choice:
        case 'a':
            os.system('cls')
            ua_alphabet = Alphabet()
            ua_alphabet.print_alphabet()
            print(f"Кількість літер в українському алфавіті: {ua_alphabet.letters_num()}")
            text = input("Введіть текст для перевірки української мови: ")
            if ua_alphabet.is_ua_letter(text):
                print("Цей текст українською мовою\n")
            else:
                print("Це не українська мова\n")
            os.system('pause')
            continue
        case 'b':
            os.system('cls')
            en_alphabet = EngAlphabet()
            en_alphabet.print_alphabet()
            print(f"Кількість літер в англійському алфавіті: {en_alphabet.letters_num()}")
            letter_j = "J"
            letter_shch = "Щ"
            print(f"Чи належить буква '{letter_j}' англійському алфавіту? {en_alphabet.is_en_letter(letter_j)}")
            print(f"Чи належить буква '{letter_shch}' англійському алфавіту? {en_alphabet.is_en_letter(letter_shch)}")
            print(f"Приклад тексту англійською мовою: {EngAlphabet.example()}")
            os.system('pause')
            continue
        case 'c':
            os.system('cls')
            print(Human.default_info())
            person = Human(name="Марк", age=20, money=4000)
            print(person.info())

            small_house = SmallHouse()
            print(small_house.info())
            person.buy_house(small_house)
            person.earn_money(10000)
            person.buy_house(small_house)
            print(person.info())

            os.system('pause')
            continue
        case 'd':
            os.system('cls')
            Appler()
            os.system('pause')
            continue
        case 'e':
            os.system('cls')
            ex4()
            os.system('pause')
            continue
        case 'q':
            os.system('cls')
            print('Завершення програми...\n')
            os.system('pause')
            break
        case _:
            os.system('cls')
            print('Неправильна дія\n')
            os.system('pause')
            continue