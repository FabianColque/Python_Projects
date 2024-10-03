
#Reading CSV files

# with open('lutadores.csv') as arquivo:
#     dados = arquivo.read()
#     print(dados.split(','))

# from csv import reader

# with open('lutadores.csv') as myfile:
#     reader_csv = reader(myfile)
#     next(reader_csv)
#     for line in reader_csv:
#         print(line)

from csv import DictReader

with open('lutadores.csv') as myfile:
    reader_csv = DictReader(myfile, delimiter=',')
    for line in reader_csv:
        print(line)