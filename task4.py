import json

import structures

filename = 'test.json'


def count_questions(data: structures.Game):
    # вывести количество вопросов (questions)
    result = 0
    for question in data.rounds:
        result += len(question.questions)
    return result


def print_right_answers(data: structures.Game):
    # вывести все правильные ответы (correct_answer)
    result = []
    for questions in data.rounds:
        for question in questions.questions:
            result.append(question.correct_answer)
    return result


def print_max_answer_time(data: structures.Game):
    # вывести максимальное время ответа (time_to_answer)
    result = []
    for question in data.rounds:
        for time_to_answer in question.questions:
            if time_to_answer.time_to_answer:
                result.append(time_to_answer.time_to_answer)
    return sorted(result)[-1]


def main(filename):
    with open(filename) as f:
        data = json.load(f)
    print(count_questions(structures.Game(**data["game"])))
    print(print_right_answers(structures.Game(**data["game"])))
    print(print_max_answer_time(structures.Game(**data["game"])))


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки

    main(filename)
