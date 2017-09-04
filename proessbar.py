import sys, time
 
for i in range(5):
    sys.stdout.write('{0}/5\r'.format(i + 1))
    sys.stdout.flush()
    time.sleep(1)


yield {'zwmc': zwmc,  # 职位名称
     'fkl': fkl,  # 反馈率
     'gsmc': gsmc,  # 公司名称
     'zwyx': zwyx,  # 职位月薪
     'gzdd': gzdd,  # 工作地点
     'gbsj': gbsj,  # 公布时间
     'brief': brief,  # 招聘简介
     'zw_link': zw_link,  # 网页链接
     'save_date': date  # 记录信息保存的日期
     }