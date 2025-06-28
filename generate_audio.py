import json
import os
from pathlib import Path
from typing import List, Dict

import requests

API_BASE = "https://api.elevenlabs.io/v1"
API_KEY_ENV = "ELEVEN_LABS_API_KEY"


def _post(endpoint: str, data: Dict[str, str]) -> bytes:
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        raise RuntimeError(f"Set the {API_KEY_ENV} environment variable")
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
    }
    url = f"{API_BASE}/{endpoint}"
    resp = requests.post(url, json=data, headers=headers)
    resp.raise_for_status()
    return resp.content


def generate_sound_effect(prompt: str) -> bytes:
    data = {
        "text": prompt,
        # Additional parameters can be added here
    }
    return _post("sound-effects/generate", data)


def generate_music(prompt: str) -> bytes:
    data = {
        "text": prompt,
    }
    return _post("music/generate", data)


def generate_for_scene(scene: Dict[str, str], out_dir: Path) -> None:
    name = scene["name"].replace(" ", "_")
    print(f"Generating audio for scene '{name}'")

    sfx_data = generate_sound_effect(scene["sound_effects"])
    sfx_path = out_dir / f"{name}_sfx.mp3"
    sfx_path.write_bytes(sfx_data)

    music_data = generate_music(scene["music"])
    music_path = out_dir / f"{name}_music.mp3"
    music_path.write_bytes(music_data)


def main(scenes_file: str, output_dir: str) -> None:
    with open(scenes_file, "r", encoding="utf-8") as fh:
        scenes: List[Dict[str, str]] = json.load(fh)

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for scene in scenes:
        generate_for_scene(scene, out_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate audio for scenes via Eleven Labs API")
    parser.add_argument("scenes", help="Path to scenes.json")
    parser.add_argument("output", help="Directory to store generated audio files")

    args = parser.parse_args()
    main(args.scenes, args.output)
