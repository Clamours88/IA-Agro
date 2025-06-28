# IA-Agro

Este repositório inclui um pequeno script em Python para transformar imagens locais em URLs no formato Data URL.

## Utilização

1. Coloque suas imagens em um diretório (por padrão `images/`).
2. Execute o script `convert_images_to_urls.py`:

```bash
python3 convert_images_to_urls.py images -o urls.json
```

O script irá gerar o arquivo `urls.json` contendo um mapeamento entre nomes de arquivos e suas URLs em formato Data URL.
