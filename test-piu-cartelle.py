import os
from datetime import datetime
from os import scandir


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def test2():
    basepath = 'my_directory/'
    albero = []
    check = 1
    albero.append(basepath)
    for elem in albero:
        print(f'Ora vediamo cosa c\'è dentro {elem}')
        with os.scandir(elem) as entries:
            for entry in entries:
                tipo = ''
                if entry.is_file():
                    tipo = 'file'
                if entry.is_dir():
                    tipo = 'cartella'
                    check +=1
                statinfo = os.stat(entry)
                access = datetime.fromtimestamp(statinfo.st_atime) ##/* time of last access */
                status = datetime.fromtimestamp(statinfo.st_ctime) ##/* time of last status change */
                modification = datetime.fromtimestamp(statinfo.st_mtime) ##/* time of last modification */
                if tipo == 'cartella':
                    print(f'{tipo}: {entry.name}\t\t\t Last Modified: {convert_date(statinfo.st_mtime)}')
                    albero.append(elem+entry.name+'/')
                elif tipo == 'file':
                    print(f'{tipo}: {entry.name}\t\t\t Last Modified: {convert_date(statinfo.st_mtime)}')
                else:
                    print('sconosciuto')
    #qui sono fuori dal for
    print(len(albero))


test2()