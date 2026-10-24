def roman2int(roman: str):
    roman_to_int_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    # inne sposoby inicjalizacji słownika
    # dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)]

    # x = {} tworzymy pusty słownik i dodajemy elementy
    # x['I'] = 1
    # x['V'] = 5
    # ...

    # y = dict([('I',1),('V',5),...]) # za pomocą listy krotek

    roman = roman.replace("IV", "IIII")
    roman = roman.replace("IX", "IIIIIIIII")
    roman = roman.replace("XL", "XXXX")
    roman = roman.replace("XC", "XXXXXXXXX")
    roman = roman.replace("CD", "CCCC")
    roman = roman.replace("CM", "CCCCCCCCC")

    int_val = 0

    for key, value in roman_to_int_dict.items():
        int_val += roman.count(key) * value

    return int_val


def roman2int_test():
    assert roman2int("XV") == 15
    assert roman2int("XII") == 12
    assert roman2int("XIV") == 14
    assert roman2int("CMXCIX") == 999
    assert roman2int("CDXLIV") == 444
    assert roman2int("XCVIII") == 98
    print("tests passed")


if __name__ == "__main__":
    roman2int_test()
