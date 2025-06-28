import os
import base64
import mimetypes
import json
import argparse

def image_to_data_url(path: str) -> str:
    """Encode uma imagem como uma Data URL."""
    mime_type, _ = mimetypes.guess_type(path)
    if mime_type is None:
        mime_type = 'application/octet-stream'
    with open(path, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('ascii')
    return f'data:{mime_type};base64,{encoded}'

def convert_directory(directory: str) -> dict:
    """Converte todas as imagens de um diretório em Data URLs."""
    urls = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            urls[filename] = image_to_data_url(filepath)
    return urls

def main():
    parser = argparse.ArgumentParser(description="Transforma todas as imagens de um diretório em URLs (formato Data URL).")
    parser.add_argument('directory', nargs='?', default='images', help='Diretório contendo as imagens.')
    parser.add_argument('-o', '--output', default='image_urls.json', help='Arquivo JSON para salvar as URLs geradas.')
    args = parser.parse_args()

    urls = convert_directory(args.directory)
    with open(args.output, 'w') as f:
        json.dump(urls, f, indent=2, ensure_ascii=False)
    print(f'Salvo {len(urls)} URLs em {args.output}')

if __name__ == '__main__':
    main()
