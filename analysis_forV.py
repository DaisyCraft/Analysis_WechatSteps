#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :analysis_forV.py
# @Time      :2024/11/29 13:46
# @Author    :DaisyCraft
# @Email     :3188563957@qq.com

import cv2
from paddleocr import PaddleOCR
import numpy as np
import openpyxl
import pandas as pd
import logging
import os

logging.disable(logging.DEBUG)
logging.disable(logging.WARNING)


ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True)  # 指定使用中文模型
global_time = []
global_step_n = []
step_n_count = {}  # 用于记录每个数字出现的次数
n = 1

def is_pure_number(s):
    return s.isdigit()

def recognize_image(img):
    global step_n_count
    global n
    # 使用PaddleOCR进行文字识别
    result = ocr.ocr(img, cls=True)  # cls=True 表示使用方向分类器
    time = []
    step_n = []
    # 检查result是否为None，防止出错
    if result is not None:
        # 输出识别结果
        for line in result:
            try:
                for info in line:
                    text = info[1][0]
                    if '晚上' in text:
                        part_before_evening = text.split('晚上')[0]
                        time.append(part_before_evening)
                    elif is_pure_number(text) and info[0][0][0] > 300 and info[1][1] > 0.95:
                        if text in step_n_count:
                            step_n_count[text] += 1
                        else:
                            step_n_count[text] = 1
                        if step_n_count[text] > 10:
                            step_n.append(text)
            except TypeError:
                cv2.imwrite(f"frame_{n}.jpg", img)  # 保存当前帧的图片
                n += 1
                return [], []
    return time, step_n

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("视频打开失败，请检查路径")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        height = frame.shape[0]
        # 计算最下面三分之一的起始行号
        top = height // 3 * 2
        bottom = int(height * 9 / 10)
        # 裁剪图像，只保留最下面三分之一
        bottom_third = frame[top:bottom, 0:frame.shape[1]]
        gray = cv2.cvtColor(bottom_third, cv2.COLOR_BGR2GRAY)

        time, step_n = recognize_image(gray)
        # 更新全局列表，如果结果已存在则不添加
        for t in time:
            if t not in global_time and '月' in t:
                global_time.append(t)
        for sn in step_n:
            if sn not in global_step_n:
                global_step_n.append(sn)

    cap.release()
    cv2.destroyAllWindows()
    return global_time, global_step_n

def save_to_excel(time_list, step_n_list, file_name):
    # 确保两个列表长度相同，用None填充较短的列表
    max_len = max(len(time_list), len(step_n_list))
    time_list.extend([''] * (max_len - len(time_list)))
    step_n_list.extend([''] * (max_len - len(step_n_list)))

    # 创建一个DataFrame
    df = pd.DataFrame({
        'Date': time_list,
        'Steps': step_n_list
    })
    # 将DataFrame写入Excel文件
    df.to_excel(file_name, index=False)

# 替换为你的视频路径
video_path = 'DaisyF.mp4'
time, step_n = process_video(video_path)

save_to_excel(time, step_n, 'output.xlsx')
print(time, step_n)