import cv2

print("Welcome to face detection program!\n1. Use camera\n2. Use video\n3. Exit")
choice = int(input())
if choice == 1:
    # Video capturing device
    cap = cv2.VideoCapture(0)
elif choice == 2:
    print("Enter file name.extension (mp4 recommended): ")
    file_name = str(input())
    # Loading from video
    cap = cv2.VideoCapture(file_name)
else:
    # end program
    exit()

# Loading cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


while True:
    ret, frame = cap.read()

    # Converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Applying face detection to gray frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:

        # Drawing blue rectangle for each face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

        # Setting face region for eye detection
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    # Frame display
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()