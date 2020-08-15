import cv2 as c
cap = c.VideoCapture(0)
print(cap.get(c.CAP_PROP_FRAME_WIDTH))
print(cap.get(c.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1208)  # 3 is the number of that property,width
cap.set(4, 1208)
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = c.cvtColor(frame, c.COLOR_BGR2GRAY)
        c.imshow('frame', gray)

        if c.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
c.destroyAllWindows()
