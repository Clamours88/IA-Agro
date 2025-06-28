import argparse
import os
import imageio


def animate_images(input_folder: str, output_file: str = "animation.gif", duration: float = 0.5) -> None:
    """Generate a GIF animation from all images in *input_folder*.

    This function assumes images were generated with PIAPI and stored in
    *input_folder*. They are combined in alphanumeric order into a single
    GIF.
    """
    frames = []
    for name in sorted(os.listdir(input_folder)):
        if name.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            path = os.path.join(input_folder, name)
            frames.append(imageio.imread(path))

    if not frames:
        raise FileNotFoundError("No supported images were found in the specified folder")

    imageio.mimsave(output_file, frames, duration=duration)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Animate images generated with PIAPI")
    parser.add_argument("input_folder", help="Folder containing the images generated via PIAPI")
    parser.add_argument("--output", default="animation.gif", help="Path to the resulting GIF file")
    parser.add_argument("--duration", type=float, default=0.5, help="Frame duration in seconds")
    args = parser.parse_args()
    animate_images(args.input_folder, args.output, args.duration)
