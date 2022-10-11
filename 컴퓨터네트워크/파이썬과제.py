# test용임 (그래서 한 파일에 소스 다 적을 거임)
# 1.키값 만들기
from collections import Counter
# 파일 읽어와서 문자열로 저장
with open('네트워크과제.txt','r') as f:   data=f.read()
# 복호화 하기 위해 대문자의 위치를 저장하자
upperIndex=["1" if ord(data[i])>=65 and ord(data[i])<=90 else '0' for i in range(len(data))]
with open('대문자위치.txt','w') as f:
    for i in range(len(upperIndex)):
        if i == len(upperIndex): f.write(upperIndex[i])
        else: f.write(upperIndex[i]+',')
# collections.Counter라이브러리 로 문자열의 모든 문자를 카운터(코테 문제 풀다 알게 되었다.)
readFileCounter=Counter(data.lower())
# 알파벳 소문자만 추출하고 갯수 세서 딕셔너리 형태로 만들기
countAlpha={chr(i):readFileCounter[chr(i)] for i in range(97,123)}
# 정렬(오름차순)  -> sorted에다 key 값으로 람다 함수를 이용하면 value를 이용한 정렬이 가능하다. 단, 반환 값이 튜플형태 이다
countAlpha=dict(sorted(countAlpha.items(),key=lambda x:x[1]))
countAlphakey=list(countAlpha.keys())
print(f'키값: {countAlpha}')
#파일 쓰기(파일로 쓸태는 무조건 문자열로 )
with open('키값.txt','w') as f:
    for i in countAlphakey:
        # 맨 마지막 문자는 개행문자를 삽입하지 않는다.
        if i==countAlphakey[25]: f.write(i)
        else: f.write(i+'\n')
# 복호화 하기 위해 대문자의 위치를 저장하자

# 2. 키 값 이용해서 암호화 하기
with open('키값.txt','r') as f:   alphaKey=f.read().split('\n')
with open('네트워크과제.txt','r') as f:   data=list(f.read().lower())
# 암호화 키를 다시 만든다.
encryptionKey={chr(97+i):alphaKey[i] for i in range(26)}
print(f'암호키:{encryptionKey}')
# 암호화(딕셔너리를 활용한 순회(해시)가 시간복작도가 빠름)
for i in range(len(data)):
    # 키 값이 있으면 데이터 변환
    if data[i] in encryptionKey:
        data[i]=encryptionKey[data[i]]
# 파일 쓰기
with open('암호화.txt','w') as f: f.write(''.join(data))

# 3. 복호화 과정
# 파일 불러오기
with open('키값.txt','r') as f:   alphaKey=f.read().split('\n')
with open('암호화.txt','r') as f:   data=list(f.read())
with open('대문자위치.txt','r') as f:   upperIndex=f.read().split(',')
# 키를 이용해서 복호화 키 만들기
dencryptionKey={alphaKey[i]:chr(97+i) for i in range(26)}
print(f'복호키:{dencryptionKey}')
# 복호화
for i in range(len(data)):
    # 키 값이 있으면 데이터 변환
    if data[i] in dencryptionKey:
        if upperIndex[i]=='1': data[i]=chr(ord(dencryptionKey[data[i]])-32)
        else: data[i]=dencryptionKey[data[i]]
# 파일 쓰기
with open('복호화.txt','w') as f: f.write(''.join(data))
