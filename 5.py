import json
import os
import re

path = './test'


def task3(path):
    count = 0
    regex = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
    res = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.split('.')[0] == "filenames":
                count += 1
            with open(os.path.join(root, file), "r") as f:
                if os.stat(os.path.join(root, file)).st_size == 0:
                    continue
                for line in f:
                    emails = re.findall(regex, line)
                    if emails:
                        res.append(emails[0])
    print(count)
    print(res)


def task1(path):
    # в папке test найти все файлы filenames вывести количество
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.split('.')[0] == "filenames":
                count += 1
    return count


def task2(path):
    # в папке test найти все email адреса записанные в файлы
    regex = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
    res = []
    for root, dirs, files in os.walk(path):
        for file in files:
            with open(os.path.join(root, file), "r") as f:
                if os.stat(os.path.join(root, file)).st_size == 0:
                    continue
                for line in f:
                    emails = re.findall(regex, line)
                    if emails:
                        res.append(emails[0])
    with open('solution.json', 'w') as f:
        json.dump(res, f)



def main(path):
    print(task1(path))
    task2(path)
    task3(path)
    # дополнительно: придумать над механизмом оптимизации 2-й задачи (параллелизация)


if __name__ == '__main__':
    main(path)
