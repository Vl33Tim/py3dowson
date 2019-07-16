bt_rng = int(input("Введите нижнюю границу счета: "))
tp_rng = (int(input("Введите верхнюю границу счета: ")) + 1)
shag = int(input("Введите шаг счета:  "))
for i in range (bt_rng, tp_rng, shag):
    print(i)
