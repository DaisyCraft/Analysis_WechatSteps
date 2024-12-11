import cv2
import os
import numpy as np

input_folder = 'output_frames'

output_folder = 'output_frames_reshape2'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):

        img = cv2.imread(os.path.join(input_folder, filename))
        if img is not None:
            # ROI设置为屏幕最下面的部分
            new_height = int(img.shape[0] / 5)
            new_width = int(img.shape[1] / 3)
            resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
            # 提高亮度
            resized_img_float = resized_img.astype(np.float32)
            brightened_img = cv2.multiply(resized_img_float, 2.0)
            brightened_img = np.clip(brightened_img, 0, 255).astype(np.uint8)
            output_filename = os.path.join(output_folder, filename)
            cv2.imwrite(output_filename, brightened_img)
            print(f'Resized and brightened image saved: {output_filename}')
        else:
            print(f'Failed to read image: {filename}')
