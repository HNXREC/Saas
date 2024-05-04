import cv2
from pytube import YouTube
from moviepy.editor import VideoFileClip

def main():
    # YouTube video URL
    video_url = 'https://www.youtube.com/watch?v=KDxJlW6cxRk'

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

    # Load the audio of the YouTube video
    audio_clip = VideoFileClip('video.mp4').audio

    # Set up audio writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))

    # Loop to continuously play the video
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame was successfully captured
        if not ret:
            print("Error: Couldn't capture frame")
            break

        # Read next audio frame
        audio_frame = next(audio_clip.iter_frames())

        # Resize audio frame to match dimensions of video frame
        audio_frame = cv2.resize(audio_frame, (width, height))

        # Add audio to the frame
        frame_with_audio = cv2.addWeighted(frame, 1, audio_frame, 0.5, 0)

        # Display the frame
        cv2.imshow('YouTube Video', frame_with_audio)

        # Write frame to output video
        out.write(frame_with_audio)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video and close all OpenCV windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
