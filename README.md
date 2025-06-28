# IA-Agro

This repository contains utilities for working with video scenes in JupyterLab.

## Scene Viewer

`scene_viewer.py` provides a simple widget-based player to navigate and play
video files from a `scenes/` directory.

### Usage

1. Place your video files (e.g., `.mp4`) inside a folder named `scenes` in the
   repository root.
2. In a JupyterLab notebook, import and launch the player:
   ```python
   import scene_viewer
   scene_viewer.scene_player()
   ```
3. Select a scene from the dropdown to play the video inline.

The first video found in the directory will be displayed automatically.
