'''
**한글 클래스 분류**

class 1 : 가
class 2 : 강
class 3 : 갊
class 4 : 구
class 5 : 궁
class 6 : 굶
class 7 : 과
class 8 : 광
class 9 : 괆
'''
'''
**코드 예시**

종성 없음(1, 4, 7)
    중성이 오른쪽에    -> 1
    중성이 아래쪽에    -> 4
    중성이 둘다쪽에    -> 7
종성 하나(2, 5, 8)
    중성이 오른쪽에    -> 2
    중성이 아래쪽에    -> 5
    중성이 둘다쪽에    -> 8
종성 두개(3, 6, 9)
    중성이 오른쪽에    -> 3
    중성이 아래쪽에    -> 6
    중성이 둘다쪽에    -> 9
'''
'''
**한글 유니코드 인덱스**

1. 종성 인덱스
    - 없음 : 0
    - 하나 : 1, 4, 7, 8, 16, 17, 19, 21~27
    - 두울 : 2, 3, 5, 6, 9~15, 18, 20

2. 중성 인덱스
    - 우측 : 0~7, 20
    - 아래 : 8, 12, 13, 17, 18
    - 둘다 : 9~11, 14~16, 19
'''


def getNumJong(jongIdx):
    if jongIdx == 0:
        return 0
    elif jongIdx in [1, 4, 7, 8, 16, 17, 19, 21, 22, 23, 24, 25, 26, 27]:
        return 1
    else:
        return 2


def getPosJung(jungIdx):
    if jungIdx in [0, 1, 2, 3, 4, 5, 6, 7, 20]:
        return 1  # right
    elif jungIdx in [8, 12, 13, 17, 18]:
        return 4  # bottom
    else:
        return 7  # both


def UnicodeToKoreanClass(unicode):
    if unicode not in range(0xAC00, 0xD7AF + 1):
        return -1  # 오류 내고 싶다

    jongIdx = (unicode - 0xAC00) % 28
    jungIdx = (((unicode - 0xAC00) - jongIdx) / 28) % 21

    numJong = getNumJong(jongIdx)
    posJung = getPosJung(jungIdx)

    classNum = numJong + posJung
    return (classNum)
