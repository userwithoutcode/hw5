"""
Домашнее задание для лекции "Задачки на собеседованиях для продвинутых,
с тонкостями языка"

Описание
    1. Перестроить заданный связанный список (LinkedList) в обратном порядке.
    Для этого использовать метод `LinkedList.reverse()`, представленный
    в данном файле.
    2. Определить сложность алгоритма.
    3. Определить потребление памяти в big-O notation.

Примечание
    Проверить работоспособность решения можно при помощи тестов,
    которые можно запустить следующей командой:

    python3 -m unittest linked_list_reverse.py
"""

import unittest

from typing import Iterable


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # type: LinkedListNode


class LinkedList:
    def __init__(self, values: Iterable):
        previous = None
        self.head = None
        for value in values:
            current = LinkedListNode(value)
            if previous:
                previous.next = current
            self.head = self.head or current
            previous = current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def reverse(self):  # разбираем реверс
        if self.head:
            previous = None
            current = self.head
            while current:
                future = current.next
                current.next = previous
                previous = current
                current = future
            self.head = previous


class LinkedListTestCase(unittest.TestCase):
    def test_reverse(self):
        cases = dict(
            empty=dict(
                items=[],
                expected_items=[],
            ),
            single=dict(
                items=[1],
                expected_items=[1],
            ),
            double=dict(
                items=[1, 2],
                expected_items=[2, 1],
            ),
            triple=dict(
                items=[1, 2, 3],
                expected_items=[3, 2, 1],
            ),
        )
        for case, data in cases.items():
            with self.subTest(case=case):
                linked_list = LinkedList(data['items'])
                linked_list.reverse()
                self.assertListEqual(
                    data['expected_items'],
                    list(linked_list),
                )


def my_test_list():
    l = LinkedList([1, 2, 3, 4])  # создаем объект l класса LinkedList из списка данных
    print('Прямой лист', list(l))
    l.reverse()  # переворачиваем список
    print('Обратный лист', list(l))


my_test_list()


'''
Ответы на вопросы
2. Определить сложность алгоритма.
- Сложность данного алгоритма O(n)
в данном примере представлена линейная зависимость от количества элементов в списке.

3. Потребление памяти
Потребление памяти данного алгоритма будет равно 1 т.к на функция получает список
и возврашает тот же список, не создавая новых переменных
'''

print('Big O')


def deductName():
    l = LinkedList([1, 2, 3, 6])
    for x in l:
        x -= 1
        print(x)


deductName()

print('Logarithmic')


def divide():  # разбираемся с Big 0
    l = LinkedList([1, 2, 3, 4])
    for x in l:
        while x > 1:
            x /= 2
            print(x)

divide()


