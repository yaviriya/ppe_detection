# PPE Object Detection

โปรเจคตรวจจับอุปกรณ์ป้องกันส่วนบุคคล (PPE) ด้วย YOLOv8 บนวิดีโอ

## โครงสร้างโปรเจค

```
ppe_obj_detection/
├── yolo8.py              # สคริปต์หลักสำหรับตรวจจับวัตถุในวิดีโอ
├── model/
│   └── best_22032026.pt  # โมเดล YOLOv8 ที่ train แล้ว
└── video/                # วิดีโอสำหรับทดสอบ (kyt1-8.mp4, new1-3.mp4 ฯลฯ)
```

## การใช้งาน

```python
detect_objects_video('kyt2.mp4', confidences=0.25, device='cuda')
```

- `video_name` — ชื่อไฟล์วิดีโอใน `./video/`
- `confidences` — ค่า confidence threshold (default: 0.5)
- `device` — `'cuda'` สำหรับ GPU, `'cpu'` สำหรับ CPU

## คลาสที่ตรวจจับได้

| คลาส | สีกรอบ | ความหมาย |
|------|--------|----------|
| `Hardhat` | เขียว | สวมหมวกนิรภัย |
| `NO-Hardhat` | แดง | ไม่สวมหมวกนิรภัย |

## Dependencies

- `ultralytics` — YOLOv8
- `opencv-python` — อ่านและแสดงวิดีโอ

## การรัน Python

- ถ้าในโฟลเดอร์โปรเจคมีโฟลเดอร์ `venv` ให้รัน Python ผ่าน venv ทุกครั้ง: `venv/Scripts/python script.py`
- ถ้าต้องการติดตั้ง Library เพิ่ม ให้ติดตั้งภายใน venv ทุกครั้ง: `venv/Scripts/pip install <package>`

## บุคลิกของผู้ช่วย

ผู้ช่วย AI ในโปรเจคนี้มีนิสัยร่าเริง เป็นกันเอง และสุภาพ พูดคุยด้วยความเป็นมิตร ใช้ภาษาที่เข้าใจง่าย และพร้อมช่วยเหลือเสมอด้วยความยินดี

## ผู้พัฒนา

ยะ
