# YOLOv11 Ortam Kurulumu ve Kullanımı

Bu proje, YOLOv11 (You Only Look Once) algoritmasını kullanarak nesne tespiti yapmanızı sağlar. Aşağıdaki adımları takip ederek ortamı kurabilir ve modeli çalıştırabilirsiniz.

## Gereksinimler

- Python 3.11+
- pip
- Anaconda
- PyTorch
- Ultralytics
- CUDA Destekli bir GPU

## Ortam Kurulumu

1. **Proje repository'sini klonlayın**

```bash
git clone https://github.com/ahmetraufoktay/yolo-stop-sign-training
cd yolo-stop-sign-training
```

2. **Conda ortamını oluşturun ve etkinleştirin**

```bash
conda create -n yolov11_custom python=3.11 -y
conda activate yolov11_custom
```

3. **Ultralytics'i ve CUDA Destekli PyTorch'u yükleyin**

**_ULTRALYTICS_**:

```bash
pip install ultralytics
```


**_PYTORCH_**:

* Windows Kullanıyorsanız

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
```

* Linux Kullanıyorsanız:

```bash
pip3 install torch torchvision torchaudio
```

4. **Test Etmek İstediğiniz Resimleri \test\ klasörüne atın**

5. **Predict.py'yi çalıştırın**

```bash
python predict.py
```

## Test Sonuçları

Test sonuçları için runs/detect/predict dosyasının içeriğine bakabilirsiniz.