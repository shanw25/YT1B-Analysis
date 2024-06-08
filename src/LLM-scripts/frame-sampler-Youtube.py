from pytube import YouTube
import cv2
import os

video_name = "8eBU4QfrFL4"
# def download_youtube_video(url, path=''):
#     yt = YouTube(url)
#     yt.streams.filter(file_extension='mp4').first().download(filename=path)
#     return path

def sample_frames(video_path, interval_seconds):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % (fps * interval_seconds) == 0:
            cv2.imwrite(f'./sampleData/sampleFrames/{video_name}/frame_{frame_count}.jpg', frame)
            print(f'Saved frame_{frame_count}.jpg')

        frame_count += 1

    cap.release()

def main():
    # video_path = download_youtube_video(video_url)
    video_path = "./sampleData/sampleVideos/{video_name}.mp4"
    sample_frames(video_path, 30)
    # Optional: Remove the downloaded video file after processing
    # os.remove(video_path)

if __name__ == "__main__":
    main()
