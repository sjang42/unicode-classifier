#UnicodeClassifier



## Synopsis

Traditionally, hangul is devided into six types according to combination method. The example is below. We got one step further. We added one more feature to this. We see two-charactered last consonant and one-charactered last consonant differently. So we divide hangul into **nine types** and new types are **'FC/W/DLC'**, **'FC/HV/DLC'** and **'FC/HV/W/DLC'** when DLC is double Last Consonant.


## Code Explanation

UnicodeClassifier can be used as a library for classifying any hangul to 9 character using module UnicodeToKoreanClass placed in file **UnicodeToKoreanClass.py** this module gets an **unicode** and return the **class number**. this can be also used as class counter program using the python file **stringToKoreanClass.py**. this program gets a hangul stirng as an argument and display how many each nine class is used in that string.

## Test

you can just clone this repo and use like below.
```
$python stringToKoreanClass.py --str="원하는 한글을 입력하세요."
```

then you will get as a result
```
Total(kor) : 11
class1(가) : 3
class2(강) : 3
class3(갊) : 0
class4(구) : 1
class5(궁) : 3
class6(굶) : 0
class7(과) : 0
class8(광) : 1
class9(괆) : 0
```

## Requirement
* python 3.6

## License
MIT: http://rem.mit-license.org