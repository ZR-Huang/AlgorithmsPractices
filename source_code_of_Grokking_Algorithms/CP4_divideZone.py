# -*- coding:utf-8 -*-
def getLongerLine(width, length):
    if width > length:
        return width
    else:
        return length

def getShortLine(width, length):
    if width > length:
        return length
    else:
        return width

def divideZone(width, length):
    longerLine = getLongerLine(width=width, length=length)
    shorterLine = getShortLine(width=width, length=length)
    if width % length == 0 or length % width == 0:
        return shorterLine
    else:
        return divideZone(width=longerLine-shorterLine,length=shorterLine)

LENGTH = int(input('Length:'))
WIDTH = int(input('Width:'))
print('\n',divideZone(width=WIDTH, length=LENGTH))
