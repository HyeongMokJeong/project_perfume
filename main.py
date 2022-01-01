import  sqlite3
from tkinter import *

root = Tk()
root.title("향수 찾기 프로그램") #이름
# root.geometry("250x270+800+350") #크기 (가로x세로 + x좌표 + y좌표)
root.resizable(True, True) #창 크기 변경 불가

# 성별 조건 선택 라디오그룹
Label(root, text='성별').grid(row=0, column=2)

sex = StringVar()
sex1 = Radiobutton(root, text='남성', value=1, variable=sex).grid(row=1, column=1)
sex2 = Radiobutton(root, text='여성', value=2, variable=sex).grid(row=1, column=2)
sex3 = Radiobutton(root, text='중성', value=3, variable=sex).grid(row=1, column=3)

# 향 종류 조건 선택 체크박스
Label(root, text='종류').grid(row=2, column=2)

type1= StringVar()
type2= StringVar()
type3= StringVar() 
type4= StringVar() 
type5= StringVar()
type6 = StringVar() 
type7 = StringVar()
type8 = StringVar()
type1 = Checkbutton(root, text='플로랄', variable=type1).grid(row=3, column=1)
type2 = Checkbutton(root, text='프루티', variable=type2).grid(row=3, column=2)
type3 = Checkbutton(root, text='그린', variable=type3).grid(row=3, column=3)
type4 = Checkbutton(root, text='스파이시', variable=type4).grid(row=4, column=1)
type5 = Checkbutton(root, text='구르망', variable=type5).grid(row=4, column=2)
type6 = Checkbutton(root, text='우디', variable=type6).grid(row=4, column=3)
type7 = Checkbutton(root, text='시크러스', variable=type7).grid(row=5, column=1)
type8 = Checkbutton(root, text='알데히드', variable=type8).grid(row=5, column=2)

# 계절 조건 선택 라디오박스
Label(root, text='계절').grid(row=6, column=2)

weather = StringVar()
weather1 = Radiobutton(root, text='봄', value=1, variable=weather).grid(row=7, column=1)
weather2 = Radiobutton(root, text='여름', value=2, variable=weather).grid(row=7, column=2)
weather3 = Radiobutton(root, text='가을', value=3, variable=weather).grid(row=7, column=3)
weather4 = Radiobutton(root, text='겨울', value=4, variable=weather).grid(row=7, column=4)


def search():
    conn = sqlite3.connect("perfume.db")
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM perfume1 WHERE perfume1.성별 == '{sex.get()}' AND perfume1.계절 == '{weather.get()}'")
    row = cur.fetchall()
    print(row)

    conn.close()
btn = Button(root, text="검색", command=search)
btn.grid(row=8, column=2)

root.mainloop() #루프를 통해 창 닫히지 않게 해줌