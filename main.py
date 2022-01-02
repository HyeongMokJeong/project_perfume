import  sqlite3
from add import start
from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("향수 찾기 프로그램") #이름
# root.geometry("250x270+800+350") #크기 (가로x세로 + x좌표 + y좌표)
root.resizable(True, True) #창 크기 변경 불가

# 성별 조건 선택 라디오그룹
Label(root, text='성별').grid(row=0, column=2)

sex = StringVar()
sex1 = Radiobutton(root, text='남성', value='남성', variable=sex)
sex1.select()
sex1.grid(row=1, column=1)
sex2 = Radiobutton(root, text='여성', value='여성', variable=sex).grid(row=1, column=2)
sex3 = Radiobutton(root, text='중성', value='중성', variable=sex).grid(row=1, column=3)

# 향 종류 조건 선택 라디오박스
Label(root, text='종류').grid(row=2, column=2)

type= StringVar()
type1 = Radiobutton(root, text='플로랄', value='플로랄', variable=type)
type1.select()
type1.grid(row=3, column=1)
type2 = Radiobutton(root, text='프루티', value='프루티',variable=type).grid(row=3, column=2)
type3 = Radiobutton(root, text='그린', value='그린', variable=type).grid(row=3, column=3)
type4 = Radiobutton(root, text='스파이시', value='스파이시', variable=type).grid(row=4, column=1)
type5 = Radiobutton(root, text='구르망', value='구르망', variable=type).grid(row=4, column=2)
type6 = Radiobutton(root, text='우디', value='우디', variable=type).grid(row=4, column=3)
type7 = Radiobutton(root, text='시크러스', value='시크러스', variable=type).grid(row=5, column=1)
type8 = Radiobutton(root, text='알데히드', value='알데히드', variable=type).grid(row=5, column=2)

# 계절 조건 선택 라디오박스
Label(root, text='계절').grid(row=6, column=2)

weather = StringVar()
weather1 = Radiobutton(root, text='봄', value='봄', variable=weather)
weather1.select()
weather1.grid(row=7, column=1)
weather2 = Radiobutton(root, text='여름', value='여름', variable=weather).grid(row=7, column=2)
weather3 = Radiobutton(root, text='가을', value='가을', variable=weather).grid(row=7, column=3)
weather4 = Radiobutton(root, text='겨울', value='겨울', variable=weather).grid(row=7, column=4)

label1 = Label(root, text='안녕하세요')
label1.grid(row=9,column=2)


def search():
    conn = sqlite3.connect("perfume.db")
    cur = conn.cursor()
       
    cur.execute(f"SELECT DISTINCT * FROM perfume1 WHERE perfume1.성별 == '{sex.get()}' AND perfume1.계절 == '{weather.get()}' AND (perfume1.종류 == '{type.get()}' OR perfume1.종류2 == '{type.get()}')" )
    row = cur.fetchall()

    if len(row) == 0: label1.config(text="결과 없음")
    else: 
        result = ["제품명 / 향 종류1 / 향 종류2 / 성별 / 계절감 \n"]
        for i in range(0, len(row)):
            row[i] = list(row[i])
            word1 = '   /   '.join(row[i])
            result.append(word1)
        word2 = '\n'.join(result)
        label1.config(text=f"{word2}")
    conn.close()
    
btn = Button(root, text="검색", command=search)
btn.grid(row=8, column=2)

# 데이터 추가 함수
def data_add():
    root3 = Toplevel(root)
    root3.title("관리자") #이름
    root3.resizable(True, True) #창 크기 변경 불가

    def handle_click(event):
        link.delete(0, "end")
        link.unbind("<Button-1>")

     # 링크 텍스트 엔트리
    link = Entry(root3,width=30) #entry는 한줄 입력
    link.insert(0, "비밀번호를 입력하세요.")
    link.grid(row=0, column=3)
    link.bind("<Button-1>", handle_click)

    def createNewWindow():
        password = link.get()
        if password == '1234':
            root3.destroy()
            start()
            
        else:
            msgbox.showerror('경고', '비밀번호가 틀립니다.')

    btn = Button(root3, text="제출", command=createNewWindow)
    btn.grid(row=1,column=3)

btn = Button(root, text="데이터 추가", command=data_add)
btn.grid(row=8, column=4)

root.mainloop() #루프를 통해 창 닫히지 않게 해줌