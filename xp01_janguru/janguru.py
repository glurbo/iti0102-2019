"""jänguru"""


def asi(value: int):
    d = {range(0, 10): "Tallinn"}
    for value in d:
        return d[value]
    else:
        return False


if __name__ == '__main__':
    print(asi(5))
