
month_list = ['Baishak','Jestha','Asar','Shrawan','Bhadra','Ashoj','Kartik','Mangshir','Poush','Magh','Falgun','Chaitra']
month = {
    month_list.index(month_name)+1 : month_name for month_name in month_list
}

def Month():
    month_list = ['Baishak','Jestha','Asar','Shrawan','Bhadra','Ashoj','Kartik','Mangshir','Poush','Magh','Falgun','Chaitra']
    month = {
        month_list.index(month_name)+1 : month_name for month_name in month_list
    }
    return month