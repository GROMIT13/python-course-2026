# Zad 3.1
# następujący kod zadziała poprawnie
# nie potrzebny jest nawias w warunku, oraz średniki po lini "result = x" i "result = y"
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

for i in "axby": if ord(i) < 100: print (i) #nie można użwyać operatora : w jednej lini wielokrotnie

for i in "axby": print (ord(i) if ord(i) < 100 else i) # ten przykład zadziała poniewarz : występuje raz

