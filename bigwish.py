import csv
import numpy
import random
from collections import Counter

ratio_number = numpy.zeros(45)

# 1부터 45까지의 숫자를 카운트할 딕셔너리 생성
count_dict = {i: 0 for i in range(1, 46)}

# 'newlo.csv' 파일 읽기
with open('numhistory.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        # 각 행의 숫자들을 확인하여 카운트 증가
        for num in row:
            num = num.strip('\ufeff')  # BOM 문자 제거
            try:
                count_dict[int(num)]+= 1
            except ValueError:
                pass  # 숫자로 변환할 수 없는 경우 무시

total_count = sum(count_dict.values())
print()
print('***** Version 3(2024/01/26) *****')
print(f'누적Data : 총 {total_count/6}회, {total_count}번 발생')

# 결과 출력
line = 0
for num, count in count_dict.items():
    print(f'{num}:{count}번') #번호별 몇번 나왔는지 프린트
    ratio_number[num-1] = count/total_count
    #print(ratio_number[num-1])
#print(ratio_number) #Ratio 확인용 출력

#for i in range(1, 6):
#    print(random.choices(range(1,46), weights=[ratio_number[0],ratio_number[1],ratio_number[2],ratio_number[3],ratio_number[4],ratio_number[5],ratio_number[6],ratio_number[7],ratio_number[8],ratio_number[9],ratio_number[10],ratio_number[11],ratio_number[12],ratio_number[13],ratio_number[14],ratio_number[15],ratio_number[16],ratio_number[17],ratio_number[18],ratio_number[19],ratio_number[20],ratio_number[21],ratio_number[22],ratio_number[23],ratio_number[24],ratio_number[25],ratio_number[26],ratio_number[27],ratio_number[28],ratio_number[29],ratio_number[30],ratio_number[31],ratio_number[32],ratio_number[33],ratio_number[34],ratio_number[35],ratio_number[36],ratio_number[37],ratio_number[38],ratio_number[39],ratio_number[40],ratio_number[41],ratio_number[42],ratio_number[43],ratio_number[44] ], k=6 ))

#for i in range(1, 6):
#    selected_numbers = random.choices(range(1, 46), weights=ratio_number, k=6)
#    print(selected_numbers)

for i in range(1, 6):
    selected_numbers = []
    for _ in range(150):
        selected_numbers.extend(random.choices(range(1, 46), weights=ratio_number, k=6))

    counter = Counter(selected_numbers)
    #print(counter) #숫자별 몇번 나왔나 보기위함
    #most_common = counter.most_common(6) #Rank 1~6일때 사용
    #most_common_numbers = [num for num, count in most_common] #Rank 1~6일때 사용
    most_common = counter.most_common() #Rank 1~3 & 43~45일때 사용
    most_common_numbers = [num for num, count in most_common] #Rank 1~3 & 43~45일때 사용
    most_common_numbers = most_common_numbers[:3]+most_common_numbers[-3:] #Rank 1~3 & 43~45일때 사용
    print(most_common_numbers)
print('*********************************')