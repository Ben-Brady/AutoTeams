def CursorPosition(Line:int=0,Column:int=0):
    print(f'\033{Line};{Column}H',end='')

def CursorUp        (Offset:int=1):
    print(f'\033[{Offset}A',end='')
def CursorDown      (Offset:int=1):
    print(f'\033[{Offset}B',end='')
def CursorForward   (Offset:int=1):
    print(f'\033[{Offset}C',end='')
def CursorBackward  (Offset:int=1):
    print(f'\033[{Offset}D',end='')

def SaveCursorPosition():
    print('\033[s',end='')
def RestoreCursorPosition():
    print('\033[u',end='')

def EraseDisplay():
    print('\033[2J',end='')
def EraseLine(Amount:int=1):
    print('\033[K'*Amount,end='')