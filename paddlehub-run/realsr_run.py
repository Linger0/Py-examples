import paddlehub as hub
import cv2

model = hub.Module(name='realsr')
r = model.predict("./output/zzy_wings.png")
# cv2.imwrite('output/girl.jpg', r)