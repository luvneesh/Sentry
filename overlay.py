import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
#
# def overlay_image_alpha(img, img_overlay, pos, alpha_mask):
#     """Overlay img_overlay on top of img at the position specified by
#     pos and blend using alpha_mask.
#
#     Alpha mask must contain values within the range [0, 1] and be the
#     same size as img_overlay.
#     """
#
#     x, y = pos
#
#     # Image ranges
#     y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
#     x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])
#
#     # Overlay ranges
#     y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
#     x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)
#
#     # Exit if nothing to do
#     if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
#         return
#
#     channels = img.shape[2]
#
#     alpha = alpha_mask[y1o:y2o, x1o:x2o]
#     # alpha = 1.0 - alpha
#     alpha_inv = 1.0 - alpha
#
#     for c in range(channels):
#         img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] +
#                                 alpha_inv * img[y1:y2, x1:x2, c])
#
#
# blank_image = np.zeros((1090,1180,3), np.uint8)
# # blank_image = cv2.cvtColor(blank_image, cv2.COLOR_RGB2RGBA).copy()
#
# test = cv2.imread("images/test.png", cv2.IMREAD_COLOR)
# test = cv2.cvtColor(test, cv2.COLOR_RGB2RGBA).copy()
# test1 = cv2.imread("images/test1.png", cv2.IMREAD_COLOR)
# test1 = cv2.cvtColor(test1, cv2.COLOR_RGB2RGBA).copy()
#
# print(test[:, :, 3])
# cv2.imshow("LOL", blank_image)
# overlay_image_alpha(blank_image, test[:, :, 0:3], (0, 0), test[:, :, 3] / 255.0)
# cv2.waitKey(0)

def put4ChannelImageOn4ChannelImage(back, fore, x, y):
    rows, cols, channels = fore.shape
    trans_indices = fore[...,3] != 0 # Where not transparent
    overlay_copy = back[y:y+rows, x:x+cols]
    overlay_copy[trans_indices] = fore[trans_indices]
    back[y:y+rows, x:x+cols] = overlay_copy

#test
background = np.zeros((1130, 1120, 4), np.uint8)
background[:] = (127, 127, 127, 1)
overlay = cv2.imread('images/test1.png', cv2.IMREAD_UNCHANGED)
overlay = cv2.cvtColor(overlay, cv2.COLOR_RGB2RGBA).copy()
put4ChannelImageOn4ChannelImage(background, overlay, 8, 8)

overlay = cv2.imread('images/test.png', cv2.IMREAD_UNCHANGED)
overlay = cv2.cvtColor(overlay, cv2.COLOR_RGB2RGBA).copy()
put4ChannelImageOn4ChannelImage(background, overlay, 150, 220)

background = cv2.resize(background, (1200, 750))

cv2.imshow("back", background)
cv2.imwrite("images/fuc.jpg", background)
cv2.waitKey(0)