def averageTurnaround(nameArr,memory): #평균시간 구하기
    reverse=memory[::-1] #메모리 리버스 하기(마지막으로 끝낸 작업의 사이클을 알기위해서)
    turnaround=[]#사이클 정보
    cnt=0 #작업이 들어온 시간
    for i in range(len(nameArr)):
        res=len(memory)-reverse.index(nameArr[i])-cnt #메모리 크기-작업이 처음발견된 위치-처음 들어온 시간
        turnaround.append(res)
        cnt=cnt+1

    return sum(turnaround)/cnt #평균내기
def jobStart(queue): #작업을 큐에서부터 메모리에 적재
    print(" 대기큐 현황:")
    print(queue)

    timeQuantum = 4 #timeQuantum은 4
    memory = []

    while queue:
        dicTemp = queue.pop(0) #작업을 꺼냄
        for key, value in dicTemp.items(): #키와 값으로 분리
            pass
        if value < timeQuantum: #작업의 사이클이 timeQuantum보다 작으면 메모리에 적재
            for i in range(value):
                memory.append(key)
        else:#작업의 사이클이 timeQuantum보다 크면
            value = value - timeQuantum# timeQuantum시간만큼 빼주고
            if value > 0:#뺀값이 0보다 크면
                for i in range(timeQuantum): #메모리에 적재 하기
                    memory.append(key)
                queue.append({key: value}) #딕셔너리 형태로 작업 넣기
            elif value == 0:#뺀값이 0  이면
                for i in range(timeQuantum): #메모리에 적재 하기
                    memory.append(key)
        print(queue)
    print("메모리 현황: ")
    print(memory)
    return memory
def readyQueue(job): #큐에다 작업 넣기
    queue = []
    for key, value in job.items():
        queue.append({key: value})

    return queue

def inputJob(): #작업 입력(작업의 자료형은 딕셔너리)
    job = {}#작업을 딕셔너리 형태로 입력 받기
    print('종료키 -1')
    while True:#원하는 만큼 작업 입력
        name = input('작업의 이름 입력: ')
        if name == str(-1):  break
        cycle = int(input('작업의 사이클 입력: '))
        job[name] = cycle

    return readyQueue(job),job.keys()


def main():
    queue,nameArr=inputJob()#queue: 작업이 큐에 적재 되어 있음 ,nameArr: 작업의 사이클을 찾을떄 필요한 변수
    memory=jobStart(queue)
    print("averageTurnaround: ")
    print(averageTurnaround(list(nameArr),memory))


if __name__=="__main__":
    main()
