# README

用于从视频中提取微信步数汇总

使用方法

```
python analysis_forV.py
```

运行这份代码会从视频中提取步数

![](E:\Data\Doc\2024.11日记\11.29\daisy.jpg)

视频要求见项目的视频示例

汇总结果输出到output.xlsx中，如左边列表所示，因为单位需要，我在示例文件中做了一些整理，你自己运行的时候没有这些

偶尔误识别，错误率大概是3%吧，有时候会检测不到，只要找到是哪天没检测到，其他的往上推就可以，以后有空，或者真的有人用再更新吧

get_frame是用于从视频中获取帧，我的翻页速度是一秒一翻，自动翻页的，你自己找个app用来翻页然后挂个录屏就可以了，获取帧用来给单位交证明

reshape是因为单位要求打印，放到word里看不清，最重要的就是上面说的analysis_forV.py，analysis.py用于对图片检测，其他的酌情使用吧

我自己是3060显卡，材料1.8G的跑了大概三个多小时，可以大概估算一下

希望能帮上你# Analysis_WechatSteps
# Analysis_WechatSteps
# Analysis_WechatSteps
# Analysis_WechatSteps
# Analysis_WechatSteps
