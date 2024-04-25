## kokios valiutos buvo naudotos?

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

## kiek income, outcome?(ignoruojant valiutas)

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


## kiek income, outcome pagal kiekvieną valiutą?

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

## kiek buvo išleista kiekvieną mėnesį?

islaidos01 = 0
islaidos02 = 0
islaidos03 = 0
islaidos04 = 0
with open('sampleData.csv', encoding='utf8') as file:
    lines = file.read().split('\n')[1:]
    for line in lines:
        line = line.replace('"','')
        if line.split(',')[7] == 'D':
            year = line.split(',')[2]
            month = year[5:7]
            # print(month)
            if month == '01':
                islaidos01 += float(line.split(',')[5])
            elif month == '02':
                islaidos02 += float(line.split(',')[5])
            elif month == '03':
                islaidos03 += float(line.split(',')[5])
            elif month == '04':
                islaidos04 += float(line.split(',')[5])

    print("Islaidos uz sausi:", islaidos01)
    print("Islaidos uz vasari:", islaidos02)
    print("Islaidos uz kova:", islaidos03)
    print("Islaidos uz balandi:", islaidos04)

## kiek buvo uždirbta kiekvieną mėnesį?

pajamos01 = 0
pajamos02 = 0
pajamos03 = 0
pajamos04 = 0
with open('sampleData.csv', encoding='utf8') as file:
    lines = file.read().split('\n')[1:]
    for line in lines:
        line = line.replace('"','')
        if line.split(',')[7] == 'K':
            year = line.split(',')[2]
            month = year[5:7]
            # print(month)
            if month == '01':
                pajamos01 += float(line.split(',')[5])
            elif month == '02':
                pajamos02 += float(line.split(',')[5])
            elif month == '03':
                pajamos03 += float(line.split(',')[5])
            elif month == '04':
                pajamos04 += float(line.split(',')[5])

    print("Pajamos uz sausi:", pajamos01)
    print("Pajamos uz vasari:", pajamos02)
    print("Pajamos uz kova:", pajamos03)
    print("Pajamos uz balandi:", pajamos04)

## koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)

sausis = pajamos01 - islaidos01
vasaris = sausis + pajamos02 - islaidos02
kovas = vasaris + pajamos03 - islaidos03
balandis = kovas + pajamos04 - islaidos04
print('Pinigu likutis sausio pabaigoje:',sausis) ## 1209.5
print('Pinigu likutis vasario pabaigoje:',vasaris) ## 2640.5
print('Pinigu likutis kovo pabaigoje:',kovas) ## 3872.0
print('Pinigu likutis balandzio pabaigoje:',balandis) ## 4860.51


## koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)

