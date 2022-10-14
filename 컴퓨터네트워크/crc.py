# nomal 방식
import re
def cheaksum(dividend,divisor):
    # 1. data에 앞에 0이 있으면 0만 제거
    dividend=dividend.lstrip('0')
    # 3. 나머지는 temp에 담아놓는다.
    temp = dividend[len(divisor):]
    # 2. 제수만큼만 문자열 분리
    dividend=dividend[0:len(divisor)]
    print(f'first div:{dividend}')
    print(f'first temp:{temp}')
    while True:
        # 10. 추가할 문자가 없고 생성다항식+1 비트가 아니면 피제수 반환
        if len(temp)==0 and len(dividend)!=len(divisor): return dividend
        cnt=0
        # 4. xor 연산(리스트 반환)
        res=[ord(a) ^ ord(b) for a,b in zip(dividend,divisor)]
        # 5. 문자열로 바꾸기
        res=''.join(map(str,res))
        # 6. 제수^0=제수 따라서 0*제수에 해당하는 계산은 필요가 없음 그래서 앞에 0만 카운터
        for i in range(len(res)):
            if res[i]=='0': cnt+=1
            elif res[i] == '1': break
        # 7. 앞에 0제거
        res=res[cnt:]
        # 8. 새로운 제수 만들기
        dividend=res+temp[:cnt]
        # 9. 0을 추가한 만큼 제거
        temp=temp[cnt:]
        print(f'div:{dividend}, temp:{temp},res:{res}')
x=2
gp='x**8+x**2+x+1'
data='01101011'
divisor=bin(eval(gp))[2:]
max_list=max(map(int,re.findall(r'\d+',gp)))
dividend=data+('0'*max_list)
print(f'피제수:{dividend}')
print(f'제수:{divisor}')
cheak_sum=cheaksum(dividend,divisor).zfill(max_list)
print(f'cheaksum:{cheak_sum}')
print(f'transedata:{data+cheak_sum}')
