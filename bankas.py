import csv

# ## kokios valiutos buvo naudotos?

# file = open('sampleData.csv','r', encoding='utf8')
# print(file.read())
# file.close()

# uniquevaliutos = set()
# with open('sampleData.csv',encoding='utf8') as file:
#     lines = file.read().split('\n')[1:]
#     for line in lines:
#         valiutos = (line.split(',')[6])
#         uniquevaliutos.add(valiutos)
#     print(uniquevaliutos)

# ## kiek income, outcome?(ignoruojant valiutas)

# pajamos = 0
# islaidos = 0
# with open('sampleData.csv', encoding='utf8') as file:
#     lines = file.read().split('\n')[1:]
#     for line in lines:
#         line = line.replace('"','')
#         if line.split(',')[7] == 'K':
#             pajamos += float(line.split(',')[5])
#         else:
#             islaidos += float(line.split(',')[5])
#     print("Visos gautos pajamos:",pajamos)
#     print("Visos islaidos:", islaidos)


# ## kiek income, outcome pagal kiekvieną valiutą?

# pajamoseur = 0
# islaidoseur = 0
# pajamosgbp = 0
# islaidosgbp = 0
# with open('sampleData.csv', encoding='utf8') as file:
#     lines = file.read().split('\n')[1:]
#     for line in lines:
#         line = line.replace('"','')
#         if line.split(',')[7] == 'K':
#             if line.split(',')[6] == 'EUR':
#                 pajamoseur += float(line.split(',')[5])
#             else:
#                 pajamosgbp += float(line.split(',')[5])
#         elif line.split(',')[7] == 'D':
#             if line.split(',')[6] == 'EUR':
#                 islaidoseur += float(line.split(',')[5])
#             else:
#                 islaidosgbp += float(line.split(',')[5])
#     print("Visos gautos pajamos eurais:",pajamoseur)
#     print("Visos gautos pajamos funtais:", pajamosgbp)
#     print("Visos islaidos eurais:", islaidoseur)
#     print("Visos islaidos funtais:", islaidosgbp)

# ## kiek buvo išleista kiekvieną mėnesį?

# islaidos01 = 0
# islaidos02 = 0
# islaidos03 = 0
# islaidos04 = 0
# with open('sampleData.csv', encoding='utf8') as file:
#     lines = file.read().split('\n')[1:]
#     for line in lines:
#         line = line.replace('"','')
#         if line.split(',')[7] == 'D':
#             year = line.split(',')[2]
#             month = year[5:7]
#             # print(month)
#             if month == '01':
#                 islaidos01 += float(line.split(',')[5])
#             elif month == '02':
#                 islaidos02 += float(line.split(',')[5])
#             elif month == '03':
#                 islaidos03 += float(line.split(',')[5])
#             elif month == '04':
#                 islaidos04 += float(line.split(',')[5])
#
#     print("Islaidos uz sausi:", islaidos01)
#     print("Islaidos uz vasari:", islaidos02)
#     print("Islaidos uz kova:", islaidos03)
#     print("Islaidos uz balandi:", islaidos04)
#
# ## kiek buvo uždirbta kiekvieną mėnesį?
#
# pajamos01 = 0
# pajamos02 = 0
# pajamos03 = 0
# pajamos04 = 0
# with open('sampleData.csv', encoding='utf8') as file:
#     lines = file.read().split('\n')[1:]
#     for line in lines:
#         line = line.replace('"','')
#         if line.split(',')[7] == 'K':
#             year = line.split(',')[2]
#             month = year[5:7]
#             # print(month)
#             if month == '01':
#                 pajamos01 += float(line.split(',')[5])
#             elif month == '02':
#                 pajamos02 += float(line.split(',')[5])
#             elif month == '03':
#                 pajamos03 += float(line.split(',')[5])
#             elif month == '04':
#                 pajamos04 += float(line.split(',')[5])
#
#     print("Pajamos uz sausi:", pajamos01)
#     print("Pajamos uz vasari:", pajamos02)
#     print("Pajamos uz kova:", pajamos03)
#     print("Pajamos uz balandi:", pajamos04)
#
# ## koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)
#
# sausis = pajamos01 - islaidos01
# vasaris = sausis + pajamos02 - islaidos02
# kovas = vasaris + pajamos03 - islaidos03
# balandis = kovas + pajamos04 - islaidos04
# print('Pinigu likutis sausio pabaigoje:',sausis) ## 1209.5
# print('Pinigu likutis vasario pabaigoje:',vasaris) ## 2640.5
# print('Pinigu likutis kovo pabaigoje:',kovas) ## 3872.0
# print('Pinigu likutis balandzio pabaigoje:',balandis) ## 4860.51
#
# ## susikurti veikiancia funkcija kitame .py faile ir ja isinesti i pagrindini pyraga
# import funkcijos
# funkcijos.fulllist()

# ## koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)
#
# likutis01 = 0
# likutis02 = 0
# likutis03 = 0
# likutis04 = 0
# with open('sampleData.csv', encoding='utf8') as file:
#     lines = file.read().split('\n')[1:]
#     for line in lines:
#         line = line.replace('"', '')
#         if line.split(',')[7] == 'D':
#             year = line.split(',')[2]
#             month = year[5:7]
#             if month == '01':
#                 likutis01 -= float(line.split(',')[5])
#             elif month == '02':
#                 likutis02 -= float(line.split(',')[5])
#             elif month == '03':
#                 likutis03 -= float(line.split(',')[5])
#             elif month == '04':
#                 likutis04 -= float(line.split(',')[5])
#         elif line.split(',')[7] == 'K':
#             year = line.split(',')[2]
#             month = year[5:7]
#             if month == '01':
#                 likutis01 += float(line.split(',')[5])
#             elif month == '02':
#                 likutis02 += float(line.split(',')[5])
#             elif month == '03':
#                 likutis03 += float(line.split(',')[5])
#             elif month == '04':
#                 likutis04 += float(line.split(',')[5])
#     print('Likutis sausio pabaigoje:', likutis01)
#     print('Likutis vasario pabaigoje:', likutis01+likutis02)
#     print('Likutis kovo pabaigoje:', likutis01+likutis02+likutis03)
#     print('Likutis balandzio pabaigoje:', likutis01+likutis02+likutis03+likutis04)

# ## koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?

likutiseur01 = 0
likutiseur02 = 0
likutiseur03 = 0
likutiseur04 = 0
likutisgbp01 = 0
likutisgbp02 = 0
likutisgbp03 = 0
likutisgbp04 = 0
with open('sampleData.csv', encoding='utf8') as file:
    lines = file.read().split('\n')[1:]
    for line in lines:
        line = line.replace('"', '')
        if line.split(',')[7] == 'D':
            if line.split(',')[6] == 'EUR':
                year = line.split(',')[2]
                month = year[5:7]
                if month == '01':
                    likutiseur01 -= float(line.split(',')[5])
                elif month == '02':
                    likutiseur02 -= float(line.split(',')[5])
                elif month == '03':
                    likutiseur03 -= float(line.split(',')[5])
                elif month == '04':
                    likutiseur04 -= float(line.split(',')[5])
            elif line.split(',')[6] == 'GBP':
                year = line.split(',')[2]
                month = year[5:7]
                if month == '01':
                    likutisgbp01 -= float(line.split(',')[5])
                elif month == '02':
                    likutisgbp02 -= float(line.split(',')[5])
                elif month == '03':
                    likutisgbp03 -= float(line.split(',')[5])
                elif month == '04':
                    likutisgbp04 -= float(line.split(',')[5])

        elif line.split(',')[7] == 'K':
            if line.split(',')[6] == 'EUR':
                year = line.split(',')[2]
                month = year[5:7]
                if month == '01':
                    likutiseur01 += float(line.split(',')[5])
                elif month == '02':
                    likutiseur02 += float(line.split(',')[5])
                elif month == '03':
                    likutiseur03 += float(line.split(',')[5])
                elif month == '04':
                    likutiseur04 += float(line.split(',')[5])
            elif line.split(',')[6] == 'GBP':
                year = line.split(',')[2]
                month = year[5:7]
                if month == '01':
                    likutisgbp01 += float(line.split(',')[5])
                elif month == '02':
                    likutisgbp02 += float(line.split(',')[5])
                elif month == '03':
                    likutisgbp03 += float(line.split(',')[5])
                elif month == '04':
                    likutisgbp04 += float(line.split(',')[5])

    print('Likutis eurais sausio pabaigoje:', likutiseur01)
    print('Likutis eurais vasario pabaigoje:', likutiseur01+likutiseur02)
    print('Likutis eurais kovo pabaigoje:', likutiseur01+likutiseur02+likutiseur03)
    print('Likutis eurais balandzio pabaigoje:', likutiseur01+likutiseur02+likutiseur03+likutiseur04)
    print()
    print('Likutis funtais sausio pabaigoje:', likutisgbp01)
    print('Likutis funtais vasario pabaigoje:', likutisgbp01 + likutisgbp02)
    print('Likutis funtais kovo pabaigoje:', likutisgbp01 + likutisgbp02 + likutisgbp03)
    print('Likutis funtais balandzio pabaigoje:', likutisgbp01 + likutisgbp02 + likutisgbp03 + likutisgbp04)