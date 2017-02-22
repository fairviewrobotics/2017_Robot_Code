# Import the camera server
from cscore import CameraServer

# Import OpenCV and NumPy
import cv2
import numpy as np
import robotmap
from networktables import NetworkTables

def getCentroid(contour):
  M = cv2.moments(contour)
  cx = int(M['m10']/M['m00'])
  cy = int(M['m01']/M['m00'])
  return cx,cy

def main():
    NetworkTables.initialize(server='localhost')
    nt = NetworkTables.getTable("camera")

    cs = CameraServer.getInstance()
    cs.enableLogging()

    # Capture from the first USB Camera on the system
    camera = cs.addAxisCamera(robotmap.network.camera)
    cs.startAutomaticCapture(camera=camera)
    camera.setResolution(320, 240)

    # Get a CvSink. This will capture images from the camera
    cvSink = cs.getVideo()

    # (optional) Setup a CvSource. This will send images back to the Dashboard
    #outputStream = cs.putVideo("Name", 320, 240)

    # Allocating new images is very expensive, always try to preallocate
    img = np.zeros(shape=(240, 320, 3), dtype=np.uint8)

    while True:
        # Tell the CvSink to grab a frame from the camera and put it
        # in the source image.  If there is an error notify the output.
        time, img = cvSink.grabFrame(img)
        if time == 0:
            # Send the output the error.
            outputStream.notifyError(cvSink.getError());
            # skip the rest of the current iteration
            continue

        frame = img
        height, width, channels = frame.shape

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cv2.line(frame,(width/2,0),(width/2,height),(0,0,255),1)

        thresh = cv2.inRange(gray,np.array([0,245,0]),np.array([179,255,255]))
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        biggest = sorted(contours, key=cv2.contourArea, reverse=True)[0:2]

        cv2.drawContours(frame, biggest, -1, (0,255,0), 3)

        centroids = []
        for contour in biggest:
          cx,cy = getCentroid(contour)
          centroids.append((cx,cy))
          cv2.putText(frame,str(cx)+","+str(cy)+":"+str(cv2.contourArea(contour)),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)

        cv2.line(frame, centroids[0], centroids[1],(0,255,0),2)

        mid_x = (centroids[0][0]+centroids[1][0])/2
        mid_y = (centroids[0][1]+centroids[1][1])/2

        cv2.circle(frame,(mid_x,mid_y),5,(255,0,0),-1)

        offset = (centroids[0][0]+centroids[1][0])/2-width/2

        nt.putNumber('offset',offset)


        # (optional) send some image back to the dashboard
        #outputStream.putFrame(img)
