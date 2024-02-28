import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
     print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
     print('\033[32mConseguir acessar o site Pudim com sucesso!\033[m')