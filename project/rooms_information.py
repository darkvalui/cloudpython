from tkinter import *
from tkinter.messagebox import *
import pymysql
from project import rooms_crud
from PyQt5.Qt import left



stay_id_input,stay_name_input,stay_address_input,stay_tel_input,stay_score_input,record,record_review,review_name,accommodation_num,stay_id,review_text= None,None,None,None,None,None,None,None,None,None,None

# room_img=None

def event_process1():
#     global stay_id_input
    print("주소검색")
    id_input = stay_id_input.get()
    rooms_crud.db_rooms_select(id_input)
    record,record_review=rooms_crud.db_rooms_select(id_input)
    
    rooms_select2(record,record_review)


def event_process2():
    review_name = name_input.get()
    accommodation_num = num_input.get()
    stay_id = id_input.get()
    review_text = text_input.get()
    rooms_crud.review_input(review_name,accommodation_num,stay_id,review_text)
    showinfo("완료", "게시글 등록 완료")
    


    
def db_rooms_select(): #숙소 ID 검색
    global stay_id_input,record

       
    w = Tk()
    w.title("숙소 검색 ")
    id_text = Label(w, text="검색할 숙소ID",font=("궁서",30),fg="blue",bg="red") 
    select = Button(w,text="검색하기",font=("궁서",30),fg="red",bg="green",command=event_process1)  
    stay_id_input = Entry(w,font=("궁서",30),fg="red",bg="green", width=12) 
      
    id_text.pack() #위치에 추가(기본 디폴트 값 있음)
    stay_id_input.pack() #입력창 추가(기본 디폴트 값 있음)
    select.pack() #버튼 위치에 추가(기본 디폴트 값 있음)

    w.mainloop()
    
    
    
    
    
    
def rooms_select2(record,record_review):  
    global name_input
    global num_input
    global id_input
    global text_input


    print(record)
  

    
    w = Toplevel() #이미지 사용 페이지는 Tk() 가 아닌 Toplevel() 를 사용!!!!
    w.geometry("1500x750") 
    w.title("검색결과")
    
    

    
    stay_name_text = Label(w, text="숙소이름 ",font=("궁서",30),fg="blue",bg="red") 
    stay_address_text = Label(w, text="숙소주소 ",font=("궁서",30),fg="blue",bg="red") 
    stay_tel_text = Label(w, text="숙소전화번호 :",font=("궁서",30),fg="blue",bg="red") 
    stay_score_text = Label(w, text="좋아요 점수 :",font=("궁서",30),fg="blue",bg="red") 
    review_text_text = Label(w, text="리뷰 :",font=("궁서",30),fg="blue",bg="red")

    stay_name_input = Label(w, text=record[0], font=("궁서", 30), fg="blue", bg="yellow")
    stay_address_input = Label(w, text=record[1], font=("궁서", 30), fg="blue", bg="yellow")
    stay_tel_input = Label(w, text=record[2], font=("궁서", 30), fg="blue", bg="yellow")
    stay_score_input = Label(w, text=record[3], font=("궁서", 30), fg="blue", bg="yellow")
    
#==========================================================================================
    name_text = Label(w, text="제목",font=("궁서",30),fg="blue",bg="red") 
    num_text = Label(w, text="회원ID",font=("궁서",30),fg="blue",bg="red") 
    id_text = Label(w, text="숙소ID",font=("궁서",30),fg="blue",bg="red") 
    text_text = Label(w, text="리뷰네용",font=("궁서",30),fg="blue",bg="red") 
    insert = Button(w,text="등록하기",font=("궁서",30),fg="red",bg="green",command=event_process2) 
     
       
    name_input = Entry(w,font=("궁서",30),fg="red",bg="green", width=12) 
    num_input = Entry(w,font=("궁서",30),fg="red",bg="green", width=12) 
    id_input = Entry(w,font=("궁서",30),fg="red",bg="green", width=12) 
    text_input = Entry(w,font=("궁서",30),fg="red",bg="green", width=12) 
         
           
    name_text.place(x=900,y=210)  
    name_input.place(x=900,y=260)
    num_text.place(x=900,y=310)
    num_input.place(x=900,y=360)
    id_text.place(x=900,y=410)
    id_input.place(x=900,y=460)
    text_text.place(x=900,y=510) 
    text_input.place(x=900,y=560)
    insert.place(x=900,y=610) #버튼 위치에 추가(기본 디폴트 값 있음)
#==========================================================================================
    stay_name_text.place(x=10,y=210) 
    stay_name_input.place(x=200,y=210) 
    stay_address_text.place(x=10,y=260) 
    stay_address_input.place(x=200,y=260) 
    stay_tel_text.place(x=10,y=310) 
    stay_tel_input.place(x=290,y=310) 
    stay_score_text.place(x=10,y=360) 
    stay_score_input.place(x=270,y=360) 
    review_text_text.place(x=10,y=420) 
    
#==========================================================================================
    print(record_review)
    review2=list(record_review)   
    
    frame1 = Frame(w)
    frame1.place(x = 10, y = 470)
    for i in range(0, len(review2)):
        review_text_input = Label(frame1, text = "제목  :"+review2[i][0])
        review_text_input.pack()
        review_text_content = Label(frame1, text = "    └ 내용 :"+review2[i][1])
        review_text_content.pack()

        
        

    w.mainloop()
    
if __name__ == '__main__':
    db_rooms_select()













