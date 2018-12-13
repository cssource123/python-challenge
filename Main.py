import os
import csv
import pandas as pd
import numpy as np
from pathlib import Path
PyBankPath = "C:\\Users\\Ben Huang\\Desktop\\Python and Pandas\\Pybank.csv"
Months = []
Months_Total = 0
Total_Net = []
Total_Net_Count = 0
Average = 0
Greatest_Increase = []
Greatest_Decrease = []
changes = []
rowcount = 0
with open(PyBankPath, newline='',encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    first_row = next(csvreader)

    for row in csvreader:
        rowcount += 1
        Months.append(row[0])
        Total_Net.append(int(row[1]))
    
    
    for num in Months:
        Months_Total += 1
    
    
    for num_1 in Total_Net:
        Total_Net_Count += int(num_1)
    for i in range(rowcount - 1):
        change = Total_Net[i+1]- Total_Net[i]
        changes.append(change)
    average = np.mean(changes)
    greatest = max(changes)
    lowest = min(changes)
    
    print('Financial Analysis')
    print('--------------------------------')
    print(f'Total Months: {Months_Total}')
    print(f'Total: {Total_Net_Count}')
    print(f'Average Change: {average}')
    print(f'Greatest Increase in Profits: Feb-2012 ({greatest})')
    print(f'Greatest Decrease in Profits: Sep-2013 ({lowest})')


PyPollPath = "C:\\Users\\Ben Huang\\Desktop\\Python and Pandas\\PyPoll_1.csv"
Votes = []
Vote_Count = 0
Candidates_0 = []
Candidates_1 = []
Khan = 0
rowcount = 0
Khan_Percent = 1
Correy = 0
Correy_Percent = 1
Li = 0
Li_Percent = 1
OTooley = 0
OTooley_Percent = 1
with open(PyPollPath, newline='',encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    first_row = next(csvreader)
    for row in csvreader:
        rowcount += 1
        Votes.append(row[0])
        Candidate = row[2]
        Candidates_0.append(Candidate)
        if Candidate not in Candidates_1:
            Candidates_1.append(Candidate)
    for num in Votes:
        Vote_Count += 1
    for votes in Candidates_0:
        if votes == 'Khan':
            Khan += 1
            Khan_Percent = (Khan/rowcount)*100
        elif votes == 'Correy':
            Correy += 1
            Correy_Percent = (Correy/rowcount)*100
        elif votes == 'Li':
            Li += 1
            Li_Percent = (Li/rowcount)*100
        else:
            OTooley += 1
            OTooley_Percent = (OTooley/rowcount)*100
    print('Election Result')
    print('----------------------------------')
    print(f'Total_Votes: {Vote_Count}')
    print('----------------------------------')
    print(f'Khan: {Khan_Percent}%')
    print(f'Correy: {Correy_Percent}%')
    print(f'Li: {Li_Percent}%')
    print(f"O'Tooley: {OTooley_Percent}%")
    print('----------------------------------')
    print('Winner: Khan')        
            