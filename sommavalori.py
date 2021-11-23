def somma_valori_file(my_file):
    values = []
    for line in my_file
    elements = line.split(",")
    if (elements[0] != "Date"):
        numero = elemenst[1]
        values.append(float(numero))
    my_file.close()
    return (sum(values))

my_file_shampoo = open("shampoo.txt", "r")
print(somma_valori_file(my_file_shampoo))
