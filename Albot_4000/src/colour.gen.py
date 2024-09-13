import cv2 as cv
import os
import numba

@numba.jit(nopython=True)
def main(path):
    img = cv.imread("/home/slindau/Downloads/blue.png")
    b, g, r = cv.split(img)

    for index, value in enumerate(b):
        r[index] = 0
        g[index] = 0
        b[index] = value
    
    final = cv.merge([b, g, r])
    cv.imwrite(f"/home/slindau/Downloads/{path}.png", final)
        


if __name__ == '__main__':
    path = input('save name: ')
    main(path)