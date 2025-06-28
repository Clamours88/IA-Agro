# IA-Agro

Este projeto contém um exemplo de script em Python para gerar um vídeo narrado a partir de um tema utilizando APIs externas. O processo gera um roteiro com o ChatGPT, cria a narração e a música de fundo com o ElevenLabs, obtém imagens com o MidJourney via PIAPI e por fim monta o vídeo com o MoviePy.

## Instalação

1. Crie um ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

2. Defina as seguintes variáveis de ambiente com suas chaves de API:

- `OPENAI_API_KEY`
- `ELEVENLABS_API_KEY`
- `PIAPI_KEY`

## Uso

Execute o script passando o tema desejado:

```bash
python video_generator.py --theme "Seu tema aqui" --output video.mp4
```

O resultado será salvo no arquivo indicado. O tempo máximo do vídeo é de cinco minutos (300 segundos).
