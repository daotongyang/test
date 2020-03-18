import pymysql
from matplotlib import pyplot as plt
import matplotlib

#实现菜单
def menu():
    print('*******************************************************************************************************')
    print('*                                                                     1.按姓名查询                                                               *')
    print('*                                                                     2.按学号查询                                                               *')
    print('*                                                                     3.按学号和时间查询                                                     *')
    print('*                                                                     4.按周查询总体                                                            *')
    print('*                                                                     5.按月查询总体                                                            *')
    #print('*                                                                     6.添加人员                                                                   *')
    #print('*                                                                     7.删除人员                                                                   *')
    print('*                                                                     111.退出系统                                                               *')
    print('********************************************************************************************************')

def init():
    menu()
    kind = int(input("请输入指令："))
    return kind

#按姓名查询
def search_by_name(st_name):
    # 打开数据库连接
    db = pymysql.connect("localhost","root","lb666666","user1" )
 
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询 
    sql = "SELECT * FROM  STUDENTS WHERE name = '%s'  " % (st_name)
    
    try:
        # 执行SQL语句
        cursor.execute(sql)
        
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            st_id = row[0]
            st_name = row[1]
            st_heat = row[2]
            st_at_school = row[3]
            st_huobei = row[4]
            st_wuhan = row[5]
            st_at_huobei = row[6]
            st_at_wuhan = row[7]
            st_disaster = row[8]
            st_arrive_school = row[9]
            st_time = row[10]

        print("学号： ", st_id)
        print("姓名：", st_name)
        print("是否发热：", st_heat )
        print("是否留校：", st_at_school)
        print("是否为湖北籍：", st_huobei)
        print("是否为武汉籍：", st_wuhan)
        print("是否在湖北：", st_at_huobei)
        print("是否在武汉：", st_at_wuhan)
        print("是否与疫区人员接触：", st_disaster)
        print("是否返校：", st_arrive_school)
        print("签到时间：", st_time)
        
        #break
    except:
        print ("Error: unfind name!")
 
    # 关闭数据库连接
    db.close()

#按学号查询
def search_by_id(st_id):
    # 打开数据库连接
    #print(st_name)

    db = pymysql.connect("localhost","root","lb666666","user1" )
 
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询 
    sql = "SELECT * FROM  STUDENTS WHERE id = '%s'  " % (st_id)
    
    #print(st_name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            st_id = row[0]
            st_name = row[1]
            st_heat = row[2]
            st_at_school = row[3]
            st_huobei = row[4]
            st_wuhan = row[5]
            st_at_huobei = row[6]
            st_at_wuhan = row[7]
            st_disaster = row[8]
            st_arrive_school = row[9]
            st_time = row[10]

            print("学号： ", st_id)
            print("姓名：", st_name)
            print("是否发热：", st_heat )
            print("是否留校：", st_at_school)
            print("是否为湖北籍：", st_huobei)
            print("是否为武汉籍：", st_wuhan)
            print("是否在湖北：", st_at_huobei)
            print("是否在武汉：", st_at_wuhan)
            print("是否与疫区人员接触：", st_disaster)
            print("是否返校：", st_arrive_school)
            print("签到时间：", st_time)
            
    except:
        print ("Error: unfind name!")
 
    # 关闭数据库连接
    db.close()


def search_by_idAndtime(st_id, st_time):

    # 打开数据库连接
    #print(st_name)

    db = pymysql.connect("localhost","root","lb666666","user1" )
 
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询 
    sql = "SELECT * FROM  STUDENTS WHERE DATE_FORMAT(arrive_school_time, '%%Y-%%m-%%d') = '%s' and  id = '%s' " % (st_time, st_id)
    
    try:
        # 执行SQL语句
        cursor.execute(sql)
        
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            st_id = row[0]
            st_name = row[1]
            st_heat = row[2]
            st_at_school = row[3]
            st_huobei = row[4]
            st_wuhan = row[5]
            st_at_huobei = row[6]
            st_at_wuhan = row[7]
            st_disaster = row[8]
            st_arrive_school = row[9]
            st_time = row[10]

            print("学号： ", st_id)
            print("姓名：", st_name)
            print("是否发热：", st_heat )
            print("是否留校：", st_at_school)
            print("是否为湖北籍：", st_huobei)
            print("是否为武汉籍：", st_wuhan)
            print("是否在湖北：", st_at_huobei)
            print("是否在武汉：", st_at_wuhan)
            print("是否与疫区人员接触：", st_disaster)
            print("是否返校：", st_arrive_school)
            print("签到时间：", st_time)
            
    except:
        print ("Error: unfind name!")
 
    # 关闭数据库连接
    db.close()


