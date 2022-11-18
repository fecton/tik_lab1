"""
File: task_1.py
Theory of information and coding
Laboratory word #3

Task 1:
Визначити кількість інформації на символ повідомлення, що складається з цього алфавіту:

а) якщо символ алфавіту зустрічаються з рівними ймовірностями;

б) якщо ймовірність появи символів відповідають підпорядкованому
наступному закону
p(i) = (1/2)**i, sum(p(i)) = 1
"""

from math import log2

def unique(s: str) -> str:
    """
    Gets unique values from a string and returns it
    @param s - string
    @return string of unique elements
    """
    a = ""
    for i in s:
        if i not in a:
            a += i
    return a


print("\n\tTask 1\n")

symbols = "abcdefghijklmnop0123456789"
task_1_message = symbols*3
print("Message: ", task_1_message)


InfoAmount_A = log2(len(symbols))
print("Information amount(a): ", InfoAmount_A)

task_2_message = "kkkkkkkkkkkkkkkk33333333cccc00fa"
print("Message: ", task_2_message)

InfoAmount_B = 0.

for symbol in unique(task_2_message):
    k = task_2_message.count(symbol) / len(task_2_message)
    InfoAmount_B += k * log2(k)
InfoAmount_B = abs(InfoAmount_B)

print("Information amount(b): ", InfoAmount_B)


