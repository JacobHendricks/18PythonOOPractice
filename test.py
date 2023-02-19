def read_file(name):
    word_list = []
    file = open(name)
    for line in file:
        word_list.append(line.strip())
    return word_list


def read_file(name):
    file = open(name)
    return [w.strip() for w in file]
