from ultralytics import YOLO
import torch, os

def main():
    os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"
    torch.cuda.empty_cache()
    model = YOLO("yolo11m.pt")
    model.train(data="data.yaml", imgsz=416, batch=2, epochs=75, workers=2, device=0)

if __name__ == '__main__':
    main()


