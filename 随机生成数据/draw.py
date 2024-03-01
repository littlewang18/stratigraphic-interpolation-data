import matplotlib.pyplot as plt
import random
import csv



if __name__ == '__main__':
    fp = open('randdata.txt', 'r')
    colors = ['ro', 'bo']
    plt.figure()
    with open("data_1.csv", "w", newline="") as datacsv:
        csvwriter = csv.writer(datacsv, dialect=("excel"))
        for line in fp:
            a = line.strip('\n').split()
            xi = float(a[0])
            yi = float(a[1])
            plt.plot(xi, yi, colors[0])
    fp.close()
    plt.savefig('data.png')
