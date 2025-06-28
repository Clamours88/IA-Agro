# IA-Agro

Este repositório inclui um exemplo simples de como gerar efeitos sonoros e músicas para cenas utilizando a API da Eleven Labs.

## Dependências

Instale as dependências com:

```bash
pip install -r requirements.txt
```

É necessário definir a variável de ambiente `ELEVEN_LABS_API_KEY` com sua chave de API.

## Geração de áudio

1. Edite o arquivo `scenes.json` para adicionar ou alterar as cenas desejadas.
2. Execute o script:

```bash
python generate_audio.py scenes.json output
```

Os arquivos de áudio gerados serão salvos no diretório informado (`output`, no exemplo acima).
