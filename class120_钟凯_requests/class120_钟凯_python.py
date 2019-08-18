


def avg_group(studens_num,group_num):
    a = []
    for i in range(group_num):
        a.append(0)
    while studens_num >0:
       for i in  range(group_num):
           if studens_num>=1:
               a[i]+=1
               studens_num -=1


    print(a)




if __name__ == '__main__':
    students_num =9
    group_num = 4
    avg_group(students_num,group_num)
