import os

import structures
from task4 import count_questions, print_right_answers, print_max_answer_time
from task5 import task1, task2

path = './test'

def test_task4_count_questions(get_data):
    res = count_questions(structures.Game(**get_data["game"]))
    assert res == 5

def test_task4_print_right_answers(get_data):
    res = print_right_answers(structures.Game(**get_data["game"]))
    assert res == ['answr', 'answr', 'qqqqq', 2, [0, 1]]

def test_task4_print_max_answer_time(get_data):
    res = print_max_answer_time(structures.Game(**get_data["game"]))
    assert res == 129

def test_task5_task1(get_path):
    res = task1(get_path)
    assert res == 9

def test_task5_task2(get_path):
    task2(get_path)
    assert os.stat('solution.json').st_size