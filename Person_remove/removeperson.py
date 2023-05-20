import cv2

def extract_frames(video_path, output_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    frame_count = 0
    success = True

    # Retrieve the video's frame rate
    frame_interval = int(video.get(cv2.CAP_PROP_FPS))

    # Calculate the frame interval based on the video's fps



    while success:
        # Read the next frame from the video
        success, frame = video.read()

        # Check if the frame was read successfully
        if success:
            # Save the frame at the calculated interval
            if frame_count % frame_interval == 0:
                frame_filename = f"{output_path}/frame_{frame_count//frame_interval}.jpg"
                cv2.imwrite(frame_filename, frame)

            frame_count += 1

    # Release the video file
    video.release()

# Specify the input video path and output directory
video_path = 'example.mp4'
output_directory = 'Person_remove/frames_output'

# Call the function to extract frames
extract_frames(video_path, output_directory)
