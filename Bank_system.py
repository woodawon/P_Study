from collections import namedtuple
import ctypes

# namedtuple()로 구조체 선언
udata = namedtuple('udata', ['username', 'date', 'month', 'year', 'pnumber', 'fname', 'lname', 'address'])
money = namedtuple('money', ['usernameto', 'userpersonfrom', 'money1'])
upass = namedtuple('upass', ['password'])

# 콘솔 커서 위치 이동 함수
def gotoxy(x, y):
    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]
        
    handle = ctypes.windll.kernel32.GetStdHandle(-11)  
    coord = COORD(x, y)

    ctypes.windll.kernel32.SetConsoleCursorPosition(handle, coord)
    


