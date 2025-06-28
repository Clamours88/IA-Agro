import os
from IPython.display import Video, display
import ipywidgets as widgets


def list_scene_files(directory='scenes'):
    """Return a list of video files in the specified directory."""
    supported = ('.mp4', '.mov', '.avi', '.mkv')
    return [f for f in os.listdir(directory) if f.lower().endswith(supported)]


def show_video(file_path):
    """Display a video file in JupyterLab."""
    display(Video(file_path))


def scene_player(directory='scenes'):
    """Create a dropdown-based video player for scenes inside a directory."""
    files = list_scene_files(directory)
    if not files:
        raise FileNotFoundError(f'No video files found in {directory}')

    dropdown = widgets.Dropdown(options=files, description='Scene:')

    def on_change(change):
        if change['type'] == 'change' and change['name'] == 'value':
            display(Video(os.path.join(directory, change['new'])))

    dropdown.observe(on_change)
    display(dropdown)

    # Show first video initially
    show_video(os.path.join(directory, files[0]))


if __name__ == '__main__':
    scene_player()
