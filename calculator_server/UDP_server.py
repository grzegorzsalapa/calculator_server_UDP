import socket
from .calculate import calculate, CalculationError


def main():
    HOST = ''
    PORT = 9010

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((HOST, PORT))
            print('\nServer started.')
            while True:
                data, client_addr = s.recvfrom(1024)
                if not data:
                    break
                expression = str(data)[2:][:-1]
                print('\nReceived expression: ', expression)
                try:
                    result = str(calculate(expression))
                except CalculationError as e:
                    result = str(e)
                print('Returned result: ', result)
                data = bytes(result, 'utf-8')
                s.sendto(data, client_addr)
    except KeyboardInterrupt:
        print("\rServer stopped.\n")


if __name__ == "__main__":
    main()
