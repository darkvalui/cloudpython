from tkinter import *
import pymysql
from project import rooms_crud
from PyQt5.Qt import left


# stay_id_input,stay_name_input,stay_address_input,stay_tel_input,stay_score_input,record= None,None,None,None,None,None

# room_img=None

def event_process1():
    print("주소검색")
    id_input = stay_id_input.get()
    rooms_crud.db_rooms_select(id_input)
    record=rooms_crud.db_rooms_select(id_input)
    rooms_select2(record)

    


    
def db_rooms_select(): 
    global stay_id_input,record

       
    w = Tk()
#     w.geometry("800x600") #사이즈창 크기
    w.title("숙소 검색 ") #창틀 타이들
#     w.configure(bg="pink")
    id_text = Label(w, text="검색할 숙소ID",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
    select = Button(w,text="검색하기",font=("궁서",30),fg="red",bg="green",command=event_process1) #버튼생성(위치지정 해줘야됨)마지막은 속성=이벤트_함수이름
    stay_id_input = Entry(w,font=("궁서",30),fg="red",bg="green", width=12) # 입력창(위치지정 해줘야됨)

      
    id_text.pack() #위치에 추가(기본 디폴트 값 있음)
    stay_id_input.pack() #입력창 추가(기본 디폴트 값 있음)
  
    select.pack() #버튼 위치에 추가(기본 디폴트 값 있음)

    w.mainloop()
    
    
def rooms_select2(record): 
#     global id_input
#     global name_input
#     global address_input
#     global tel_input
#     global score_input
 

    
     
    w = Toplevel() #이미지 사용 페이지는 Tk() 가 아닌 Toplevel() 를 사용!!!!
    w.geometry("800x750") #사이즈창 크기
    w.title("검색결과") #창틀 타이들
#     w.configure(bg="black")
    

        
    review_num_text = Label(w, text="리뷰넘버",font=("궁서",30),fg="blue",bg="red")#텍스트 생성 완료 (위치지정 해줘야됨)
    review_name_text = Label(w, text="리뷰 제목",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
    accommodation_num_text = Label(w, text="회원넘버",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
    stay_id_text = Label(w, text="숙소넘버",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
    stay_name_text = Label(w, text="숙소이름 ",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
    stay_address_text = Label(w, text="숙소주소 ",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
    stay_tel_text = Label(w, text="숙소전화번호 :",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
    stay_score_text = Label(w, text="좋아요 점수 :",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
    review_text_text = Label(w, text="리뷰 :",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
    

#     img_text = Label(w, text="포스터",font=("궁서",30),fg="blue",bg="red") #텍스트 생성 완료 (위치지정 해줘야됨)
     
      
    review_num_input = Label(w, text=record[0], font=("궁서", 30), fg="blue", bg="yellow")
    review_name_input = Label(w, text=record[1], font=("궁서", 30), fg="blue", bg="yellow")
    accommodation_num_input = Label(w, text=record[2], font=("궁서", 30), fg="blue", bg="yellow")
    stay_id_input = Label(w, text=record[3], font=("궁서", 30), fg="blue", bg="yellow")
    stay_name_input = Label(w, text=record[6], font=("궁서", 30), fg="blue", bg="yellow")
    stay_address_input = Label(w, text=record[7], font=("궁서", 30), fg="blue", bg="yellow")
    stay_tel_input = Label(w, text=record[8], font=("궁서", 30), fg="blue", bg="yellow")
    stay_score_input = Label(w, text=record[9], font=("궁서", 30), fg="blue", bg="yellow")
    review_text_input = Label(w, text=record[4], font=("궁서", 30), fg="blue", bg="yellow")

#     img_input = Label(w, text=record[4], font=("궁서", 30), fg="blue", bg="yellow")
    
    
    
#     img = PhotoImage(file=record[4])
#     img_input = Label(w, image=img) 
    
    
    
          
    review_num_text.place(x=10,y=10) #위치에 추가(기본 디폴트 값 있음)
    review_num_input.place(x=190,y=10) #입력창 추가(기본 디폴트 값 있음)
    review_name_text.place(x=10,y=60) #위치에 추가(기본 디폴트 값 있음)
    review_name_input.place(x=190,y=60) #입력창 추가(기본 디폴트 값 있음)
    accommodation_num_text.place(x=10,y=110) #위치에 추가(기본 디폴트 값 있음)
    accommodation_num_input.place(x=190,y=110) #입력창 추가(기본 디폴트 값 있음)
    stay_id_text.place(x=10,y=160) #위치에 추가(기본 디폴트 값 있음)
    stay_id_input.place(x=190,y=160) #입력창 추가(기본 디폴트 값 있음)
    stay_name_text.place(x=10,y=210) #위치에 추가(기본 디폴트 값 있음)
    stay_name_input.place(x=200,y=210) #입력창 추가(기본 디폴트 값 있음)
    stay_address_text.place(x=10,y=260) #위치에 추가(기본 디폴트 값 있음)
    stay_address_input.place(x=200,y=260) #입력창 추가(기본 디폴트 값 있음)
    stay_tel_text.place(x=10,y=310) #위치에 추가(기본 디폴트 값 있음)
    stay_tel_input.place(x=290,y=310) #입력창 추가(기본 디폴트 값 있음)
    stay_score_text.place(x=10,y=360) #위치에 추가(기본 디폴트 값 있음)
    stay_score_input.place(x=270,y=360) #입력창 추가(기본 디폴트 값 있음)
    review_text_text.place(x=10,y=420) #위치에 추가(기본 디폴트 값 있음)
    review_text_input.place(x=10,y=470) #입력창 추가(기본 디폴트 값 있음)

#     img_text.pack()
#     img_input.pack()
    
    
    
#     img_input.pack()
        
        
        

    w.mainloop()
    
if __name__ == '__main__':
    db_rooms_select()













