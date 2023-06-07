from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    data = []
    for index in range(len(instance)):
        file_data = instance.search(index)
        lines_search = [
            {
                "linha": position + 1
            }
            for position, line in enumerate(file_data["linhas_do_arquivo"])
            if word.casefold() in line.casefold()
        ]
        if lines_search:
            data.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": lines_search
                }
            )
    return data


def search_by_word(word, instance: Queue):
    data = []
    for index in range(len(instance)):
        file_data = instance.search(index)
        lines_search = [
            {
                "linha": position + 1,
                "conteudo": line
            }
            for position, line in enumerate(file_data["linhas_do_arquivo"])
            if word.casefold() in line.casefold()
        ]
        if lines_search:
            data.append(
                {
                    "palavra": word,
                    "arquivo": file_data["nome_do_arquivo"],
                    "ocorrencias": lines_search
                }
            )
    return data
