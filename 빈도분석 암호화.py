# 연습.py

def init_count_alpha(number):
    for i in range(26):  # 알파벳(a~z)갯수에 대해 모두 0으로 초기화 a:0개 b:0개 ...z:0개
        number.append(0)

    return number

def init_Alpha(Alpha):
    for i in range(26):  # 대문자를 저장한 배열 초기화
        Alpha.append(chr(ord("A")+i))

    return Alpha

def init_alpha(alpha):
    for i in range(26):  # 소문자를 저장한 배열 초기화
        alpha.append(chr(ord("a")+i))

    return alpha

def init_sort_alpha(sort_alpha):
    for i in range(26):  # 소문자(정렬)를 저장한 배열 초기화
        sort_alpha.append(chr(ord("a")+i))

    return sort_alpha

def init_Alpha_index(Alpha_index,data): #대문자의 위치를 저장한 배열을 0으로 저장
    for i in range(len(data)):
        Alpha_index.append(0)
    return Alpha_index


def count_alpha(number,data):
    for i in range(ord("a"),ord("z")+1): #알파벳의 소문자의 갯수 새기
        for j in range(0,len(data)):
            if(chr(i)==data[j]):
                number[i-97]+=1

    for i in range(ord("A"),ord("Z")+1): #알파벳의 대문자의 갯수 새기
        for j in range(0,len(data)):
            if(chr(i)==data[j]):
                number[i-65]+=1

    return number

def Alpha_index_mark(Alpha_index,data): #대문자의 위치 저장
    for i in range(len(data)):
        if (ord(data[i])>=ord("A")) and (ord(data[i])<=ord("Z")):
            Alpha_index[i]=1;
        else:
            Alpha_index[i]=0;

    return Alpha_index

def encryption(data,alpha,Alpha,sort_alpha): #데이터 암호화
    for i in range(len(data)):
        flag=False #플래그를 사용한 이유는 데이터가 중복되었을때 값이 중복 변환되는 것을 막기 위해서임 
        for j in range(26):
            if data[i]==alpha[j]: #소문자일 경우
                if flag==True:
                    continue
                data[i]=sort_alpha[j]
                flag=True
            elif data[i]==Alpha[j]:# 대문자일 경우
                if flag==True:
                    continue
                data[i]=sort_alpha[j]
                flag=True
    return data

def number_decoding(data,sort_alpha,alpha,dictionary_alpha):# 키값에 따라 복호화 진행(알파벳 빈도수로 복호화 진행)
    for i in range(len(data)): 
        flag=False
        for j in range(26):
            if data[i]==sort_alpha[j]:
                if flag==True:
                    continue
                data[i]=str(dictionary_alpha[alpha[j]])
                flag=True
    return data

def decoding(data,dictionary_alpha,dictionary_Alpha,Alpha_index): #알파벳으로 복호화 진행
    for i in range(len(data)): #대문자
         flag=False
         for key in dictionary_alpha.keys():
             if data[i]==str(key) and Alpha_index[i]==1:
                 if flag==True:
                     continue
                 data[i]=dictionary_Alpha[key]
                 flag=True
    for i in range(len(data)): #소문자
         flag=False
         for key in dictionary_alpha.keys():
             if data[i]==str(key) :
                 if flag==True:
                     continue
                 data[i]=dictionary_alpha[key]
                 flag=True

    return data

number=[] #알파벳의 갯수를 세기 위한 26개의 배열
alpha=[] #알파벳(소문자)를 저장하기 위한 배열
sort_alpha=[] #알파벳 빈도수에 따라 저장하기 위한 배열
Alpha=[] #알파벳 (대문자)를 저장하기 위한 배열

#파일을 열고 파일 안에 있는 데이터를 배열 값으로 저장
f=open("1000단어 이상의 파일.txt", 'rt',encoding='UTF8')
data=f.read()
data=list(data)

#변수 초기화
alpha=init_alpha(alpha)
sort_alpha=init_sort_alpha(sort_alpha)
Alpha=init_Alpha(Alpha)               
number=init_count_alpha(number)

number=count_alpha(number,data) #데이터 카운터

#카운터 한 데이터를 파일에 저장
f=open("count_alpha.txt",'w')
for i in range(26):
    f.write(str(number[i]))
    f.write('\n')

#알파벳 갯수와 갯수에 대한 알파벳을 내림차순으로 정렬
for i in range(len(number)): 
    for j in range(len(number)-1):
        if number[j]<number[j+1]:
            number[j],number[j+1]=number[j+1],number[j]
            sort_alpha[j],sort_alpha[j+1]=sort_alpha[j+1],sort_alpha[j]

#대문자에 위치를 배열값으로 저장
Alpha_index=[]
Alpha_index=init_Alpha_index(Alpha_index,data)
Alpha_index=Alpha_index_mark(Alpha_index,data)    


#암호화 하고 암화화된 데이터를 문자열로 치환
data=encryption(data,alpha,Alpha,sort_alpha)            
encoding_data=''.join(data)

#파일에다 암화화된 데이터 저장
f=open("encoding.txt",'wt',encoding='UTF8')
f.write(encoding_data)


#복호화 하기 위해 암호화 된 파일 불러오기 여기서 문자열로 데이터를 읽어왔기 때문에 데이터를 배열(리스트) 형태로 바꿔준다. 
f=open("encoding.txt", 'rt',encoding='UTF8')
encoding_data=f.read() 
data=list(encoding_data)

#복호화 하기 위해 키값(count_alpha.txt(알파벳의 빈도수를 저장한 파일))파일을 불러온다. 여기서 데이터를 \n 기준으로 저장했기 때문에 split 함수로 구분해준다.
f=open("count_alpha.txt",'r')

#소문자에 대해서 딕션너리  만들기(딕셔너리를 만드는 이유는 알파벳과 키값(알파벳 빈도수)을 연결하기 위해서 만들었다.)
count_data=f.readlines() # 배열 형태로 값을 읽어 온다.
count_data=''.join(count_data)# 배열을 문자열로 바꾼다.
count_data=count_data.split('\n') #여기서 데이터를 \n 기준으로 저장했기 때문에 split 함수로 구분해준다.
for i in range(26): #정수값으로 배열을 저장
    count_data[i]=int(count_data[i])
    
dictionary_alpha=dict(zip(alpha,count_data))# dict,zip 함수로 딕셔너리를 만든다. zip 함수는 zip(키,키값) 형태로 만들어 준다.


#키값(알파벳의 빈도수)로 복호화 진행
data=number_decoding(data,sort_alpha,alpha,dictionary_alpha) 
            
#알파벳으로 복호화 하기 위해 딕셔너리의 키와 키값을 바꿔서 저장

dictionary_alpha=dict(zip(count_data,alpha))
dictionary_Alpha=dict(zip(count_data,Alpha))

#알파벳으로 복호화 진행 
data=decoding(data,dictionary_alpha,dictionary_Alpha,Alpha_index)

#데이터를 문자열로 변환 하고 파일에 저장
decoding_data=''.join(data)
f=open("decoding.txt",'wt',encoding='UTF8')
f.write(decoding_data)




    

