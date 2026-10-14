# Zad 2.10
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

if __name__ == '__main__':
    test_2_10()
    test_2_11()
    test_2_12()
    test_2_13()