def search_by_weekend(st_weekend):
    
    # 打开数据库连接
    db = pymysql.connect("localhost","root","lb666666","user1" )
 
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    sql = [ ]
    #s0是周的统计人数
    s0=  "SELECT COUNT(*) FROM STUDENTS \
            WHERE DATE_FORMAT(arrive_school_time, '%%Y-%%u')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%u') " % (st_weekend)
    sql.append(s0)    
    
    s1=  "SELECT COUNT(*) FROM STUDENTS \
            WHERE heat='N' and DATE_FORMAT(arrive_school_time, '%%Y-%%u')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%u') and heat='N' " % (st_weekend)
    sql.append(s1)

    s2 =  "SELECT COUNT(*) FROM STUDENTS \
            WHERE at_school = 'N' and DATE_FORMAT(arrive_school_time, '%%Y-%%u')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%u') " % (st_weekend)
    sql.append(s2)
    s3 =  "SELECT COUNT(*) FROM STUDENTS \
            WHERE at_huobei = 'N' and DATE_FORMAT(arrive_school_time, '%%Y-%%u')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%u') " % (st_weekend)
    sql.append(s3)
    s4 =  "SELECT COUNT(*) FROM STUDENTS \
            WHERE at_wuhan = 'N' and DATE_FORMAT(arrive_school_time, '%%Y-%%u')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%u') " % (st_weekend)
    sql.append(s4)
    
    s5 =  "SELECT COUNT(*) FROM STUDENTS \
            WHERE meet_disease_area_people = 'N' and DATE_FORMAT(arrive_school_time, '%%Y-%%u')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%u') " % (st_weekend)
    sql.append(s5)
    
    try:
        # 执行SQL语句
        results = [ ]
        for i in range(0,len(sql)):
            result = 0
            cursor.execute(sql[i])
            result = cursor.fetchone()
            #print(result)
            results.append(result)
        return results
    except:
        print ("Error: unfind!")
 
    # 关闭数据库连接
    db.close()


