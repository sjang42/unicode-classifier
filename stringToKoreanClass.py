import argparse
from UnicodeToKoreanClass import UnicodeToKoreanClass


def parse_args():
    desc = "문자열을 9개의 글자 class로 나누어 개수를 셉니다"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        '--str', '-s', type=str, default='', help='확인할 문장', required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    count = [0 for _ in range(10)]
    classExample = ['가', '강', '갊', '구', '궁', '굶', '과', '광', '괆']

    if args is None:
        exit()
    lenStr = len(args.str)
    countKorean = 0

    for i in range(lenStr):
        classNum = UnicodeToKoreanClass(ord(args.str[i]))
        if classNum != -1:
            countKorean += 1
            count[classNum] += 1

    print("Total(kor) :", countKorean)
    for i in range(9):
        print('class' + str(i + 1) + '(' + classExample[i] + ')', ':',
              count[i + 1])


if __name__ == '__main__':
    main()
