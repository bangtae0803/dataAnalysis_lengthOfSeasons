import pandas as pd
import matplotlib.pyplot as plt
import csv

Weather_Data = pd.read_csv('Weather_Data.csv', names=['date', 'location', 'avg','low', 'high'],encoding='CP949')
 
date=Weather_Data['date']
date_val=date.values
date_list=date_val.tolist()  #날짜 데이터 리스트

avg= Weather_Data['avg']
avg_val=avg.values
avg_list=avg_val.tolist() #평균 기온 데이터 리스트

period_spring=[]  #20년 간의 봄 길이 리스트
period_summer=[] #20년 간의 여름 길이 리스트
period_fall=[] #20년 간의 가을 길이 리스트
period_winter=[] #20년 간의 겨울 길이 리스트 (단, 분석에 사용한 데이터는 20020101~20211231의 데이터로 겨울은 총 19번 나타납니다.)

avg_spring=[] #20년 간의 봄의 평균 기온 리스트
avg_summer=[] #20년 간의 여름의 평균 기온 리스트
avg_fall=[] #20년 간의 가을의 평균 기온 리스트
avg_winter=[] #20년 간의 가을의 평균 기온 리스트 (단, 분석에 사용한 데이터는 20020101~20211231의 사이의 데이터로 겨울은 총 19번 나타납니다.)


i=1
point=[] #계절 변화 시작 지점 리스트

str_year=[] #리스트에 추가하기 위해 str 타입 리스트 생성
for t in range(2002,2022):
    t=str(t)
    str_year.append(t)


def spring(): #봄 시작 지점 탐색 함수
    global i    
    
    while(i<=len(date_list)-9) :
        if float(avg_list[i])>=5.0\
           and float(avg_list[i+1])>=5.0\
                    and float(avg_list[i+2])>=5.0\
                        and float(avg_list[i+3])>=5.0\
                            and float(avg_list[i+4])>=5.0\
                                and float(avg_list[i+5])>=5.0\
                                    and float(avg_list[i+6])>=5.0\
                                        and float(avg_list[i+7])>=5.0\
                                            and float(avg_list[i+8])>=5.0 :
                                            point.append(i)
                                            i+=1
                                            return i
                                            break
                   
        else: i+=1
                                              
def summer(): #여름 시작 지점 탐색 함수
    global i
    
    while(i<=len(date_list)-9) :
        if float(avg_list[i])>=20.0\
           and float(avg_list[i+1])>=20.0\
                    and float(avg_list[i+2])>=20.0\
                        and float(avg_list[i+3])>=20.0\
                            and float(avg_list[i+4])>=20.0\
                                and float(avg_list[i+5])>=20.0\
                                    and float(avg_list[i+6])>=20.0\
                                        and float(avg_list[i+7])>=20.0\
                                            and float(avg_list[i+8])>=20.0 :
                                            point.append(i)
                                            i+=1
                                            return i
                                            break
                
        else: i+=1

def fall(): #가을 시작 지점 탐색 함수
    global i 

    while(i<=len(date_list)-9) :
        if float(avg_list[i])<20.0\
           and float(avg_list[i+1])<20.0\
                    and float(avg_list[i+2])<20.0\
                        and float(avg_list[i+3])<20.0\
                            and float(avg_list[i+4])<20.0\
                                and float(avg_list[i+5])<20.0\
                                    and float(avg_list[i+6])<20.0\
                                        and float(avg_list[i+7])<20.0\
                                            and float(avg_list[i+8])<20.0 :
                                            point.append(i)
                                            i+=1
                                            return i
                                            break
            
        else: i+=1

