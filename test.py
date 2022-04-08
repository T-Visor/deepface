# For reference: https://pypi.org/project/deepface/
from PIL import Image
from numpy import asarray
from deepface import DeepFace
from matplotlib import pyplot

backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]

first_image = 'angelina.jpg'
second_image = 'lowkey_image.jpg'

#df = DeepFace.find(img_path =
#        "../sample-face-recognition/5-celebrity-faces-dataset/val/elton_john/httpafilesbiographycomimageuploadcfillcssrgbdprgfacehqwMTEODAOTcxNjcMjczMjkzjpg.jpg",
#        db_path = "../sample-face-recognition/5-celebrity-faces-dataset/train",
#        detector_backend = backends[3])
#print(df.to_string())

result = DeepFace.verify(img1_path=first_image, img2_path=second_image, detector_backend=backends[3])
print(result)

img = Image.open(first_image) 
img2 = Image.open(second_image) 

i = 1
for image in [img, img2]:
    pyplot.suptitle('Images provided', fontsize=20)
    pyplot.subplot(1, 2, i) # 1-row, 2 columns
    pyplot.axis('off')
    pyplot.imshow(image)
    i += 1
pyplot.show()
