import cv2 as c
cap = c.VideoCapture(0)
print(cap.get(c.CAP_PROP_FRAME_WIDTH))
print(cap.get(c.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1208)  # 3 is the number of that property,width
cap.set(4, 1208)
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = c.FONT_HERSHEY_SIMPLEX
        text = 'Width:' + str(cap.get(3)) + 'Height:' + str(cap.get(4))
        frame = c.putText(frame, text, (10, 15), font,
                          1, (0, 255, 255), 2, c.LINE_AA)
        c.imshow('frame', frame)

        if c.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
c.destroyAllWindows()