def winter(): #겨울 시작 지점 탐색 함수
    global i
    
    while(i<=len(date_list)-9) :
        if float(avg_list[i])<5.0\
           and float(avg_list[i+1])<5.0\
                    and float(avg_list[i+2])<5.0\
                        and float(avg_list[i+3])<5.0\
                            and float(avg_list[i+4])<5.0\
                                and float(avg_list[i+5])<5.0\
                                    and float(avg_list[i+6])<5.0\
                                        and float(avg_list[i+7])<5.0\
                                            and float(avg_list[i+8])<5.0 :
                                            point.append(i)
                                            i+=1
                                            return i
                                            break
                       
        else: i+=1

def length_graph(season): #season을 인수로 받아 해당 계절의 길이 그래프 생성
    if season=='spring':
        plt.title('The length of spring')
        plt.xlabel('Year')
        plt.ylabel('Length')
        plt.plot(year,period_spring,color='green', marker='o', markerfacecolor='green', markersize=6)
        plt.xticks(year)
        plt.show()
    elif season=='summer':
        plt.title('The length of summer')
        plt.xlabel('Year')
        plt.ylabel('Length')
        plt.plot(year,period_summer,color='green', marker='o', markerfacecolor='green', markersize=6)
        plt.xticks(year)
        plt.show()
    elif season=='fall':
        plt.title('The length of fall')
        plt.xlabel('Year')
        plt.ylabel('Length')
        plt.plot(year,period_fall,color='green', marker='o', markerfacecolor='green', markersize=6)
        plt.xticks(year)
        plt.show()
    elif season=='winter':
        del year[19] #겨울의 데이터는 2020년까지만 있기 때문에 임시로 2021년을 삭제해준다.
        plt.title('The length of winter')
        plt.xlabel('Year')
        plt.ylabel('Length')
        plt.plot(year,period_winter,color='green', marker='o', markerfacecolor='green', markersize=6)
        plt.xticks(year)
        plt.show()
        year.append(2021) #임시로 2021을 삭제해주었기 때문에 다시 추가해준다.

def avg_graph(season): #season을 인수로 받아 해당 계절의 평균 기온 그래프 생성
    if season=='spring':
        plt.title('The average temperature of spring')
        plt.xlabel('Year')
        plt.ylabel('Average Temperature')
        plt.plot(year,avg_spring,color='green', marker='o', markerfacecolor='green', markersize=6)
        plt.xticks(year)
        plt.show()
    elif season=='summer':
        plt.title('The average temperature of summer')
        plt.xlabel('Year')
        plt.ylabel('Average Temperature')
        plt.plot(year,avg_summer,color='green', marker='o', markerfacecolor='green', markersize=6)
        plt.xticks(year)
        plt.show()
    elif season=='fall':
        plt.title('The average temperature of fall')
        plt.xlabel('Year')
        plt.ylabel('Average Temperature')
        plt.plot(year,avg_fall,color='green', marker='o', markerfacecolor='green', markersize=6)
        plt.xticks(year)
        plt.show()
    elif season=='winter':
        del year[19] #겨울의 데이터는 2020년까지만 있기 때문에 임시로 2021년을 삭제해준다.
        plt.title('The average temperature of winter')
        plt.xlabel('Year')
        plt.ylabel('Average Temperature')
        plt.plot(year,avg_winter,color='green', marker='o', markerfacecolor='green', markersize=6)
        plt.xticks(year)
        plt.show()
        year.append(2021) #임시로 2021을 삭제해주었기 때문에 다시 추가해준다.



for year in range(2002,2022) : #2002년부터 2021년까지 각 계절의 시작 지점 탐색
   
    spring()
    summer()
    fall()
    winter()

for l in range(0,len(point)-1):
    if l%4==0 :  #봄 길이 구하기
        period_spring.append(int(point[l+1]-point[l]))
    elif l%4==1 :  #여름 길이 구하기
        period_summer.append(int(point[l+1]-point[l]))
    elif l%4==2 :  #가을 길이 구하기
        period_fall.append(point[l+1]-point[l])
    else :  #겨울 길이 구하기
        period_winter.append(point[l+1]-point[l])

