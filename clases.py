import string
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt


class Alphabet:
    lang = 'Ua'
    ukrainian_alphabet_letters = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й',
               'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']

    def __init__(self, lang=lang, letters=ukrainian_alphabet_letters):
        self.lang = lang
        self.letters = letters

    def print_alphabet(self):
        print(f"Алфавіт ({self.lang}): {' '.join(self.letters)}")

    def alphabet_lenth(self):
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
    __en_alphabet_lenth = 26

    def __init__(self):
        super().__init__('En', list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    def is_en_letter(self, text):
        return self.is_valid_text(text, self.letters)

    def alphabet_lenth(self):
        return self.__en_alphabet_lenth

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
    states_of_growing = {0: "Відсутнє", 1: "Цвітіння", 2: "Зелене", 3: "Червоне"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state< len(Apple.states_of_growing)-1:
            self._state += 1

    def is_ripe(self):
        return self._state == max(Apple.states_of_growing.keys())

    def __str__(self):
        state_name = Apple.states_of_growing[self._state]
        return f"Яблуко {self._index}: {state_name}"


class AppleTree:
    def __init__(self, apple_count):
        self.apples = [Apple(i + 1) for i in range(apple_count)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
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
        number_of_answers = 20
        self.file_path = file_path
        self.correct_answers = [0] * number_of_answers
        self.incorrect_answers = [0] * number_of_answers
        self.scores = []
        self.time_score = []

    def analyze(self):
        with open(self.file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                if line:
                    self.process_score(line)
                    self.process_time_score(line)
                    self.process_answers(line)

    def process_score(self, line):
        total_score_row = 4
        score_of_the_person = float(line[total_score_row].replace(',', '.'))
        self.scores.append(score_of_the_person)

    def process_time_score(self, line):
        total_score_row = 4
        total_spented_time_row = 3
        test_time = int(line[total_spented_time_row].split(' ')[0])
        self.time_score.append((test_time, float(line[total_score_row].replace(',', '.'))))

    def process_answers(self, line):
        first_question_row = 5
        last_question_row = 25
        scored_point = 0.5
        for i in range(first_question_row, last_question_row):
            score_str = line[i].replace(',', '.')
            if score_str in ('-', ''):
                continue
            try:
                score = float(score_str)
            except ValueError:
                continue
            if score == scored_point:
                self.correct_answers[i - first_question_row] += 1
            else:
                self.incorrect_answers[i - first_question_row] += 1

    def get_avg_correct(self):
        total_answers = [self.correct_answers[i] + self.incorrect_answers[i] for i in range(20)]

        return tuple((self.correct_answers[i] / total * 100 if total > 0 else 0)
            for i, total in enumerate(total_answers))

    def get_score_distribution(self):
        return {score: self.scores.count(score) for score in set(self.scores)}

    def get_top_5_scores(self):
        self.time_score.sort(key=lambda x: (x[1] / x[0]), reverse=True)
        first_question_row = 5
        return self.time_score[:first_question_row]


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
            Plots.cat = 'plots'

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
    def _compare_csv(kmr1, kmr2, output_file='compare_result.txt'):
        stats1 = KmrWork.kmrs[kmr1].get_statistics()
        stats2 = KmrWork.kmrs[kmr2].get_statistics()

        result_data = {
            "kmr1": kmr1,
            "kmr2": kmr2,
            "avg1": stats1['average'],
            "avg2": stats2['average']
        }

        result = KmrWork._format_csv_comparison_result(result_data)
        KmrWork._save_to_file(result, output_file)

    @staticmethod
    def _format_csv_comparison_result(data):
        return (
            f"Порівняння КМР {data['kmr1']} та {data['kmr2']}:\n"
            f"Середній бал КМР {data['kmr1']}: {data['avg1']:.2f}\n"
            f"Середній бал КМР {data['kmr2']}: {data['avg2']:.2f}\n"
        )

    @staticmethod
    def _save_to_file(content, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

    def get_statistics(self):
        stats = Statistic(self.file_path)
        stats.analyze()
        return {
            'average': sum(stats.scores) / len(stats.scores),
            'scores': stats.scores
        }

    @staticmethod
    def _compare_avg_plots(kmr1, kmr2):
        avg_stats = {
            "kmr1": KmrWork.kmrs[kmr1].get_avg_correct(),
            "kmr2": KmrWork.kmrs[kmr2].get_avg_correct()
        }

        KmrWork._plot_average_comparison(avg_stats, kmr1, kmr2)

    @staticmethod
    def _plot_average_comparison(avg_stats, kmr1, kmr2):
        plt.figure()

        labels = [f'Питання {i + 1}' for i in range(len(avg_stats["kmr1"]))]
        plt.plot(labels, avg_stats["kmr1"], label=f'КМР {kmr1}', color='blue')
        plt.plot(labels, avg_stats["kmr2"], label=f'КМР {kmr2}', color='red')

        plt.title('Порівняння відсотків правильних відповідей')
        plt.xlabel('Питання')
        plt.ylabel('Відсоток правильних відповідей')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        file_path = os.path.join(KmrWork.kmrs[kmr1].cat, 'compare_avg_plots.png')
        KmrWork._save_plot(file_path)

    @staticmethod
    def _save_plot(file_path):
        plt.savefig(file_path)
        plt.close()

    @staticmethod
    def _compare_marks_plots(kmr1, kmr2):
        marks1, counts1 = KmrWork.kmrs[kmr1].get_marks_distribution()
        marks2, counts2 = KmrWork.kmrs[kmr2].get_marks_distribution()

        marks_data = {
            "kmr1": (marks1, counts1),
            "kmr2": (marks2, counts2)
        }

        KmrWork._plot_marks_comparison(marks_data, kmr1, kmr2)

    @staticmethod
    def _plot_marks_comparison(marks_data, kmr1, kmr2):
        plt.figure()

        marks1, counts1 = marks_data["kmr1"]
        marks2, counts2 = marks_data["kmr2"]

        plt.bar(marks1, counts1, width=0.4, label=f'КМР {kmr1}', align='center', color='blue')
        plt.bar(marks2, counts2, width=0.4, label=f'КМР {kmr2}', align='edge', color='red')

        plt.title('Порівняння розподілу оцінок серед студентів')
        plt.xlabel('Оцінка')
        plt.ylabel('Кількість студентів')
        plt.legend()
        plt.tight_layout()

        file_path = os.path.join(KmrWork.kmrs[kmr1].cat, 'compare_marks_plots.png')
        KmrWork._save_plot(file_path)

    def get_marks_distribution(self):
        marks_stat = self.marks_stat(self.students)
        return list(marks_stat.keys()), list(marks_stat.values())
