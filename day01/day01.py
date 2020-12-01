import math

def find(expenses):
    for expense in expenses:
        for expense2 in expenses:
            sum = expense + expense2
            if sum == 2020:
                return expense * expense2

def find2(expenses):
    for expense in expenses:
        for expense2 in expenses:
            for expense3 in expenses:
                sum = expense + expense2 + expense3
                if sum == 2020:
                    return expense * expense2 * expense3

expenses = []
with open('input.txt') as file:
    for expense in file.readlines():
        expenses.append(int(expense.strip()))

print(str(find(expenses)))
print(str(find2(expenses)))
