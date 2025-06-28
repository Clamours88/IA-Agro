import os
import openai
import requests
from moviepy.editor import ImageSequenceClip, AudioFileClip, CompositeAudioClip

# Constants
PIAPI_KEY = os.getenv('PIAPI_KEY')  # Set this environment variable with your PIAPI key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

# Configure API clients
openai.api_key = OPENAI_API_KEY


def generate_script(theme: str, max_length: int = 600) -> str:
    """Generate a video script from a theme using ChatGPT."""
    prompt = f"Gerar um roteiro sobre: {theme}\nDuração máxima: {max_length} segundos."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Você é um criador de roteiros"},
                  {"role": "user", "content": prompt}],
    )
    script = response.choices[0].message['content']
    return script


def synthesize_speech(text: str, voice: str = "Bella", output_file: str = "narration.mp3") -> str:
    """Generate narration audio from text using ElevenLabs."""
    url = "https://api.elevenlabs.io/v1/text-to-speech/" + voice
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }
    r = requests.post(url, json=data, headers=headers)
    with open(output_file, "wb") as f:
        f.write(r.content)
    return output_file


def generate_images(prompt: str, num_images: int = 5) -> list:
    """Generate a list of image file paths using MidJourney via PIAPI."""
    images = []
    for i in range(num_images):
        response = requests.post(
            "https://api.piapi.ai/midjourney/generate",
            headers={"Authorization": f"Bearer {PIAPI_KEY}"},
            json={"prompt": prompt, "num_images": 1}
        )
        data = response.json()
        img_url = data['images'][0]
        img_data = requests.get(img_url).content
        img_path = f"image_{i}.png"
        with open(img_path, 'wb') as f:
            f.write(img_data)
        images.append(img_path)
    return images


def compose_video(image_files: list, narration_audio: str, music_audio: str, output_path: str = "output.mp4") -> str:
    """Compose a video from image sequence and audio tracks."""
    clip = ImageSequenceClip(image_files, fps=1)
    narration = AudioFileClip(narration_audio)
    music = AudioFileClip(music_audio)
    audio = CompositeAudioClip([music.volumex(0.2), narration])
    clip = clip.set_audio(audio)
    clip.write_videofile(output_path, fps=24)
    return output_path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a narrated video from a theme.")
    parser.add_argument("--theme", required=True, help="Tema do vídeo")
    parser.add_argument("--output", default="video.mp4", help="Arquivo de saída")
    parser.add_argument("--duration", type=int, default=300, help="Duração máxima em segundos")
    args = parser.parse_args()

    script = generate_script(args.theme, args.duration)
    narration = synthesize_speech(script)
    background_music = synthesize_speech("Música de fundo para o tema " + args.theme, voice="musical", output_file="music.mp3")
    images = generate_images(args.theme)
    compose_video(images, narration, background_music, args.output)
    print(f"Vídeo salvo em {args.output}")

