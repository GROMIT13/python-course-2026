while True:
    val = input("Podaj liczbę rzeczywistą: ")
    if val == "stop":
        exit(0)
    try:
        val = float(val)
        print("{}, {}".format(val,pow(val,3)))
    except ValueError:
        print("Podana wartość nie jest liczbą rzeczywistą")
