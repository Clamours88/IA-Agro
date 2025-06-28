import argparse
import glob
import os
import subprocess
import sys


def merge_scenes(files, output):
    """Join video files into a single output file."""
    try:
        from moviepy.editor import VideoFileClip, concatenate_videoclips
    except ImportError:
        # Fallback to ffmpeg concat if moviepy is unavailable
        concat_path = "concat_list.txt"
        with open(concat_path, "w", encoding="utf-8") as concat_file:
            for f in files:
                concat_file.write(f"file '{f}'\n")
        cmd = [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            concat_path,
            "-c",
            "copy",
            output,
        ]
        subprocess.run(cmd, check=True)
        os.remove(concat_path)
        return

    clips = [VideoFileClip(f) for f in files]
    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(output)
    final.close()


def main():
    parser = argparse.ArgumentParser(description="Merge scenes into a single video")
    parser.add_argument(
        "scenes",
        nargs="+",
        help="Paths or glob patterns for scene files in order",
    )
    parser.add_argument(
        "-o", "--output", default="final_video.mp4", help="Output video file"
    )
    args = parser.parse_args()
    files = []
    for pattern in args.scenes:
        matched = sorted(glob.glob(pattern))
        if not matched:
            parser.error(f"No files matched pattern: {pattern}")
        files.extend(matched)
    merge_scenes(files, args.output)


if __name__ == "__main__":
    main()
