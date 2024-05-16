import os
from datetime import datetime
from os import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    #now = datetime.now() # current date and time

    #year = now.strftime("%Y")
    #print("year:", year)

    #month = now.strftime("%m")
    #print("month:", month)

    #day = now.strftime("%d")
    #print("day:", day)

    #time = now.strftime("%H:%M:%S")
    #print("time:", time)

    #date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    #print("date and time:",date_time)	
    
    return formated_date

def get_files():
    dir_entries = scandir('my_directory/')
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')


def test_iniziali_sui_file():
    ##versione vecchia 	Returns a list of all files and folders in a directory
    entries = os.listdir('./')
    print(entries)
    #for entry in entries:
    #    print(entry)

    ##dalle versioni nuove si usa scandir - Returns an iterator of all the objects in a directory including file attribute information
    basepath = 'my_directory/cartella1/'
    with os.scandir(basepath) as entries:
        for entry in entries:
            tipo = 'sconosciuto'
            if entry.is_file():
                tipo = 'file'
            else:
                tipo = 'cartella'
            statinfo = os.stat(entry)
            access = datetime.fromtimestamp(statinfo.st_atime) ##/* time of last access */
            status = datetime.fromtimestamp(statinfo.st_ctime) ##/* time of last status change */
            modification = datetime.fromtimestamp(statinfo.st_mtime) ##/* time of last modification */
            print(f'{tipo}: {entry.name}\t\t\t Last Modified: {convert_date(statinfo.st_mtime)}')


    # Walking a directory tree and printing the names of the directories and files
    #for dirpath, dirnames, files in os.walk('my_directory/'):
    #    print(f'Found directory: {dirpath}')
    #    for file_name in files:
    #        print(file_name)

###########################################

test_iniziali_sui_file()

