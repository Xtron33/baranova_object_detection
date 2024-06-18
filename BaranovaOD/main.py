from roboflow import Roboflow
from ultralytics import YOLO
import os
import cv2
import math
from flask import Flask, Response
import websocket

classNames = ["defect", "planson"]

model = YOLO('best.pt')


def video_detection():
    flag = True
    cap = cv2.VideoCapture(1)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    while True:
        success, img = cap.read()
        results = model(img, stream=True, verbose=False)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                clas = int(box.cls[0])
                class_name = classNames[clas]
                if class_name == classNames[0]:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
                    if flag == True:
                        ws.send('Defects found')
                        flag = False
                else:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (60, 130, 230), 3)
                conf = math.ceil((box.conf[0]*100))/100
                label = f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, [
                              255, 0, 255], -1, cv2.LINE_AA)  # filled
                cv2.putText(img, label, (x1, y1-2), 0, 1,
                            [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)
        yield img
    cv2.destroyAllWindows()


def generate_frames_web():
    yolo_output = video_detection()
    for detection_ in yolo_output:
        ref, buffer = cv2.imencode('.jpg', detection_)

        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


if __name__ == '__main__':
    HOME = os.getcwd()
    app = Flask(__name__)

    @app.route('/')
    def mainpage():
        return Response(generate_frames_web(), mimetype='multipart/x-mixed-replace; boundary=frame')

    ws = websocket.WebSocket()
    ws.connect("ws://localhost:8765/ws")
    app.run()

    # rf = Roboflow(api_key="ariZTxZU8HPGJdvtPqjs")
    # project = rf.workspace("baranova").project("baranovaod")
    # version = project.version(3)
    # dataset = version.download("yolov8")

    # result = model.train(
    #     data=f'{HOME}/datasets/BaranovaOD-3/data.yaml', epochs=1000, imgsz=1280)

    # preds = model.predict(source="2", show=True)
    # print(preds)
