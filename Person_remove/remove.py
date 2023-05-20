import cv2
from pytube import YouTube

# Get the YouTube video URL from the user
video_url = input("Enter the YouTube video URL: ")

# Download the YouTube video
yt = YouTube(video_url)
video_path = yt.streams.filter(file_extension='mp4').first().download()

# Open the video file
cap = cv2.VideoCapture(video_path)

# Initialize frame count
frame_count = 0

# Read the first frame
ret, frame = cap.read()

# Loop through the video frames
while ret:
    # Save the frame as an image
    frame_path = "C:\\Users\\lcman\\OneDrive - 한양대학교\\바탕 화면\\개발\\강의요약(HX-CES_2023)\\Person_remove\\test\\frame{}.jpg".format(frame_count)
    cv2.imwrite(frame_path, frame)

    # Increment the frame count
    frame_count += 1

    # Read the next frame
    ret, frame = cap.read()

# Release the video capture object
cap.release()
