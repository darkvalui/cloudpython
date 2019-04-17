import pymysql


    
def db_rooms_select(stay_id_input):
    con = pymysql.connect(host = 'localhost', user='root',password='1234', db='rooms')
    cur = con.cursor()
    print("db접근")
    sql="select review.*, data.* from data,review where review.stay_id =("+stay_id_input+")"
    result=cur.execute(sql)
    print(result)
 
     
    record = cur.fetchone() 
    print("review_num :",record[0])
    print("review_name :",record[1])
    print("accommodation_num :",record[2])
    print("stay_id :",record[3])
    print("review_text :",record[4])
    print("stay_id :",record[5])
    print("stay_name :",record[6])
    print("stay_address :",record[7])
    print("stay_tel :",record[8])
    print("stay_score :",record[9])

    con.commit()
    con.close()
    print("완료,db 연결해제")
    return record



# def db_review_text(stay_id_input):
#     con = pymysql.connect(host = 'localhost', user='root',password='1234', db='rooms')
#     cur = con.cursor()
#     print("db접근")
#     sql="review_text from review where review.stay_id =("+stay_id_input+")"
#     result=cur.execute(sql)
#     print(result)
#  
#      
#     record = cur.fetchone() 
#     print("review_num :",record[0])
#     print("review_name :",record[1])
#     print("accommodation_num :",record[2])
#     print("stay_id :",record[3])
#     print("review_text :",record[4])
#     print("stay_id :",record[5])
#     print("stay_name :",record[6])
#     print("stay_address :",record[7])
#     print("stay_tel :",record[8])
#     print("stay_score :",record[9])
# 
#     con.commit()
#     con.close()
#     print("완료,db 연결해제")
#     return record



    
     
     
     
if __name__ == '__main__':
    stay_id_input = input("검색할 주소: ")
    db_rooms_select(stay_id_input)
#     db_review_text(stay_id_input)


