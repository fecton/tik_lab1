"""
File: task_3.py
Theory of information and coding
Laboratory word #3

Task 3:
Знайти швидкість передачу повідомлень, складених із таких символів.
1.3 Побудувати оптимальний код повідомленення з використанням методу
Шеннона-Фано, описаного вище.

1.4 Отримайний код має бути переданий ввід кодера (пристрій 1)
на декодер (пристрій 2).

1.5 Декодер має розкодувати отриману послідовність. Можна
Використовувати будь-які пристої для кодування та декодування
"""

from .task_2 import *

print("\n\tTask 3\n")
alphabetB = "abcdefghijklemnop"
print("Message", alphabetB)

duration = 0

for i in range(1,17):
    duration += Entropy / i

print("Speed of translation thee messsage(1) = ", duration)

task3 = "aabbccddeeffgghhiijj"
print("Message: ", task3)

probability = 0.0625
Entropy1 = 0
for i in range(0,11):
    Entropy1 += probability * log2(probability)

Entropy1 = abs(Entropy1)

duration2 = 0
for i in range(1,17):
    duration2 += Entropy1 / i

print("Speed of translation(2) = ", duration2)






