def exists_word(word, instance):
    found_list = list()
    found_dict = dict()
    found_dict["ocorrencias"] = list()
    found_dict["arquivo"] = 0
    for element in instance.data:
        for index, linha in enumerate(element["linhas_do_arquivo"]):
            if word.lower() in linha.lower():
                if found_dict["arquivo"] == 0:
                    found_dict["arquivo"] = element["nome_do_arquivo"]
                    found_dict["palavra"] = word
                    found_dict["ocorrencias"].append({"linha": index + 1})
                    found_list.append(found_dict)
                else:
                    found_dict["ocorrencias"].append({"linha": index + 1})
    return found_list


def search_by_word(word, instance):
    pass
