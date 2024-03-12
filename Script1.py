def find_str(line: str, query: str) -> bool:
    """Находит все строчки документа с определенным тегом"""
    if query in line:
        return True
    else:
        return False


def find_list(file_path: str) -> list:
    """Возвращает из файла массив КИЗ коробок"""
    with open(file_path, 'r', encoding='cp1251') as f:
        content = f.readlines()
        array = []
        for line in content:
            if find_str(line, '<НомУпак>'):
                array.append(line.strip().replace('<НомУпак>','').replace('</НомУпак>',''))
    return array


def find_unique(array: list) -> set:
    return set(array)


if __name__ == '__main__':
    first_set = find_unique(find_list('docs/UTD1.xml'))
    second_set = find_unique(find_list('docs/UTD2.xml'))
    print(sorted(first_set))
    print(sorted(second_set))
    print(first_set.difference(second_set))

