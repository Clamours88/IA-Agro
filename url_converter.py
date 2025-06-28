import sys
import urllib.parse
import unicodedata


def narracao_para_url(texto: str) -> str:
    """Converte uma string de narra\xc3\xa7\xc3\xa3o para um formato seguro de URL."""
    texto = texto.strip().lower()
    # Normaliza para remover acentos
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ascii', 'ignore').decode('ascii')
    # Substitui espa\xc3\xa7os por h\xc3\xadfens
    texto = texto.replace(' ', '-')
    # Remove caracteres n\xc3\xa3o alfanum\xc3\xa9ricos permitidos
    texto = ''.join(ch for ch in texto if ch.isalnum() or ch in '-_')
    return urllib.parse.quote(texto)


def main(args):
    if not args:
        print('Uso: python url_converter.py "Texto da narra\xc3\xa7\xc3\xa3o"')
        return
    texto = ' '.join(args)
    url = narracao_para_url(texto)
    print(url)


if __name__ == '__main__':
    main(sys.argv[1:])
