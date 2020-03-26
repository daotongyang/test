import string
import time
import random

def random_time():
    a1 = (2019,12,1,0,0,0,0,0,0)
    a2 = (2020,3,18,23,59,59,0,0,0)
    #生成时间戳
    start=time.mktime(a1)    
    end=time.mktime(a2)      

    #随机生成10个日期字符串
    for i in range(10):
        t=random.randint(start,end)            
        date_touple=time.localtime(t)          
        date=time.strftime("%Y-%m-%d",date_touple)  
        return date
        

def random_str(length=1):
    template = string.ascii_letters + string.digits
    
    chars = random.sample(template, length)
    return "".join(chars)

def generate_record():
    
    st_id = random.randint(201771030000, 201771033000)
  
    name = str(random.randint(0, 2000))  
    heat= random.choice(['Y', 'N'])
    at_school= random.choice(['Y', 'N'])
    huobei= random.choice(['Y', 'N'])
    wuhan= random.choice(['Y', 'N'])
    at_huobei= random.choice(['Y', 'N'])
    at_wuhan= random.choice(['Y', 'N'])
    meet_disease_area_people= random.choice(['Y', 'N'])
    arrive_school= random.choice(['Y', 'N'])
    arrive_school_time = random_time() 
    
    return [st_id,name,heat, at_school,huobei,wuhan, at_huobei,at_wuhan,meet_disease_area_people,arrive_school,arrive_school_time]

def create_file(num=2000):
    with open("user_data1.txt", "w") as f:
        for i in range(num):
            row = generate_record()
            f.write(",".join(map(str, row))+"\n")

if __name__ == '__main__':
    import datetime
    start = datetime.datetime.now()
    create_file()
    end = datetime.datetime.now()
    cost = (end -start).total_seconds()
    print("cost: %s" % cost)







    
