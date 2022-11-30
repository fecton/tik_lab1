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
from func import unique


print("\n\tTask 1\n")

# Символ зустрічаються з рівними ймовірностями
symbols = "abcdefghijklmnopqrstuvw"
task_1_message = symbols*4
print("Message: ", task_1_message)


InfoAmount_A = log2(len(symbols))
print("Information amount(a): ", InfoAmount_A)

# Ймовірність появи символів відповідають підпорядкованому
# наступного закону

task_2_message = "bbffchhhbbffffffbbjjjjjjjjjjaaaa"
print("Message: ", task_2_message)
InfoAmount_B = 0.
for symbol in unique(task_2_message):
    k = task_2_message.count(symbol) / len(task_2_message)
    InfoAmount_B += k * log2(k)
InfoAmount_B = abs(InfoAmount_B)

print("Information amount(b): ", InfoAmount_B)


