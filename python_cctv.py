import cv2
import time
import datetime

#import telegram
# current_time = datetime.datetime.now().strftime("%d-%m-%Y")
# print(current_time)

#bot = telegram.Bot(token='6110698173:AAF4lnl-ZcRQ5pKvlzGPIMJoYmxaAmgg0dY')

#bot.send_message(chat_id="-1001826468115", text='Hello, World!')
font=cv2.FONT_HERSHEY_SIMPLEX
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")



def send_document(update, context):
    chat_id = "-1001826468115"
    document = open('cctv_system.txt', 'rb')
    context.bot.send_document(chat_id, document)

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 10
cap = cv2.VideoCapture(0)

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")



while True:
    _, frame = cap.read()
    frame1 = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

    if len(faces) > 0 or len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-----%H-%M-%S")
            out = cv2.VideoWriter("E:\\Projcets\\python_3IA\\cctv_videos\\"+current_time+".mp4", fourcc, 24, frame_size)
            print("Started Recording!")
            dataTele = " person dectected in " + current_time
            current_time1 = datetime.datetime.now().strftime("%d-%m-%Y")

            file1 = open(current_time1+'cctv_system'+'.txt', 'a')
            file1.writelines(dataTele+'/n')

            cv2.imwrite('/home/nano/python_3IA/cctv_vid/'+dataTele+".png", frame)

            #bot.send_message(chat_id="-1001826468115", text=dataTele)
            #bot.send_photo(chat_id = "-1001826468115" , photo=open('/home/nano/python_3IA/cctv_vid/'+dataTele+'.png', 'rb'))

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
        cv2.putText(frame,'Recording',(width,height-6),font,.75,(0,0,255),2) 
    for (x, y, width, height) in bodies:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
    
    

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):

        break

out.release()

file1.close()

cap.release()
cv2.destroyAllWindows()