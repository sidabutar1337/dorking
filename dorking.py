import os
from googlesearch import search

def start():
    try:
        print('---------------------------')
        print('| Author: Sanggam Sidabutar|')
        print('| Github: sidabutar1337    |')
        print('| Facebook: zeussec1337    |')
        print('----------------------------')
        query =  input('search: ')
        count = input('country: ')
        results = int(input('jumlah pencarian: '))
        for link in search(query,lang=count,num_results=results):
            print(link)
        var_again = input('ingin menggunakan lagi?y/n ')
        if var_again == 'y' or var_again == 'Y':
            ulang = start()
            print(ulang)
        else:
            print('program stop')
            var_chat = input('ingin memberi masukan untuk author?y/n ')
            if var_chat == 'y' or var_chat == 'Y':
                message = input('masukan untuk author: ')
                kirim = os.system(f'xdg-open https://wa.me/+6285275797174?text={message}')
                print(kirim)
            else:
                print('goodbye')
    except ConnectionError:
        print('koneksi error')
        ulang = start()
        print(ulang)
    except ValueError:
        print('harap masukan angka untuk jumlah penarian')
        ulang = start()
        print(ulang) 
mulai =  start()
print(mulai)