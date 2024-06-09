import matplotlib.pyplot as plt
import numpy as np

def DrawHistogram(Points):
    plt.figure(dpi=300, figsize = (6.73, 2.33))
    plt.hist(Points, bins = 200)
    plt.xlabel('Кадр')
    plt.ylabel('Количество моментов, когда кадр горел')
    plt.title('Время горения пикселей на видео')
    plt.show()

def DrawGraph(Points, NameVideo):
    x = np.arange(0, len(Points)/120, 1/120)
    y = Points
    plt.figure(dpi=300, figsize = (6.73, 2.33))
    plt.plot(x, y, 'g', label= "Кол-во областей в определённое время",linewidth = 2)
    plt.xlabel('Время, мин')
    plt.ylabel('Количество областей, пиксель')
    plt.title('Количество областей с течением времени в кадре')
    plt.xlim(0,2.5)
    plt.xticks(range(0,3))
    plt.ylim(min(Points), max(Points))
    plt.legend()
    plt.savefig('Зависимость количества областей от времени на видео ' + NameVideo + '.png')
    plt.savefig('Зависимость количества областей от времени на видео ' + NameVideo + '.svg', format = 'svg')
    plt.show()