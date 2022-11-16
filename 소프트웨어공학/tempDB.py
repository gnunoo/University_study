
def MYDB(_user_id, _password, _name, _code, _department, _team):
    user_id, password, name, code, department, team=_user_id, _password, _name, _code, _department, _team
    arr=[]
    arr.append((user_id, password, name, code, department, team))
    with open('userinfo.txt','w') as f: f.write(str(arr))
    print(f'데이터 저장 완료:{arr}')

