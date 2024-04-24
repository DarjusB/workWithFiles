print("--- 1 uzd ---")
# failas = open('uzduociu_faila.txt', 'w')
# failas.write('labas rytas,\n mano vardas Darjus\n')
#
# failas = open('uzduociu_faila.txt', 'a')
# failas.write('kaip cia taip?')
#
# print("----------------------------------")
#
# failas = open('uzduociu_faila.txt', 'r')
# print(failas.read())
#
# print("----------------------------------")
#
# failas = open('uzduociu_faila.txt', 'r')
# print(failas.readline())
#
# print("----------------------------------")
#
# failas = open('uzduociu_faila.txt', 'r')
# print(failas.readlines())
#
# print("----------------------------------")
#
# failas = open('uzduociu_faila.txt', 'r')
# for line in failas.readlines():
#     print(line)
#
# failas.close()

print("--- 2 uzd ---")
# failas2 = open('vardai.txt','w')
# failas2.write('labas o ka tu cia darai?\n')
# failas2.write('as pasiklydau :D\n')
# failas2.write('einam - padesiu\n')
#
# failas2 = open('vardai.txt', 'r')
# print(failas2.read())
# print("----------------")
# failas2 = open('vardai.txt', 'r')
# print(failas2.readline())
# print("-------------------")
# failas2 = open('vardai.txt', 'r')
# print(failas2.readlines())
#
# failas2.close()

print("--- 3 uzd ---")
# failas3 = open('automobilai.txt', 'w')
# failas3.write("Volvo;S60;2015;155000\n")
# failas3.write("Audi;A3;2005;255000\n")
# failas3.write("Audi;A7;2015;55000\n")
#
#
# automobiliai = []
# with open('automobilai.txt') as failas3:
#     for eilute in failas3:
#         eilute = eilute.rstrip('\n')
#         padalinta = eilute.split(';')
#         auto = dict(
#             marke = padalinta[0],
#             modelis = padalinta[1],
#             gamybosMetai = padalinta[2],
#             rida = padalinta[3]
#         )
#         automobiliai.append(auto)
# print(automobiliai)


failas3 = open('automobilai.txt', 'w')
failas3.write("Volvo;S60;2015;155000\n")
failas3.write("Audi;A3;2005;255000\n")
failas3.write("Audi;A7;2015;55000\n")
for metai in failas3:
    print(metai)

failas3.close()
