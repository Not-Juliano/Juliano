import cv2
import numpy as np
import face_recognition

# creating a encoding that can be compared
Known_Person = face_recognition.load_image_file(
    r'C:\Users\Me\Desktop\Known_Faces\Taylor_Swift\Taylor_Swift1.jpg')
Known_Encode = face_recognition.face_encodings(Known_Person)[0]


# Creating a comparison encoding. We can call the comparison an unknown
Unknown_Person = face_recognition.load_image_file(
    r'C:\Users\Me\Desktop\Known_Faces\Taylor_Swift\Taylor_Swift2.jpg')
Unknown_Encoding = face_recognition.face_encodings(Unknown_Person)[0]


results = face_recognition.compare_faces(
    [Known_Encode], Unknown_Encoding)

# Working on a way to show pictures in comparison with results
width = 250
height = 200
dimensions = (width, height)

image = Known_Person
image = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)


image2 = Unknown_Person
image2 = cv2.resize(image2, dimensions, interpolation=cv2.INTER_AREA)


if results[0] == True:
    print("These are the same person, press any key to exit")
# Concatenate images next to each other in one window
    numpy_horizontal_concat = np.concatenate((image, image2), axis=1)
    cv2.imshow('The same Person!', numpy_horizontal_concat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("These are not the same person, press any key to exit")
    numpy_horizontal_concat = np.concatenate((image, image2), axis=1)
    cv2.imshow('Not the same person!', numpy_horizontal_concat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
