# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :reshape.py
# @Time      :2024/12/2 00:06
# @Author    :DaisyCraft
# @Email     :3188563957@qq.com


import cv2
import os

input_folder = 'output_frames'
output_folder = 'output_frames_reshape'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# 遍历
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # 检查文件扩展名
        # 读取图片
        img = cv2.imread(os.path.join(input_folder, filename))
        if img is not None:

            new_width = img.shape[1] // 5
            new_height = img.shape[0] // 5

            resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

            output_filename = os.path.join(output_folder, filename)
            # 保存缩放后的图片
            cv2.imwrite(output_filename, resized_img)
            print(f'Resized image saved: {output_filename}')
        else:
            print(f'Failed to read image: {filename}')
