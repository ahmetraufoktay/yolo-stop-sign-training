from ultralytics import YOLO

model = YOLO("yolov11_stop_detection.pt")
results = model.predict(source= "./test", show=True, save=True, conf=0.55)