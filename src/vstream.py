import numpy as np
import cv2


class VideoStream:
    def __init__(self,path,**kwargs):
        self.cap = cv2.VideoCapture(path)
        self.f = [lambda x:x]
        self.names = ['none']
        for k,v in kwargs.items():
            self.names.append(k)
            self.f.append(v)
    def apply(self):
        while(True):
            try:
                # Capture frame-by-frame
                ret, frame = self.cap.read()

                # Our operations on the frame come here
                #img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
                for f in self.f:
                    frame = f(frame)
                                    
                # Display the resulting frame
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except:
                break

        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()