temp_year=['연도'] #csv 파일 작성을 위한 임시 리스트 생성
temp_spring=['봄 길이(일)'] #csv 파일 작성을 위한 임시 리스트 생성
temp_summer=['여름 길이(일)'] #csv 파일 작성을 위한 임시 리스트 생성
temp_fall=['가을 길이(일)'] #csv 파일 작성을 위한 임시 리스트 생성
temp_winter=['겨울 길이(일)'] #csv 파일 작성을 위한 임시 리스트 생성

temp_year.extend(str_year)
temp_spring.extend(period_spring)
temp_summer.extend(period_summer)
temp_fall.extend(period_fall)
temp_winter.extend(period_winter)

length_data = [
    temp_year,
    temp_spring,
    temp_summer,
    temp_fall,
    temp_winter
]
 
f = open("length_data.csv", "w")
writer = csv.writer(f) 
for row in length_data: #연도별 각 계절 일 수 csv 파일로 작성
    writer.writerow(row) 
f.close()


print("봄 길이(일):", end=' ')
print(period_spring)
print("여름 길이(일):", end=' ')
print(period_summer)
print("가을 길이(일):", end=' ')
print(period_fall)
print("겨울 길이(일):", end=' ')
print(period_winter)
print("")


for l in range(0,len(point)-1):
    sum=0
    if l%4==0 :  #봄 평균 기온 구하기
        for m in range(point[l], point[l+1]):
            sum+=float(avg_list[m])
        avg_spring.append(round(sum/(point[l+1]-point[l]),2))    
    elif l%4==1 :  #여름 평균 기온 구하기
        for m in range(point[l], point[l+1]):
            sum+=float(avg_list[m])
        avg_summer.append(round(sum/(point[l+1]-point[l]),2))
    elif l%4==2 :  #가을 평균 기온 구하기
        for m in range(point[l], point[l+1]):
            sum+=float(avg_list[m])
        avg_fall.append(round(sum/(point[l+1]-point[l]),2))
    else :  #겨울 평균 기온 구하기
        for m in range(point[l], point[l+1]):
            sum+=float(avg_list[m])
        avg_winter.append(round(sum/(point[l+1]-point[l]),2))

year=[]
for i in range(2002,2022):
    i=int(i)
    year.append(i)

print("봄 평균 기온(˚C):", end=' ')
print(avg_spring)
print("여름 평균 기온(˚C):", end=' ')
print(avg_summer)
print("가을 평균 기온(˚C):", end=' ')
print(avg_fall)
print("겨울  평균 기온(˚C):", end=' ')
print(avg_winter)


length_graph('spring')
length_graph('summer')
length_graph('fall')
length_graph('winter')

avg_graph('spring')
avg_graph('summer')
avg_graph('fall')
avg_graph('winter')

''' 모든 계절들의 시작 날짜 출력
for m in point: 
    print(date_list[m])
'''

temp_year=['연도'] #csv 파일 작성을 위한 임시 리스트 생성
temp_spring=['봄 평균 기온(˚C)'] #csv 파일 작성을 위한 임시 리스트 생성
temp_summer=['여름 평균 기온(˚C)'] #csv 파일 작성을 위한 임시 리스트 생성
temp_fall=['가을 평균 기온(˚C)'] #csv 파일 작성을 위한 임시 리스트 생성
temp_winter=['겨울 평균 기온(˚C)'] #csv 파일 작성을 위한 임시 리스트 생성

temp_year.extend(str_year)
temp_spring.extend(avg_spring)
temp_summer.extend(avg_summer)
temp_fall.extend(avg_fall)
temp_winter.extend(avg_winter)

avg_data = [
    temp_year,
    temp_spring,
    temp_summer,
    temp_fall,
    temp_winter
]
 
f = open("avg_data.csv", "w")
writer = csv.writer(f) 
for row in avg_data: #연도별 각 계절 평균 기온 csv 파일로 작성
    writer.writerow(row) 
f.close()


