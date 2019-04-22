import pymysql


    
def db_rooms_select(stay_id_input): 
      
    #해당 숙소 정보 db처리
    con = pymysql.connect(host = 'localhost', user='root',password='1234', db='rooms')
    cur = con.cursor()
    sql="select stay_name,stay_address,stay_tel,stay_score  from data where data.stay_id=("+stay_id_input+")"
    result=cur.execute(sql) 
    record = cur.fetchone() 
    

  
  
   
    #해당 숙소 리뷰 db처리
    con2 = pymysql.connect(host = 'localhost', user='root',password='1234', db='rooms')
    cur2 = con2.cursor()
    sql2="select review_name,review_text from review where review.stay_id =("+stay_id_input+")"
    result2=cur2.execute(sql2)
    record_review = cur2.fetchall()     
  
    con2.commit()
    con2.close()
      

    return record, record_review




def review_input(review_name,accommodation_num,stay_id_input,review_text):

    con = pymysql.connect(host = 'localhost', user='root',password='1234', db='rooms') #인증받기
    cur = con.cursor()
    #3.sql 문 만들어서 -> 전송 insert into review values(null,'바보산들','바보여','1','진짜 최악3')
    sql="insert into review(review_name, accommodation_num, stay_id, review_text) values('"+review_name+"','"+accommodation_num+"','"+stay_id_input+"','"+review_text+"')"
    cur.execute(sql)
    con.commit()
    
    #4.db 연결해제
    con.close()
    
    
    
    
    
def like_input(a):

    con = pymysql.connect(host = 'localhost', user='root',password='1234', db='rooms') #인증받기
    cur = con.cursor()
    #3.sql 문 만들어서 -> 전송 insert into review values(null,'바보산들','바보여','1','진짜 최악3')
    sql="select stay_score from data where stay_id =("+a+")"
    cur.execute(sql)
    like_count=cur.fetchone()

    like_count2=list(like_count)

    b=int(like_count2[0])+1

    c=str(b)
      

    con2 = pymysql.connect(host = 'localhost', user='root',password='1234', db='rooms') #인증받기
    cur2 = con.cursor()
    sql="update data set stay_score=('"+c+"') where stay_id =("+a+")"
    cur2.execute(sql)
 
    con.commit()
    con.close()
    con2.commit()
    con2.close()

    
    

    
#     con2 = pymysql.connect(host = 'localhost', user='root',password='1234', db='rooms') #인증받기
#     cur = con.cursor()
#     sql="select stay_score from data where stay_id =("+a+")"

    

     
# if __name__ == '__main__':
#  
#      
#      
#     a=input()
#     like_input(a)
    
    
#     stay_id_input = input("검색할 주소: ")
#     db_rooms_select(stay_id_input)
#      
#     print("====================================")
#     review_name = input("리뷰 제목: ")
#     accommodation_num = input("회원 이름: ")
#     stay_id_input = input("숙소 id: ")
#     review_text = input("리뷰내용: ")
#     review_input(review_name,accommodation_num,stay_id_input,review_text)