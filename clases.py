import string
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

#ex 1
class Alphabet:
    lang = 'Ua'
    letters = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й',
               'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']

    def __init__(self, lang=lang, letters=letters):
        self.lang = lang
        self.letters = letters

    def print_alphabet(self):
        print(f"Алфавіт ({self.lang}): {' '.join(self.letters)}")

    def letters_num(self):
        return len(self.letters)

    def is_valid_text(self, text, allowed_letters):
        punctuation = string.punctuation
        found_valid_letter = False
        for char in text.upper().strip():
            if char.isalpha():
                if char in allowed_letters:
                    found_valid_letter = True
                else:
                    return False
            elif char in punctuation or char.isspace() or char.isdigit():
                continue
            else:
                return False
        return found_valid_letter

    def is_ua_letter(self, text):
        return self.is_valid_text(text, self.letters)


class EngAlphabet(Alphabet):
    __en_letters_num = 26

    def __init__(self):
        super().__init__('En', list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    def is_en_letter(self, text):
        return self.is_valid_text(text, self.letters)

    def letters_num(self):
        return self.__en_letters_num

    @staticmethod
    def example():
        return "Hello, mr John, how are u?\n"

#ex 2
class Human:
    default_name = "Вадим"
    default_age = 21

    def __init__(self, name=default_name, age=default_age, money=0, house=None):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        house='Немає будинку'
        if self.__house:
            house=self.__house.info()
        else:
            "Немає будинку"
        return f"Ім'я: {self.name}, Вік: {self.age}, Бюджет: {self.__money}, {house}\n"

    @staticmethod
    def default_info():
        return f"Ім'я за замовчуванням: {Human.default_name}, вік за замовчуванням: {Human.default_age}\n"

    def __make_deal(self, house, price):
        if isinstance(house, House):
            self.__money -= price
            self.__house = house
        else:
            raise ValueError("Не знайдено такого будинку\n")

    def earn_money(self, amount):
        self.__money += amount
        print(f"На рахунок внесено {amount}\nРахунок: {self.__money}\n")

    def buy_house(self, house, discount=10):
        total = house.final_price(discount)
        if self.__money >= total:
            self.__make_deal(house, total)
            print(f"Куплено будинок по ціні: {total}\n")
        else:
            print(f"У вас замало грошей для купівлі\n")

class House:
    def __init__(self, area=45, price=7000):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount/100)

    def info(self):
        return f"Будинок: {self._area}м² за {self._price}."

class SmallHouse(House):
    def __init__(self):
        super().__init__(area=40, price=5000)

