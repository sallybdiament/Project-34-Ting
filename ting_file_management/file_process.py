from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for element in instance.data:
        if element['nome_do_arquivo'] == path_file:
            return None
    content_file = txt_importer(path_file)
    words_dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(content_file),
        'linhas_do_arquivo': content_file
    }
    instance.enqueue(words_dict)
    print(words_dict, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        removed = instance.dequeue()
        message = f"Arquivo {removed['nome_do_arquivo']} removido com sucesso"
        print(message, file=sys.stdout)


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(result, file=sys.stdout)
    except IndexError:
        sys.stderr.write("Posição inválida")
