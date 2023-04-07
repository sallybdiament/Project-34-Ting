import sys

def txt_importer(path_file):
    list_file = []
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido")
    try:
        with open(path_file) as file:
            for line in file:
                new_line = line.replace('\n', '')
                list_file.append(new_line)
            return list_file
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
