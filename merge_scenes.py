import json
from pathlib import Path
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate_videoclips


def carregar_audio(caminhos):
    """Carrega uma lista de caminhos de audio, ignorando os que não existem."""
    clipes = []
    for caminho in caminhos:
        p = Path(caminho)
        if p.is_file():
            clipes.append(AudioFileClip(str(p)))
    return clipes


def combinar_cena(info):
    """Combina animação com narração, efeitos e música."""
    video = VideoFileClip(info["animacao"])
    audios = []

    narracao = info.get("narracao")
    if narracao:
        audios += carregar_audio([narracao])

    efeitos = info.get("sfx", [])
    if efeitos:
        audios += carregar_audio(efeitos)

    musica = info.get("musica")
    if musica:
        audios += carregar_audio([musica])

    if audios:
        trilha = CompositeAudioClip(audios)
        video = video.set_audio(trilha)
    return video


def unir_cenas(config):
    clips = [combinar_cena(cena) for cena in config["cenas"]]
    return concatenate_videoclips(clips, method="compose")


def main(arquivo_config: str, saida: str = "video_final.mp4"):
    with open(arquivo_config, "r", encoding="utf-8") as f:
        config = json.load(f)

    video = unir_cenas(config)
    video.write_videofile(saida)


if __name__ == "__main__":
    import sys

    config = sys.argv[1] if len(sys.argv) > 1 else "cenas.json"
    saida = sys.argv[2] if len(sys.argv) > 2 else "video_final.mp4"
    main(config, saida)
