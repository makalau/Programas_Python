def title(texto):
    yellow = f'\033[33m{texto}\033[m'
    print()
    print('-'*66)
    print(f'{yellow}'.center(66, ' '))
    print('-'*66)
    print()


def marca(texto):
    yellow = f'\033[33m{texto}\033[m'
    print('#################################################################'.center(66, ' '))
    print(f'     {yellow:^20}    '.center(66, ' '))
    print('#################################################################'.center(66, ' '))
    print()


def erro(texto):
    red = f'\033[31m{texto}\033[m'
    print('#####################################################'.center(66, ' '))
    print(f'     ###  {red:^55}###'.center(66, ' '))
    print('#####################################################'.center(66, ' '))





