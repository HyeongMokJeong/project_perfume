from os import link
import  sqlite3
from tkinter import *
import tkinter.messagebox as msgbox

def start():
    root = Toplevel()
    root.title("향수 추가") #이름
    root.resizable(True, True) #창 크기 변경 불가
    # 엔트리 지우는 함수
    def handle_click(event):
        link.delete(0, "end")
        link.unbind("<Button-1>")

    # 링크 텍스트 엔트리
    link = Entry(root,width=30) #entry는 한줄 입력
    link.insert(0, "향수 이름을 입력하세요.")
    link.grid(row=0, column=3, pady=10)
    link.bind("<Button-1>", handle_click)

    # 향 종류 선택 라디오버튼
    Label(root, text='종류').grid(row=1, column=3)
    kind = StringVar()
    kind1 = Radiobutton(root, text='플로랄', value='플로랄', variable=kind)
    kind1.select()
    kind1.grid(row=2, column=1)
    kind2 = Radiobutton(root, text='프루티', value='프루티', variable=kind).grid(row=2, column=2)
    kind3 = Radiobutton(root, text='그린', value='그린', variable=kind).grid(row=2, column=3)
    kind4 = Radiobutton(root, text='스파이시', value='스파이시', variable=kind).grid(row=2, column=4)
    kind5 = Radiobutton(root, text='구르망', value='구르망', variable=kind).grid(row=3, column=1)
    kind6 = Radiobutton(root, text='우디', value='우디', variable=kind).grid(row=3, column=2)
    kind7 = Radiobutton(root, text='시트러스', value='시트러스', variable=kind).grid(row=3, column=3)
    kind8 = Radiobutton(root, text='알데히드', value='알데히드', variable=kind).grid(row=3, column=4)

    # 향 종류2 선택 라디오버튼
    Label(root, text='종류2').grid(row=4, column=3, pady=10)
    kinds = StringVar()
    kinds1 = Radiobutton(root, text='플로랄', value='플로랄', variable=kinds)
    kinds1.select()
    kinds1.grid(row=5, column=1)
    kinds2 = Radiobutton(root, text='프루티', value='프루티', variable=kinds).grid(row=5, column=2)
    kinds3 = Radiobutton(root, text='그린', value='그린', variable=kinds).grid(row=5, column=3)
    kinds4 = Radiobutton(root, text='스파이시', value='스파이시', variable=kinds).grid(row=5, column=4)
    kinds5 = Radiobutton(root, text='구르망', value='구르망', variable=kinds).grid(row=6, column=1)
    kinds6 = Radiobutton(root, text='우디', value='우디', variable=kinds).grid(row=6, column=2)
    kinds7 = Radiobutton(root, text='시트러스', value='시트러스', variable=kinds).grid(row=6, column=3)
    kinds8 = Radiobutton(root, text='알데히드', value='알데히드', variable=kinds).grid(row=6, column=4)
    kinds9 = Radiobutton(root, text='NULL', value='NULL', variable=kinds).grid(row=7, column=3)

    # 성별 선택 라디오버튼
    Label(root, text='성별').grid(row=8, column=3, pady=10)
    sexual = StringVar()
    sexual1 = Radiobutton(root, text='남성', value='남성', variable=sexual)
    sexual1.select()
    sexual1.grid(row=9, column=1)
    sexual2 = Radiobutton(root, text='여성', value='여성', variable=sexual).grid(row=9, column=2)
    sexual3 = Radiobutton(root, text='중성', value='중성', variable=sexual).grid(row=9, column=3)

    # 계절 선택 라디오버튼
    Label(root, text='계절').grid(row=10, column=3, pady=10)
    wea = StringVar()
    wea1 = Radiobutton(root, text='봄', value='봄', variable=wea)
    wea1.select()
    wea1.grid(row=11, column=1)
    wea2 = Radiobutton(root, text='여름', value='여름', variable=wea).grid(row=11, column=2)
    wea3 = Radiobutton(root, text='가을', value='가을', variable=wea).grid(row=11, column=3)
    wea4 = Radiobutton(root, text='겨울', value='겨울', variable=wea).grid(row=11, column=4)

    
    def add2():
        lin = link.get()
        kin = kind.get()
        kins = kinds.get()
        seu = sexual.get()
        we = wea.get()

        conn = sqlite3.connect("perfume.db")
        cur = conn.cursor()

        cur.execute('INSERT INTO perfume1 VALUES(?, ?, ?, ?, ?)', 
            (f'{lin}', f'{kin}', f'{kins}', f'{seu}', f'{we}'))
        conn.commit()
        conn.close()
        msgbox.showinfo('알림', '정상적으로 추가되었습니다.')

    btn = Button(root, text="추가", command=add2)
    btn.grid(row=12, column=3, pady=10)

    root.mainloop()