import os
def convertirCsvCiiu():
    ciiu_file = open('%s/utils/CODIGOS_CIIU_POR_MUNICIPIO.csv'%os.getcwd(),'r')
    new_ciiu_file = open('%s/utils/CODIGOS_CIIU.csv'%os.getcwd(),'w')
    for line in ciiu_file.readlines()[1:]:
        ciu = line.split(",")[0].split('**')
        print(ciu)
        new_ciiu_file.write(ciu[0][:-1]+','+ciu[1][1:] + '\n')

convertirCsvCiiu()