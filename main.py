import cv2
from pytube import YouTube

def main():
    # YouTube video URL
    video_url = 'https://www.youtube.com/watch?v=wjoar7T-Ag4&list=RDwjoar7T-Ag4&start_radio=1'

    # Download the YouTube video
    yt = YouTube(video_url)
    video = yt.streams.filter(file_extension='mp4').first()
    video.download(filename='video.mp4')

    # Open the downloaded video
    cap = cv2.VideoCapture('video.mp4')

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open video")
        return

    # Loop to continuously play the video
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was successfully captured
        if not ret:
            print("Error: Couldn't capture frame")
            break

        # Display the frame
        cv2.imshow('YouTube Video', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
