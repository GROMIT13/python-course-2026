def element_list_a(list_a, list_b):
    return list(set(str(list_a)) & set(str(list_b)))


def element_list_b(list_a, list_b):
    return list(set(str(list_a)) | set(str(list_b)))


def element_list_test():
    assert element_list_a("abcdea", "lsacd") == ['d', 'c', 'a']
    assert element_list_a("abc", "def") == []
    assert element_list_a(1246890, 671723) == ['6','1','2']
    assert element_list_a(123,456) == []
    assert element_list_b("abcdea", "lsacd") == ['d', 's', 'b', 'c', 'a', 'e', 'l']
    assert element_list_b("abc", "def") == ['d', 'c', 'a', 'f', 'e', 'b']
    assert element_list_b(1246890, 671723) == ['7', '9', '2', '0', '8', '4', '6', '1', '3']
    assert element_list_b(123,456) == ['4', '5', '6', '1', '3', '2']
    print("tests passed")

if __name__ == "__main__":
    element_list_test()
