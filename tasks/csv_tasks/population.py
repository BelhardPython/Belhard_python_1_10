"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""

import csv

change_perc = []
years = []


def max_delta():

    with open('world_population.csv', 'r') as file:
        reader = csv.reader(file)
        next(file)
        for row in reader:
            change_perc.append(float(row[2]))
            years.append(int(row[0]))
        max_change = max(change_perc)  # находим максимальный прирост населения
        for i in range(len(change_perc)):
            if change_perc[i] == max_change:
                print(years[i])  # выводим годы с максимальным приростом населения


max_delta()
