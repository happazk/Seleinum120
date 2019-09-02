job_msg = '成都-锦江区  |  2年经验  |  本科  |  招2人  |  08-20发布'
if job_msg.find('招'):
    start_pos = job_msg.find('招')
    end_pos = job_msg.index('|', start_pos)
    end_pos = job_msg.find('人')
    people_num = job_msg[start_pos+1:end_pos]

    print(people_num)
if job_msg.find('科'):
    start_pos = job_msg.find('科')-1
    end_pos = job_msg.index('|',start_pos)
    people_num = job_msg[start_pos:end_pos]
    print(people_num)