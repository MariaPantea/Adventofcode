import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

with open('puzzle_input/day8.txt') as f:
    data = f.readline()


def part_1():
    layers = np.array([int(x) for x in data]).reshape((100, 150))

    min_zeros = np.inf
    layer_id = 0
    for i, layer in enumerate(layers):
        zeros = len(np.where(layer == 0)[0])
        if zeros < min_zeros:
            min_zeros = zeros
            layer_id = i

    layer = layers[layer_id]
    twos = len(np.where(layer == 2)[0])
    ones = len(np.where(layer == 1)[0])
    print(twos * ones)


def part_2():
    layers = np.array([int(x) for x in data]).reshape((100, 150))
    image = np.zeros([150])

    for pixel in range(150):
        for layer in layers:
            if layer[pixel] != 2:
                image[pixel] = int(layer[pixel])
                break

    image = image.reshape(6, 25)
    fig, ax = plt.subplots()
    ax.matshow(image, cmap=plt.cm.Blues)
    plt.show()


part_1()
part_2()
