import sys
from .file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            print(f"Arquivo {path_file} já foi processado.")
            return
    response = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(response),
        "linhas_do_arquivo": response,
    }
    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return
    file_removed = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file_removed} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        correct_position = instance.search(position)
        sys.stdout.write(str(correct_position))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
