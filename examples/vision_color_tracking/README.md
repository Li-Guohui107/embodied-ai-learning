# OpenCV 颜色检测

安装：

```bash
pip install -r requirements-vision.txt
```

运行：

```bash
python examples/vision_color_tracking/color_tracker.py --camera 0
```

默认检测一段绿色 HSV 范围。不同摄像头、光照和物体颜色可能需要调整阈值。按 `q` 退出。输出为像素坐标，不是三维机器人坐标。
