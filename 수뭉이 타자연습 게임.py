import tkinter
import random

#순서도
'''
make_text() - 블럭을 일정 시간에 맞춰 생성한 뒤 리스트에 해당 x,y,글자 값을 저장해 drop할 준비를 마침
drop_text() - 리스트에서 글자를 가져와서 드랍시킴 리스트 속 모든 글자들에 해당함
            - 바닥까지 간 글자들은 life를 1차감시키고 오브젝트의 y값을 -50000시켜 점수가 한 번만 차감되도록 설정
word_compare() - Enter키가 입력되었을 때, entry.get()을 통해 내가 입력한 글자를 리스트의 글자들과 비교, 해당한 글자들을 빈칸("")으로 만듦
stage_level() - 플레이에 따라 점수가 추가되면, 난이도를 자동으로 조절함
root.after() - 반복 시행을 통해 위의 함수들이 지속적으로 작동하도록 함
'''

#리스트
ready = ["사슴","매화","소나무","송백관","청록관","상록관","본관","생활관","본관","계당관","수뭉이"]
ready2= ["한누리관","디자인대학","종합실기관1","종합실기관2","학생회관","학술정보관","학생생활관","식물과학관"]
ready3 = ["디자인학부","실내디자인전공", "세라믹디자인전공","산업디자인전공","커뮤니케이션디자인전공","패션디자인전공","텍스타일전공","스페이스디자인전공"]


#점수
score=0
#엔터 입력
enter_c=1
#목숨
life=10
#콤보
combo=0
#난이도
level=0
difficulty=0
#마우스 입력
mouse_c=0
#게임에서 블록의 낙하속도를 보여줌
speed=0
#게임 실행,0=준비,1=메인,2=오버
start=0
#게임에서 root.after로 실행된 game_main 총 횟수
count=0
#랜덤생성된 글자
sampletext=""
#랜덤하게 생성된 글자의 x,y 값
x_place=0
y_place=0
#PlaceList 안에 있는 리스트
code=[] #리스트속의 리스트로서 x,y,글자 3개의 값을 한 번에 가짐
#생성되었던 텍스트들을 담아두는 리스트
PlaceList=[] 
#맵에 생성된 글자들이 떨어지기 위해 맵에 표시된 글자들의 리스트(PlaceList)에 len()을 쓰기 위해 생성한 변수 n
n=0 
mouse_x = 0
mouse_y = 0
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
compare=0
comparelist=[] #entry.get()과 비교하는 것을 목적으로 만든 변수와 리스트

def mouse_move_press(e):
    global mouse_x,mouse_y
    mouse_x = e.x
    mouse_y = e.y
    
    

#Enter키 입력시
def enter_add(e):
    global enter_c
    enter_c=1



def make_text():
    global sampletext,x_place,y_place,code,level
    #글자 생성(일정한 시간)
    if (count+1)%45==0:
        #랜덤 텍스트 생성
        if level==0:
            sampletext=random.sample(ready,1)
        if level==1:
            sampletext=random.sample(ready2,1)
        if level==2:
            sampletext=random.sample(ready3,1)
        #code에 들어갈 3개의 변수 x,y,글자
        compare=str(sampletext)
        x_place=random.randint(150,1100)
        y_place=0
        code=[x_place,y_place,sampletext]
        #리스트 속에 리스트 넣기ㅣ
        comparelist.append(compare)
        PlaceList.append(code)
        


def drop_text():
    global n,code,difficulty,speed,score,life,combo
    n=len(PlaceList)
    for code in PlaceList:
        #낙하속도
        code[1]=code[1]+4+difficulty
        #수뭉이 뿔 근처
        if code[0]<190:
            if code[1]>470:
                code[2]=""
                code[1]=-500000000 #끝까지 간 글자의 삭제 및 위치 조정을 통한 점수에서의 배제
                print(code[1])
                score-=500
                combo=0
                life-=1


        #점수판 위
        elif code[0]<400:
            if code[1]>550:
                code[2]=""
                code[1]=-500000000
                print(code[1])
                score-=500
                combo=0
                life-=1
                

        #나머지 오른쪽 구역
        else:
            if code[0]>=380:
                if code[1]>800:
                    code[2]=""
                    code[1]=-500000000
                    print(code[1])
                    score-=500
                    combo=0
                    life-=1
        cvs.create_text(code[0],code[1],text=code[2],tag="letters")



