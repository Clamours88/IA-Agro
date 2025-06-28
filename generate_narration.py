"""Python script to generate narration for script scenes"""

import textwrap
import sys


def generate_narration(scene_description: str) -> str:
    """Generate a simple narration line based on a scene description."""
    return textwrap.fill(
        f"Nessa cena, {scene_description.strip()}. O que acontece a seguir promete envolver o espectador.",
        width=70,
    )


def main(scene_file: str) -> None:
    with open(scene_file, 'r', encoding='utf-8') as f:
        scenes = [line.strip() for line in f if line.strip()]

    for idx, scene in enumerate(scenes, start=1):
        print(f"Cena {idx}:")
        print(generate_narration(scene))
        print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python generate_narration.py <arquivo_de_cenas.txt>")
        sys.exit(1)

    main(sys.argv[1])
