# Zad 2.10-2.19
# to execute run
# python3 zad2/zad10-19.py

def exercise_2_10(string: str) -> int:
    return len(string.split())

def test_2_10(): 
    assert exercise_2_10("""abc def ghj""") == 3
    assert exercise_2_10("""Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.""") == 31
    assert exercise_2_10(""" kajsd   aaa a    anv\n\taaa""") == 5

def exercise_2_11(string: str) -> str:
    return '_'.join(list(string))

def test_2_11():
    assert exercise_2_11("Pomidor") == "P_o_m_i_d_o_r"
    assert exercise_2_11("Dwa Pomidory") == "D_w_a_ _P_o_m_i_d_o_r_y"

def exercise_2_12_first_char(string: str) -> str:
    words = string.split()
    return ''.join([ word[0] for word in words ])

def exercise_2_12_last_char(string: str) -> str:
    words = string.split()
    return ''.join([ word[-1] for word in words ])

def test_2_12():
    assert exercise_2_12_first_char("""Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.""") == "LOmtjjzIctcttsdKcsDptwcoWiobtpt"
    assert(exercise_2_12_last_char("""Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.""")) == ",o!yśk;eęa,noę,oę.śćąwjeęi,oęo."

def exercise_2_13(string: str):
    words = string.split()
    lengths = [ len(word) for word in words ]
    return sum(lengths)

def test_2_13():
    assert exercise_2_13("""Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.""") == 146

def exercise_2_14(string: str):
    words = string.split()
    a = max(words, key=len)
    b = len(a)
    return a,b

def test_2_14():
    assert exercise_2_14("""Litwo, Ojczyzno moja! ty jesteś jak zdrowie; Ile cię trzeba cenić, ten tylko się dowie, Kto cię stracił. Dziś piękność twą w całej ozdobie Widzę i opisuję, bo tęsknię po tobie.""") == ("Ojczyzno", 8)
    assert exercise_2_14(""" abdc dacb \n\n\n\n\n a""") == ("abdc", 4)
    assert exercise_2_14(" abdc dacb \n\n\n\n\n a") == ("abdc", 4)

def exercise_2_15(L: list) -> str:
    return ''.join(str(num) for num in L)

def test_2_15():
    assert exercise_2_15([1,4,12,7,9]) == "141279"
    assert exercise_2_15([]) == ""

def exercise_2_16(string: str):
    return string.replace("GvR", "Guido van Rossum")

def test_2_16():
    assert exercise_2_16("GvR") == "Guido van Rossum"
    assert exercise_2_16("Gvr") == "Gvr"
    assert exercise_2_16("text GvR text") == "text Guido van Rossum text"
    assert exercise_2_16("textGvR") == "textGuido van Rossum"

def exercise_2_17_alphabetic(string: str):
    words = string.split()
    return sorted(words)

def exercise_2_17_length(string: str):
    words = string.split()
    return sorted(words, key=len)

def test_2_17():
    assert exercise_2_17_alphabetic("aaa bbb aab") == ['aaa', 'aab', 'bbb']
    assert exercise_2_17_alphabetic("Ala ma kota") == ['Ala', 'kota', 'ma']
    assert exercise_2_17_alphabetic("") == []
    assert exercise_2_17_length("Ala ma kota") == ['ma', 'Ala', 'kota']
    assert exercise_2_17_length("") == []

def exercise_2_18(number: int):
    string = str(number)
    return string.count('0')

def test_2_18():
    assert exercise_2_18(1234567890) == 1
    assert exercise_2_18(123456789) == 0
    assert exercise_2_18(0x14) == 1
    assert exercise_2_18(123002340510123012302340) == 7
    assert exercise_2_18(-1230430) == 2

def exercise_2_19(L: list):
    return ''.join([ str(e).zfill(3) for e in L ])
    
def test_2_19():
    assert exercise_2_19([1, 10 , 100]) == "001010100"
    assert exercise_2_19([]) == ""
    assert exercise_2_19([17]) == "017" 

if __name__ == '__main__':
    test_2_10()
    test_2_11()
    test_2_12()
    test_2_13()
    test_2_14()
    test_2_15()
    test_2_16()
    test_2_17()
    test_2_18()
    test_2_19()
