import cv2
import time
import datetime

import telegram

bot = telegram.Bot(token='6110698173:AAF4lnl-ZcRQ5pKvlzGPIMJoYmxaAmgg0dY')

#bot.send_message(chat_id="-1001826468115", text='Hello, World!')

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 10
cap = cv2.VideoCapture(0)

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")



while True:
    _, frame = cap.read()
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-----%H-%M-%S")
            out = cv2.VideoWriter(
                f"{'/home/nano/iot_pro/cctv_videos/'+current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
            dataTele = " person dectected in " + current_time
            cv2.imwrite('/home/nano/iot_pro/cctv_vid/'+dataTele+".png", frame)

            bot.send_message(chat_id="-1001826468115", text=dataTele)
            bot.send_photo(chat_id = "-1001826468115" , photo=open('/home/nano/iot_pro/cctv_vid/'+dataTele+'.png', 'rb'))

    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print('Stop Recording!')

        else:
            timer_started = True
            detection_stopped_time = time.time()

    if detection:
        out.write(frame)

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
    for (x, y, width, height) in bodies:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
    
    

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):

        break

out.release()

cap.release()
cv2.destroyAllWindows()