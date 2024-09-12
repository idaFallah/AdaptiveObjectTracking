import cv2

#tracker = cv2.TrackerKCF_create()
tracker = cv2.TrackerCSRT_create()

video = cv2.VideoCapture('race.mp4')

ok, frame = video.read()

bbox = cv2.selectROI(frame)     # to choose the object we wanna track & see the results
#print(bbox)

ok = tracker.init(frame, bbox)
#print(ok)

while True:      # loop to go thru the whole frames in the video
    ok, frame = video.read()
    #print(ok)  # to print false when the last frame is processed
    if not ok:
        break
    ok, bbox = tracker.update(frame)
    #print(bbox)
    #print(ok)   # tp print true while going thru frames

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]   # to save the info of the binding box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2, 1)

    else:
        cv2.putText(frame, 'Error', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: #ESC key, when u press it, it closes the window
        break