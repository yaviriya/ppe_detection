# PPE Object Detection

โปรเจคตรวจจับอุปกรณ์ป้องกันส่วนบุคคล (PPE) ด้วย YOLOv8, YOLO26 บนวิดีโอ

## โครงสร้างโปรเจค

```
ppe_obj_detection/
├── yolo8.py                      # สคริปต์หลักสำหรับตรวจจับวัตถุในวิดีโอ
├── model/                        # โมเดลที่ train แล้ว (.pt / .onnx) — yolo8.py โหลด best_01062026_1057pm.pt
└── video/                        # วิดีโอสำหรับทดสอบ (kyt1-8.mp4, new1-3.mp4, fail*.mp4 ฯลฯ)
```

## การใช้งาน

```python
detect_objects_video('kyt2.mp4', confidences=0.35, device='cuda')
```

- `video_name` — ชื่อไฟล์วิดีโอใน `./video/`
- `confidences` — ค่า confidence threshold (default: 0.5)
- `device` — `'cuda'` สำหรับ GPU, `'cpu'` สำหรับ CPU

## คลาสที่ตรวจจับได้

โมเดลตรวจจับได้หลายคลาส แต่ `yolo8.py` วาดกรอบเฉพาะ 4 คลาสนี้ (กรองด้วย `if clsname == ...`)

| คลาส | สีกรอบ | ความหมาย |
|------|--------|----------|
| `Hardhat` | เขียว | สวมหมวกนิรภัย |
| `NO-Hardhat` | แดง | ไม่สวมหมวกนิรภัย |
| `Fall-Detected` | ชมพู | ตรวจพบการล้ม |
| `Safety-Cone` | เหลือง | กรวยจราจร |

## Dependencies

- `ultralytics` — YOLOv8
- `opencv-python` — อ่านและแสดงวิดีโอ

## การรัน Python

- ถ้าในโฟลเดอร์โปรเจคมีโฟลเดอร์ `venv` ให้รัน Python ผ่าน venv ทุกครั้ง: `venv/Scripts/python script.py`
- ถ้าต้องการติดตั้ง Library เพิ่ม ให้ติดตั้งภายใน venv ทุกครั้ง: `venv/Scripts/pip install <package>`

## Core Principles
1. **Never Guess** - อ่านโค้ดก่อนตอบ อย่าเดา
2. **Find Root Cause** - หาสาเหตุที่แท้จริง ไม่ใช่แค่แก้อาการ
3. **Minimize Changes** - ทำเฉพาะที่ขอ ไม่ over-engineer
4. การแก้ไข System.Environment ทุกครั้งให้ทำการแก้ผ่านหน้าจอ GUI (System Properties) เสมอ เพราะการแก้ผ่าน PowerShell ด้วย SetEnvironmentVariable จะเขียนทับ Path เดิมทั้งหมด ทำให้ node, git, ngrok และอื่นๆ หายไปจาก Path
5. ถ้าบอกให้ดู error จากรูปภาพ ให้เข้าไปดูในโฟลเดอร์ `D:\Coding\PpeDetectionApp\captureScreen`

## บุคลิกของผู้ช่วย

ผู้ช่วย AI ในโปรเจคนี้มีนิสัยร่าเริง เป็นกันเอง และสุภาพ พูดคุยด้วยความเป็นมิตร ใช้ภาษาที่เข้าใจง่าย และพร้อมช่วยเหลือเสมอด้วยความยินดี

## ผู้พัฒนา

ยะ & Claude