def word_compare():
    global code,PlaceList,n,enter_c,score,combo
    n=len(PlaceList)
    #enter 했을 떄 entry.get()값과 리스트 안의 값이 동일할 때 삭제하는 역할
    if enter_c==1:
        for i in range(n):
            final="['"+typingbox1.get()+"']" #entry.get()의 글자형태 변형
            if comparelist[i]==final:        #for문을 통해 PlaceList의 글자들과 entry.get()값 비교
                typingbox1.delete(0,"end")   #형태를 맞추기 위해 comparelist로 비교함
                PlaceList[i][2]=""
                comparelist[i]=""
                PlaceList[i][1]=-50000000
                score=score+500+combo*10     #점수 계산(콤보 시 점수 추가)
                combo=combo+1
                enter_c=0
                break
                
            
                 


#인게임에서 난이도 상승 조건 
def stage_level():
    global score,difficulty
    if score>2000:
        difficulty=0.5
    elif score>800:
        difficulty=0.2
    else:
        difficulty=0



def game_start():
    global level,start
    cvs.create_rectangle(620,475,820,525,fill="blue")
    cvs.create_text(720,500,text="Easy",fill="white",font=("Times New Roman ",30))
    cvs.create_rectangle(620,575,820,625,fill="purple")
    cvs.create_text(720,600,text="Normal",fill="white",font=("Times New Roman ",30))
    cvs.create_rectangle(620,675,820,725,fill="black")
    cvs.create_text(720,700,text="Hard",fill="white",font=("Times New Roman ",30))
    if 620<= mouse_x and mouse_x <820 and 475<= mouse_y and mouse_y < 525 :
        mouse_c==1
        level=0
        start=1
    if 620<= mouse_x and mouse_x <820 and 575<= mouse_y and mouse_y < 625 :
        mouse_c==1
        level =1
        start=1
    if 620<= mouse_x and mouse_x <820 and 675<= mouse_y and mouse_y < 725 :
        mouse_c==1
        level =2
        start=1



def game_over():
    global start
    if life<=0:
        start=2
        cvs.create_image(720,405,image=bg2)



def game_main():
    global count,score,start
    game_start()
    if start==1:
        cvs.delete("all")
        cvs.create_image(720,405,image=bg1)
        cvs.delete("c")
        #표시되는 글자들(점수,목숨,실행횟수,콤보 4가지)
        cvs.create_text(270,700,text=score,fill="black",tag='c')
        cvs.create_text(50,50,text="life",fill="black",tag='c')
        cvs.create_text(110,50,text=life,fill="black",tag='c')
        cvs.create_text(50,100,text="콤보",fill="black",tag='c')
        cvs.create_text(110,100,text=combo,fill="black",tag='c')
        count+=1
    
        if enter_c==1:
            word_compare()
        cvs.delete("letters")
        make_text()
        drop_text()
        stage_level()
        cvs.delete("drop")
    game_over()

    root.after(50,game_main) #반복 시행




root=tkinter.Tk()
root.title("슴우 타자게임")

#입력창
typingbox1=tkinter.Entry()
typingbox1.pack()
#캔버스
cvs=tkinter.Canvas(root,width=1440,height=810)
cvs.pack()
#배경
bg1=tkinter.PhotoImage(file="1_back.png")
bg=tkinter.PhotoImage(file="3_intro.png")
cvs.create_image(720,405,image=bg)
#cvs.create_image(1080,300,image=bg_font)
#게임오버화면
bg2=tkinter.PhotoImage(file="2_back.png")

#enter키 입력시 함수 실행
root.bind("<ButtonPress>",mouse_move_press)
root.bind('<Return>',enter_add)
game_main()

root.mainloop()
