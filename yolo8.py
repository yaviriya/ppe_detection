from ultralytics import YOLO
import cv2
import os

def detect_objects_video(video_name, confidences=0.5, device='cuda'):

    paths = os.path.join('./video', video_name)  # กำหนด path ของวีดีโอที่จะตรวจจับวัตถุ
    cap = cv2.VideoCapture(paths)  # อ่านวิดีโอจากไฟล์ที่ส่งเข้ามา

    # Load YOLO model
    model = YOLO('./model/best_22032026.pt').to(device)  # โหลดโมเดลจากในเครื่อง
    # model.predict(classes=[0, 2])  # กำหนดคลาสที่ต้องการตรวจจับ เช่น [0, 1, 2] สำหรับบุคคลและรถยนต์

    # ตรวจสอบว่าการเปิดวิดีโอสำเร็จหรือไม่
    while cap.isOpened():
        success, frame = cap.read()  # อ่านเฟรมจากวิดีโอ
        if not success:
            print("Error reading video.")
            break  # ถ้าไม่สามารถอ่าน video ให้หยุดการทำงาน

        # ส่ง video ไปยังโมเดลเพื่อทำการตรวจจับวัตถุ
        results = model.predict(frame, conf=confidences)
        # แสดงผลลัพธ์การตรวจจับวัตถุ
        person_count = 0
        car_count = 0

        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()  # แปลงผลลัพธ์เป็น numpy array
            confidenses = result.boxes.conf.cpu().numpy()  # แปลง confidenses เป็น numpy array
            classes = result.boxes.cls.cpu().numpy()  # แปลง class เป็น numpy array 

            # วนลูปเพื่อวาดกรอบสี่เหลี่ยม และแสดงชื่อวัตถุที่ตรวจจับได้
            for box, confs, cls in zip(boxes, confidenses, classes):
                label = f"{model.names[int(cls)]}: {confs:.2f}"  # สร้าง label สำหรับวัตถุที่ตรวจจับได้
                clsname = model.names[int(cls)]  # ใช้สำหรับ if else by classed
                x1, y1, x2, y2 = map(int, box)  # แปลงค่าพิกัดของกล่องเป็นจำนวนเต็ม
                # print(clsname)

                if clsname == 'Hardhat':
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # วาดกรอบสี่เหลี่ยมรอบวัตถุที่ตรวจจับได้
                    cv2.putText(frame, f'{label}', (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2) # แสดงชื่อวัตถุที่ตรวจจับได้
                if clsname == 'NO-Hardhat':
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # วาดกรอบสี่เหลี่ยมรอบวัตถุที่ตรวจจับได้
                    cv2.putText(frame, f'{label}', (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2) # แสดงชื่อวัตถุที่ตรวจจับได้

        # แสดง video ที่มีการตรวจจับวัตถุ
        cv2.imshow("Video Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# เรียกใช้งานฟังก์ชันตรวจจับวัตถุ
detect_objects_video('kyt2.mp4', 0.25)