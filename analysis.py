#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :analysis.py
# @Time      :2024/11/29 12:39
# @Author    :DaisyCraft
# @Email     :3188563957@qq.com


import cv2
from paddleocr import PaddleOCR
import numpy as np  # 确保导入了numpy

# 初始化PaddleOCR对象
ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True)  # 指定使用中文模型
def is_pure_number(s):
    return s.isdigit()

def recognize_image(image_path):
    # 使用OpenCV读取图片
    img = cv2.imread(image_path)
    if img is None:
        print("图片读取失败，请检查路径")
        return

    # 使用PaddleOCR进行文字识别
    result = ocr.ocr(img, cls=True)  # cls=True 表示使用方向分类器
    time = []
    step_n = []
    # 输出识别结果
    for _ in result:
        for line in _:
            # print('----------------------------')
            # print(line)
            if '晚上' in line[1][0]:
                part_before_evening = line[1][0].split('晚上')[0]
                # print(part_before_evening,line[0][0][0])
                # print(line[0])
                time.append(part_before_evening)
            elif is_pure_number(line[1][0]) and line[0][0][0]>500:
                # print(line[1][0],line[0][0][0])
                step_n.append(line[1][0])

    return time,step_n

# 替换为你的图片路径
image_path = 'daisy.jpg'
time , step_n = recognize_image(image_path)
print(time,step_n)
