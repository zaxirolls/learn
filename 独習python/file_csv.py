import csv

with open('./member.tsv',encoding='UTF-8') as file:
    for row in csv.reader(file,delimiter='\t'):
        for cell in row :
            print(cell)
        print('------')