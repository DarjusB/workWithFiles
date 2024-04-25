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
# failas3.write("Audi;A7;2015;55000")
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


# metai = []
# totalsum = 0
# count = 0
# with open('automobilai.txt', 'r') as failas3:
#     lines = failas3.read().split('\n')
#     for line in lines:
#         print(line.split(';')[2])
#         metai.append(int(line.split(';')[2]))
#         totalsum += int(line.split(';')[2])
#         count += 1
#         vidurkis = totalsum / len(metai)
#     print(vidurkis)


print("--- 4 uzd ---")
from csv import reader, writer
### Bazes kurimaas
# failas4 = open('kainos.csv', 'w')
# failas4.write("bananai - 2.99\n")
# failas4.write("slyvos - 1.99\n")
# failas4.write("braskes - 5.99\n")
# failas4.write("kriausies - 4.99\n")
# failas4.write("ananasai - 8.99")
#
# failas4.close()
### Bazes analize
# kaina = []
# bendrasuma = 0
# count = 0
# with open('kainos.csv', 'r') as failas4:
#     lines = failas4.read().split('\n')
#     for line in lines:
#         # print(line.split(' - ')[1])
#         kaina.append(float(line.split(' - ')[1]))
#         bendrasuma += float(line.split(' - ')[1])
#         count += 1
#         vidurkis = round(bendrasuma) / len(kaina)
#     for itemcost in kaina:
#         if itemcost > vidurkis:
#             print(itemcost,"Brangus vaisius")
#         else:
#             print(itemcost,"Pigus vaisius")
#
#     print(f'Kainos vidurkis:', vidurkis, 'Eur')


print("--- 5 uzd ---")
# failas5 = open('statybos.csv', 'w')
# failas5.write("plytos - 1 - Eur\n")
# failas5.write("lentos - 2 - Eur\n")
# failas5.write("vynis - 2 - Eur\n")
# failas5.write("reples - 3 - Eur\n")
# failas5.write("lempos - 5 - Eur\n")
# failas5.write("laminatas - 20 - Eur\n")
# failas5.close()

# asortimentas = []
# with open('statybos.csv') as failas5:
#     csv_reader = reader('statybos.csv')
#     lines = failas5.read().split('\n')
#     for line in lines:
#         # print(line.split(' - ')[0])
#         asortimentas.append(line.split(' - ')[0])
#     print(asortimentas)
# print()
# failas5 = open('statybos.csv', 'r')
# print(failas5.read())
# failas5.close()

print("--- 6 uzd ---")

