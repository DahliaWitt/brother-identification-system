# Import brothers from another file
from brothers import BROTHERS, BROTHERS_NAMES
import face_recognition
import cv2

known_face_encodings = []
face_names = BROTHERS_NAMES

# Load images and encodings
for bro in BROTHERS:
    face_image = face_recognition.load_image_file('brothers/images/' + bro)
    known_face_encodings.append(face_recognition.face_encodings(face_image)[0])

# Setup OpenCV Stuff

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Uncomment this and change below frame to small_frame for further optimization
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(
            face_locations, face_encodings):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        # Uncomment the below if you uncomment the small_frame above
        '''top *= 4
        right *= 4
        bottom *= 4
        left *= 4'''

        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings,
                                                 face_encoding)

        name = "Person"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = face_names[first_match_index]
            
        cropped = frame[top - 50:bottom + 50, left - 50:right + 50]
       
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255),
                      cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0,
                    (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

