import csv

def readcsv():

    std_dit = []

    with open('data_std.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)


        for row in csv_reader:
            std_dit.append(row)

    return std_dit

