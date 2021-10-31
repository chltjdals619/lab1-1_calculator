print("구구단을 출력 프로그램입니다.")
print("원하는 단수를 입력하세요.")
mul = int(input())

for i in range(1, 10):
    result = mul*i
    print(mul, 'x', i, '=', result)
