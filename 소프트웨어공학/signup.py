from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tempDB import MYDB



# 회원가입
def signup():
    # 회원 가입 완료 메세지 보내기
    def signup_ok_message():
        response = messagebox.showinfo("회원가입완료", "로그인해주세요")
        if response == 'ok':  window.destroy()
    # 그래픽 부분
    window = Tk()
    user_id, password, name, code, department, team = StringVar(), StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
    ttk.Label(window, text="UserID : ").grid(row=0, column=0, padx=10, pady=10)
    ttk.Label(window, text="Password : ").grid(row=1, column=0, padx=10, pady=10)
    ttk.Label(window, text="이름 : ").grid(row=2, column=0, padx=10, pady=10)
    ttk.Label(window, text="사원코드 : ").grid(row=3, column=0, padx=10, pady=10)
    ttk.Label(window, text="부서 : ").grid(row=4, column=0, padx=10, pady=10)
    ttk.Label(window, text="팀 : ").grid(row=5, column=0, padx=10, pady=10)
    # ?ttk로는 안됨
    user_id=Entry(window, textvariable=user_id)
    user_id.grid(row=0, column=1, padx=10, pady=10)
    password=Entry(window, textvariable=password)
    password.grid(row=1, column=1, padx=10, pady=10)
    name=Entry(window, textvariable=name)
    name.grid(row=2, column=1, padx=10, pady=10)
    code=Entry(window, textvariable=code)
    code.grid(row=3, column=1, padx=10, pady=10)
    department=Entry(window, textvariable=department)
    department.grid(row=4, column=1, padx=10, pady=10)
    team=Entry(window, textvariable=team)
    team.grid(row=5, column=1, padx=10, pady=10)
    ttk.Button(window, text="회원가입", command=lambda: [MYDB(user_id.get(), password.get(), name.get(), code.get(), department.get(), team.get()),signup_ok_message()]).grid(row=6, column=1, padx=10, pady=10)


    window.mainloop()