import cv2
import numpy as np

"""
    vectors2d - (N,M) numpy array, with N vectors of size M
    img_paths - [N] list with N image paths corresponding to vectors
    image_width - size of image in manifold in px

"""
def make_manifold(vectors2d, img_paths, image_width=60):
    canvas_width = 6000
    canvas = np.zeros((canvas_width, canvas_width, 3), dtype=np.uint8)
    image_width = 60
    minx = vectors2d[:, 0].min()
    miny = vectors2d[:, 1].min()

    vectors2d[:, 0] -= minx
    vectors2d[:, 1] -= miny

    maxx = vectors2d[:, 0].max()
    maxy = vectors2d[:, 1].max()

    canvas_width = canvas.shape[1]
    for i, imgpath in enumerate(img_paths):
        imx = int((vectors2d[i, 0]/maxx * (canvas_width-image_width)) + image_width/2)
        imy = int((vectors2d[i, 1]/maxy * (canvas_width-image_width)) + image_width/2)
        scaled_image = cv2.resize(cv2.imread(imgpath), (image_width, image_width))
        canvas[imx - image_width/2:imx+image_width/2, imy-image_width/2:imy+image_width/2] = scaled_image
        if not i % 100:
            print('added %s images on canvas ' % i)

    cv2.imwrite('manifold.png', canvas)
