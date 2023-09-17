import sys
import json

filename = 'test.json'


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    result = 0
    for question in data["game"]["rounds"]:
        result += len(question["questions"])
    return result


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    result = []
    for questions in data["game"]["rounds"]:
        for question in questions["questions"]:
            result.append(question["correct_answer"])
    return result


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    result = []
    for question in data["game"]["rounds"][1]["questions"]:
        result.append(question["time_to_answer"])
    return sorted(result)[-1]


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    print(count_questions(data))
    print(print_right_answers(data))
    print(print_max_answer_time(data))


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки

    main(filename)