def search_by_month(st_month):
    db = pymysql.connect("localhost","root","lb666666","user1" )
 
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    sql = [ ]
    #s0是周的统计人数
    s0=  "SELECT COUNT(*) FROM STUDENTS \
            WHERE DATE_FORMAT(arrive_school_time, '%%Y-%%m')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%m') " % (st_month)
    sql.append(s0)    
    
    s1=  "SELECT COUNT(*) FROM STUDENTS \
            WHERE heat='N' and DATE_FORMAT(arrive_school_time, '%%Y-%%m')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%m') and heat='N' " % (st_month)
    sql.append(s1)

    s2 =  "SELECT COUNT(*) FROM STUDENTS \
            WHERE at_school = 'N' and DATE_FORMAT(arrive_school_time, '%%Y-%%m')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%m') " % (st_month)
    sql.append(s2)
    s3 =  "SELECT COUNT(*) FROM STUDENTS \
            WHERE at_huobei = 'N' and DATE_FORMAT(arrive_school_time, '%%Y-%%m')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%m') " % (st_month)
    sql.append(s3)
    s4 =  "SELECT COUNT(*) FROM STUDENTS \
            WHERE at_wuhan = 'N' and DATE_FORMAT(arrive_school_time, '%%Y-%%m')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%m') " % (st_month)
    sql.append(s4)
    
    s5 =  "SELECT COUNT(*) FROM STUDENTS \
            WHERE meet_disease_area_people = 'N' and DATE_FORMAT(arrive_school_time, '%%Y-%%m')='%s' \
            GROUP BY DATE_FORMAT(arrive_school_time, '%%Y-%%m') " % (st_month)
    sql.append(s5)
   
    try:
        # 执行SQL语句
        results = [ ]
        for i in range(0,len(sql)):
            cursor.execute(sql[i])
            result = cursor.fetchone()
            results.append(result)
        return results
    except:
        print ("Error: unfind!")
 
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    kind = init()
    while True:
        if kind == 111:
            exit()
        elif kind == 1:
            st_name = input("请输入姓名: ")
            search_by_name(st_name)
            kind = int(input("按111退出: "))
            if kind == 111:
                exit()
            kind = init()
                
        elif kind == 2:
            st_id = input("请输入学号: ")
            search_by_id(st_id)
            kind = int(input("按111退出: "))
            if kind == 111:
                exit()
            kind = init()
            
        elif kind == 3:
            st_id = input("请输入学号: ")
            st_time = input("请输入时间：")
            search_by_idAndtime(st_id, st_time)
            kind = int(input("按111退出: "))
            if kind == 111:
                exit()
            kind = init()
    
        elif kind == 4:
            st_weekend = input("请输入'年-周'：")
            results = search_by_weekend(st_weekend)
            r=[ ]
            ry=[ ]
            rn=[ ]
            t = len(results)
            n = [ ]
            n = results[0]
            q = n[0]
            print("该周点到人数：", q)
            for i in range(1, t):
                r = results[i]
                rn.append(r[0])
                ry.append(q-r[0])

            # 设置中文字体和负号正常显示
            matplotlib.rcParams['font.sans-serif'] = ['SimHei']
            matplotlib.rcParams['axes.unicode_minus'] = False

            label_list = ['heat', 'at_school', 'at_huobei', 'at_wuhan','meet_dap']    # 横坐标刻度显示值
            num_list1 = ry      # 纵坐标值1
            num_list2 = rn      # 纵坐标值2

            m = range(len(num_list1))
                
            """
            绘制条形图
            x:长条形中点横坐标
            height:长条形高度
            width:长条形宽度，默认值0.8
            label:为后面设置legend准备
            """
            rects1 = plt.bar(x=m, height=num_list1, width=0.4, alpha=0.8, color='red', label="Yes")
            rects2 = plt.bar(x=[i + 0.4 for i in m], height=num_list2, width=0.4, color='green', label="No")
            plt.ylim(0, 20)     # y轴取值范围
            plt.ylabel("数量")
            """
            设置x轴刻度显示值
            参数一：中点坐标
            参数二：显示值
            """
            plt.xticks([index + 0.2 for index in m], label_list)
            plt.xlabel("类型")
            plt.title("周统计图")
            plt.legend()     # 设置题注
            # 编辑文本
            for rect in rects1:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
            for rect in rects2:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
            plt.show()
            kind = int(input("按111退出: "))
            if kind == 111:
                exit()
            kind = init()
                      
        elif  kind == 5:
            st_month = input("请输入'年-月'：")
            results = search_by_month(st_month)
            r=[ ]
            ry=[ ]
            rn=[ ]
            t = len(results)
            n = [ ]
            n = results[0]
            q = n[0]
            print("该月点到人数：", q)
            for i in range(1, t):
                r = results[i]
                rn.append(r[0])
                ry.append(q-r[0])
                    
            # 设置中文字体和负号正常显示
            matplotlib.rcParams['font.sans-serif'] = ['SimHei']
            matplotlib.rcParams['axes.unicode_minus'] = False

            label_list = ['heat', 'at_school', 'at_huobei', 'at_wuhan','meet_dap']    # 横坐标刻度显示值
            num_list1 = ry      # 纵坐标值1
            num_list2 = rn      # 纵坐标值2

            m = range(len(num_list1))
                
            """
            绘制条形图
            x:长条形中点横坐标
            height:长条形高度
            width:长条形宽度，默认值0.8
            label:为后面设置legend准备
            """
            rects1 = plt.bar(x=m, height=num_list1, width=0.4, alpha=0.8, color='red', label="Yes")
            rects2 = plt.bar(x=[i + 0.4 for i in m], height=num_list2, width=0.4, color='green', label="No")
            plt.ylim(0, 20)     # y轴取值范围
            plt.ylabel("数量")
            """
            设置x轴刻度显示值
            参数一：中点坐标
            参数二：显示值
            """
            plt.xticks([index + 0.2 for index in m], label_list)
            plt.xlabel("类型")
            plt.title("月统计图")
            plt.legend()     # 设置题注
            # 编辑文本
            for rect in rects1:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
            for rect in rects2:
                height = rect.get_height()
                plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
            plt.show()
            kind = int(input("按111退出: "))
            if kind == 111:
                exit()
            kind = init()
    
