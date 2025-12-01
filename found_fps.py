import cv2
import time

url = "rtsp//.."   # my camera rtsp stream url 
cap = cv2.VideoCapture(url)   

fps = 0
frame_count = 0
start_time = time.time()

cv2.namedWindow("Live Stream", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Live Stream", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    elapsed_time = time.time() - start_time

    # Update fps every second
    if elapsed_time > 1:
        fps = frame_count / elapsed_time
        frame_count = 0
        start_time = time.time()

    # Display fps on video
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Live Stream", frame)

    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()
