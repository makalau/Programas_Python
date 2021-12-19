import ascii
#Só funciona em IDES mais robustas, como por exemplo Pycharm.
#Precisa instalar a biblioteca ascii usando o pip
#pip install --upgrade pip && pip install ascii
#para maiores informações: git show ascii

url ='https://1.bp.blogspot.com/-rErx67rNFYQ/XL8PYQqDXNI/AAAAAAAAWkg/9TcP6oC8OWMjpITY_dFzmJ5AZ1Lw8mk1ACPcBGAYYCw/s1600/python.ico'

result = ascii.loadFromUrl(url)
print(result)