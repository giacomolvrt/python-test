import os
from datetime import datetime
from os import scandir


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    #formated_date = d.strftime('%d %b %Y')   18 Apr 2022
    formated_date = d.strftime('%d/%m/%Y')
    return formated_date

def test2():
    basepath = '/VIRTUALBOX/'
    albero = []
    num_folder = 1
    num_file = 0
    stringone = ''
    stringone = stringone + '['
    albero.append(basepath)
    for elem in albero:
        print(f'Ora vediamo cosa c\'è dentro {elem}')
        with os.scandir(elem) as entries:
            for entry in entries:
                statinfo = os.stat(entry)
                access = datetime.fromtimestamp(statinfo.st_atime) ##/* time of last access */
                status = datetime.fromtimestamp(statinfo.st_ctime) ##/* time of last status change */
                modification = datetime.fromtimestamp(statinfo.st_mtime) ##/* time of last modification */
                
                if entry.is_dir():
                    num_folder +=1
                    print(f'cartella: {entry.name}\t\t\t Last Modified: {convert_date(statinfo.st_mtime)}')
                    albero.append(elem+entry.name+'/')
                elif entry.is_file():
                    num_file +=1
                    #scommentare per stampare una riga per ogni file
                    #print(f'file: {entry.name}\t\t\t Last Modified: {convert_date(statinfo.st_mtime)}')
                    if num_file > 1:
                       stringone = stringone + ','
                    #costruzione dati senza info sul percorso
                    #stringone = stringone + '{"nome_file":"'+entry.name+'", "dt_modifica":"'+str(convert_date(statinfo.st_mtime))+'"}'
                    #costruzione dati anche con il percorso
                    stringone = stringone + '{"nome_file":"'+entry.name+'", "dt_modifica":"'+str(convert_date(statinfo.st_mtime))+', "percorso":"'+str(elem)+'"}'
                else:
                    print('sconosciuto')
    #qui sono fuori dal for
    stringone = stringone + ']'
    print(f'num_folder: {num_folder} - array albero {len(albero)}')
    print(f'num_file: {num_file}')
    return stringone

a = test2()
print(a)