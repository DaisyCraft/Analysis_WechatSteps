#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :get_frame.py
# @Time      :2024/12/1 23:43
# @Author    :DaisyCraft
# @Email     :3188563957@qq.com


import cv2
import time
import os

# 视频文件路径
video_path = 'daisyFULL.mp4'
output_folder = 'output_frames'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_rate = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
frame_interval = int(2 * frame_rate)  # 计算每隔两秒的帧数

frame_count = 0
extracted_count = 0

while True:
    ret, frame = cap.read()  # 读取一帧
    if not ret:
        break  # 如果没有帧了，退出循环

    frame_count += 1

    if frame_count % frame_interval == 0:
        output_filename = os.path.join(output_folder, f'frame_{extracted_count:04d}.jpg')
        cv2.imwrite(output_filename, frame)
        print(f'Extracted frame {extracted_count} : {output_filename}')
        extracted_count += 1
    time.sleep(1 / frame_rate)

cap.release()
print('Finished extracting frames.')
