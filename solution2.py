import matplotlib.pyplot as plt
import numpy as np
from math import exp,pow, pi

def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1
    return


def get_kernel(windos_size,sigma):
    kernel = np.ones((windos_size, windos_size))
    for i in range(windos_size):
        for j in range(windos_size):
            d = (i-windos_size//2)*(i-windos_size//2) + (j-windos_size//2)*(j-windos_size/2)
            kernel[i,j]= exp(-(d)/(2*sigma*sigma))/(sigma*pow(2*pi,1/2))

    kernel/=kernel.sum()

    print(kernel.shape)
    return kernel


def filter(img,sigma, window_size=3):
    window_size = 3*sigma
    img2 = np.zeros_like(img)
    kernel = get_kernel(window_size,sigma)
    p = window_size//2
    for k in range(img.shape[2]): # foreach color channel
        for i in range(p, img.shape[0]-p): # foreach row
            for j in range(p, img.shape[1]-p): # foreach column
                window = img[i-p:i+p, j-p:j+p, k]
                #window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i,j,k] = (kernel*window).sum()
    return img2


def main():
    sigma= 5
    img = plt.imread("img.png")[:, :, :3]
    add_noise(img)
    img2 = filter(img,sigma)

    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()