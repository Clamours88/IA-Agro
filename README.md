# IA-Agro

Este repositório contém um exemplo simples de como gerar imagens para cenas de um roteiro utilizando a Midjourney API com a biblioteca **PIAPI**.

## Arquivos

- `scenes.txt`: arquivo de texto com a descrição de cada cena.
- `generate_scenes.py`: script que lê o arquivo de cenas e cria as imagens correspondentes via Midjourney.

## Uso

1. Instale a biblioteca `piapi` (ou a que implementa o cliente da Midjourney).
2. Defina a variável de ambiente `MIDJOURNEY_API_KEY` com a sua chave de acesso.
3. Execute o script:

```bash
python generate_scenes.py
```

As imagens geradas serão salvas na pasta `outputs/`.