# ex 3
class Apple:
    states = {0: "Відсутнє", 1: "Цвітіння", 2: "Зелене", 3: "Червоне"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state< len(Apple.states)-1:
            self._state += 1

    def is_ripe(self):
        return self._state == max(Apple.states.keys())

    def __str__(self):
        state_name = Apple.states[self._state]
        return f"Яблуко {self._index}: {state_name}"


class AppleTree:
    def __init__(self, apple_count):
        self.apples = [Apple(i + 1) for i in range(apple_count)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        """Перевіряє, чи всі яблука стиглі."""
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
        """Очищає список яблук після збору"""
        self.apples = []

    def __str__(self):
        return "\n".join(str(apple) for apple in self.apples)


class Gardener:
    def __init__(self, name, tree):
        self.name = name
        self._tree = tree

    def work(self):
        print(f"Час працювати для {self.name}")
        self._tree.grow_all()

    def harvest(self):
        if self._tree.all_are_ripe():
            print("Усі яблука стиглі! Збираю")
            self._tree.give_away_all()
        else:
            print("Яблука ще недозріли")

    @staticmethod
    def apple_base(tree):
        print("Довідка про яблука:")
        print(tree)

#ex 4
class CsvKmr:
    ref = None
    num = None

    @classmethod
    def set_ref(cls, ref):
        cls.ref = ref

    @classmethod
    def set_num(cls, num):
        cls.num = num

    @classmethod
    def get_info(cls):
        return f"Файл КМР: {cls.ref}, Номер КМР: {cls.num}"


class Statistic:
    def __init__(self, file_path):
        self.file_path = file_path
        self.correct_answers = [0] * 20
        self.incorrect_answers = [0] * 20
        self.scores = []
        self.time_score = []

    def analyze(self):
        with open(self.file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                if line:
                    thescore = float(line[4].replace(',', '.'))
                    self.scores.append(thescore)

                    timer = int(line[3].split(' ')[0])
                    self.time_score.append((timer, thescore))

                    for i in range(5, 25):
                        score_str = line[i].replace(',', '.')
                        if score_str in ('-', ''):
                            continue
                        try:
                            score = float(score_str)
                        except ValueError:
                            continue
                        if score == 0.5:
                            self.correct_answers[i - 5] += 1
                        else:
                            self.incorrect_answers[i - 5] += 1

    def get_avg_correct(self):
        total_answers = [self.correct_answers[i] + self.incorrect_answers[i] for i in range(20)]

        return tuple((self.correct_answers[i] / total * 100 if total > 0 else 0)
            for i, total in enumerate(total_answers))

    def get_score_distribution(self):
        return {score: self.scores.count(score) for score in set(self.scores)}

    def get_top_5_scores(self):
        self.time_score.sort(key=lambda x: (x[1] / x[0]), reverse=True)
        return self.time_score[:5]


class Plots:
    cat = None

    @classmethod
    def set_cat(cls, cat):
        cls.cat = cat
        if not os.path.exists(cat):
            os.makedirs(cat)

    @staticmethod
    def avg_plot(percentages):
        plt.bar(range(1, len(percentages) + 1), percentages, color='blue')
        plt.xlabel("Питання")
        plt.ylabel("Відсоток правильних відповідей")
        plt.title("Гістограма правильних відповідей")
        plt.xticks(ticks=range(1, len(percentages) + 1,1), labels=range(1, len(percentages) + 1,1))

        if Plots.cat is None:
            Plots.cat = 'D:/Python/pr9/pr9/plots'

        file_path = os.path.join(Plots.cat, 'avg_plot.png')
        plt.savefig(file_path)
        plt.close()

    @staticmethod
    def marks_plot(scores_distribution):
        scores, counts = zip(*scores_distribution.items())
        plt.bar(scores, counts, color='green')
        plt.xlabel("Оцінка")
        plt.ylabel("Кількість студентів")
        plt.title("Розподіл оцінок")
        plt.xticks([1,3,7])
        file_path = os.path.join(Plots.cat, 'marks_plot.png')
        plt.savefig(file_path)
        plt.close()

    @staticmethod
    def best_marks_plot(top_scores):
        times, scores = zip(*top_scores)
        plt.bar(range(1, len(scores) + 1), scores, color='purple')
        plt.xlabel("Місце")
        plt.ylabel("Середній бал")
        plt.title("Топ-5 найкращих результатів")
        file_path = os.path.join(Plots.cat, 'best_marks_plot.png')
        plt.savefig(file_path)
        plt.close()


class KmrWork(CsvKmr, Statistic, Plots):
    kmrs = {}
    cat = None

    def __init__(self, file_path, num):
        super().__init__(file_path)
        KmrWork.kmrs[num] = self
        KmrWork.set_ref(file_path)
        KmrWork.set_num(num)

    @staticmethod
    def compare_csv(kmr1, kmr2, output_file='compare_result.txt'):
        stats1 = Statistic(KmrWork.kmrs[kmr1].file_path)
        stats2 = Statistic(KmrWork.kmrs[kmr2].file_path)

        stats1.analyze()
        stats2.analyze()

        avg1 = sum(stats1.scores) / len(stats1.scores)
        avg2 = sum(stats2.scores) / len(stats2.scores)

        result = (
            f"Порівняння КМР {kmr1} та {kmr2}:\n"
            f"Середній бал КМР {kmr1}: {avg1:.2f}\n"
            f"Середній бал КМР {kmr2}: {avg2:.2f}\n")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)

    @staticmethod
    def compare_avg_plots(kmr1, kmr2):
        KmrWork.kmrs[kmr1].analyze()
        KmrWork.kmrs[kmr2].analyze()

        avg_stat1 = KmrWork.kmrs[kmr1].get_avg_correct()
        avg_stat2 = KmrWork.kmrs[kmr2].get_avg_correct()


        plt.figure()
        plt.plot([f'Питання {i + 1}' for i in range(len(avg_stat1))], avg_stat1, label='КМР 1', color='blue')
        plt.plot([f'Питання {i + 1}' for i in range(len(avg_stat2))], avg_stat2, label='КМР 2', color='red')
        plt.title('Порівняння відсотків правильних відповідей')
        plt.xlabel('Питання')
        plt.ylabel('Відсоток правильних відповідей')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        file_path = os.path.join(KmrWork.kmrs[kmr1].cat, 'compare_avg_plots.png')
        plt.savefig(file_path)
        plt.close()

    @staticmethod
    def compare_marks_plots(kmr1, kmr2):
        marks_stat1 = KmrWork.kmrs[kmr1].marks_stat(KmrWork.kmrs[kmr1].students)
        marks_stat2 = KmrWork.kmrs[kmr2].marks_stat(KmrWork.kmrs[kmr2].students)

        marks1 = list(marks_stat1.keys())
        counts1 = list(marks_stat1.values())
        marks2 = list(marks_stat2.keys())
        counts2 = list(marks_stat2.values())

        plt.figure()
        plt.bar(marks1, counts1, width=0.4, label=f'КМР {kmr1}', align='center', color='blue')
        plt.bar(marks2, counts2, width=0.4, label=f'КМР {kmr2}', align='edge', color='red')
        plt.title('Порівняння розподілу оцінок серед студентів')
        plt.xlabel('Оцінка')
        plt.ylabel('Кількість студентів')
        plt.legend()
        plt.tight_layout()

        file_path = os.path.join(KmrWork.kmrs[kmr1].cat, 'compare_marks_plots.png')
        plt.savefig(file_path)
        plt.close()

    @staticmethod
    def compare_best_marks_plots(kmr1, kmr2, bottom_margin, top_margin):
        best_results1 = KmrWork.kmrs[kmr1].best_marks_per_time(KmrWork.kmrs[kmr1].students, bottom_margin, top_margin)
        best_results2 = KmrWork.kmrs[kmr2].best_marks_per_time(KmrWork.kmrs[kmr2].students, bottom_margin, top_margin)

        students1 = [result[0] for result in best_results1]
        avg_per_min1 = [result[2] for result in best_results1]
        students2 = [result[0] for result in best_results2]
        avg_per_min2 = [result[2] for result in best_results2]

        plt.figure()
        plt.bar(students1, avg_per_min1, width=0.4, label=f'КМР {kmr1}', align='center', color='blue')
        plt.bar(students2, avg_per_min2, width=0.4, label=f'КМР {kmr2}', align='edge', color='red')
        plt.title('Порівняння найкращих студентів за співвідношенням балів до часу')
        plt.xlabel('Студент')
        plt.ylabel('Середній бал за хвилину')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        file_path = os.path.join(KmrWork.kmrs[kmr1].cat, 'compare_best_marks_plots.png')
        plt.savefig(file_path)
        plt.close()