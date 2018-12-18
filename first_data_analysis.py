# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 13:27:56 2018

@author: Jacek
"""
import matplotlib.pyplot as plt


def system_conversion(number, system):
    if number < 0:
        symbol = -1
    else:
        symbol = 1
    number = symbol*number
    converted_number = 0
    for i in range(len(str(number))):
        converted_number += number % 10 * system**i
        number = number//10
    return converted_number*symbol


data = []
times = []
temperatures = []
files = [["binary_data.txt", 2], ["quad_data.txt", 4], ["octal_data.txt", 8]]


def load_data(file_name, system):
    source_file = open(file_name, 'r')
    
    while True:
        current_line = source_file.readline()
        if current_line == '':
            break
        data.append(current_line)
    source_file.close()
        
    for i in range(len(data)):
        current_record = data[i].split(" ")
        times.append(current_record[0])
        temperatures.append(current_record[1])
        
        times[i] = system_conversion(int(times[i]), system)
        temperatures[i] = system_conversion(int(temperatures[i]), system)


for file in files:
    load_data(file[0], file[1])
    plt.figure(dpi=300)
    plt.plot(times, temperatures)
    plt.title(file[0][:-4])
    plt.tight_layout()
    plt.savefig(file[0][:-4]+".png")

    if temperatures[0:364] == temperatures[365:729] and temperatures[365:729] == temperatures[730:1094]:
        print("Plik w systemie "+str(file[1])+"-owym zawiera trzykrotnie te same dane temperaturowe")

    data.clear()
    times.clear()
    temperatures.clear()
    plt.close()

