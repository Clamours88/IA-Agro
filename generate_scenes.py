import os
from piapi import MidjourneyClient

SCENES_FILE = 'scenes.txt'
OUTPUT_DIR = 'outputs'


def load_scenes(filepath: str):
    """Read scenes from a text file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def create_scene(client: MidjourneyClient, prompt: str, out_dir: str):
    """Send prompt to Midjourney and save the resulting image."""
    response = client.create_image(prompt)
    image_path = os.path.join(out_dir, f"{prompt[:20].replace(' ', '_')}.png")
    with open(image_path, 'wb') as img_file:
        img_file.write(response.content)
    print(f"Generated {image_path}")


def main():
    api_key = os.environ.get('MIDJOURNEY_API_KEY')
    if not api_key:
        raise RuntimeError('Defina MIDJOURNEY_API_KEY no ambiente')

    client = MidjourneyClient(api_key=api_key)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    scenes = load_scenes(SCENES_FILE)
    for scene in scenes:
        create_scene(client, scene, OUTPUT_DIR)


if __name__ == '__main__':
    main()
