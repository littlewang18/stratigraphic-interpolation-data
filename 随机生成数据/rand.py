import matplotlib.pyplot as plt
import random
import csv

FinalResult = []
dict = {'RandomValue': FinalResult}

if __name__ == '__main__':
    fp = open('randdata.txt', 'r')
    colors = ['ro', 'bo']
    plt.figure()
    with open("data_1.csv", "w", newline="") as datacsv:
        csvwriter = csv.writer(datacsv, dialect=("excel"))
        for line in fp:
            n = 100
            a = line.strip('\n').split()
            xi = float(a[0])
            yi = float(a[1])
            plt.plot(xi, yi, colors[0])
            while n > 1:
                xi = xi +  random.randint(-100, 100) + random.random() * 0.5
                yi = yi +  random.randint(-100, 100) + random.random() * 0.5
                csvwriter.writerow([xi, yi])
                plt.plot(xi, yi, colors[1])
                n = n - 1
    fp.close()
    plt.savefig('randdata.png')
