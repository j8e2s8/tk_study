import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("ttk 예제")
win.geometry("300x200")  # 처음 뜨는 창의 크기 설정

# ttk 레이블 추가
label1 = ttk.Label(win, text="입력 필드에 값을 입력하고 확인 버튼을 누르면 입력한 값을 반영하는 창 만들기")
label1.grid(column=0, row=0)

label2 = ttk.Label(win, text="아무 값을 입력하시오.")
label2.grid(column=0, row=1)

label3 = ttk.Label(win, text="결과 값 :")
label3.grid(column=0, row=2)

# tk 값 지정 공간 추가 (엔트리 위젯:입력 필드와 레이블이 동일하면 내용 반영됨)
def update_label():
    if input_var.get() == '10':   # 옳지 않은 답을 쓰면 다시 쓰게 유도할 수 있음.
        output_var.set("잘못 입력하셨습니다.")
    else:
        output_var.set(input_var.get())

input_var = tk.StringVar() # (어떤 값이 될지 모르는) 문자값을 변수에 할당해줌
input = tk.Entry(win, textvariable= input_var, width=10)
input.grid(column=1, row=1)  # 입력창

output_var = tk.StringVar() # (어떤 값이 될지 모르는) 문자값을 변수에 할당해줌
output = tk.Label(win, textvariable= output_var)
output.grid(column=1, row=2)  # 결과값

button = ttk.Button(win, text="확인", command=update_label, width=5)
button.grid(column=2, row=1)

# ttk 버튼 추가
button2 = ttk.Button(win, text="닫기", command=win.quit)
button2.grid(column=0, row=3)

win.mainloop()  # 항상 코드 마지막에 있어야함.