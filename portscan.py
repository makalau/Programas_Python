import socket
import sys

if len(sys.argv) < 2:
    print("Passe o IP como argumento")
    sys.exit()

IP = sys.argv[1]
print('+'+'-'*18+'+')
print("| portas |  status |")
for porta in range(1, 1025):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.2)
    result = cliente.connect_ex((IP, porta))
    if result == 0:
        print('+'+'-'*18+'+')
        print(f"| {porta:^6} |  aberta |")
    cliente.close()
print('+'+'-'*18+'+')