
month_list = ['Baishak','Jestha','Asar','Shrawan','Bhadra','Ashoj','Kartik','Mangshir','Poush','Magh','Falgun','Chaitra']
month = {
    month_list.index(month_name)+1 : month_name for month_name in month_list
}

def MonthData():
    month_list = ['Baishak','Jestha','Asar','Shrawan','Bhadra','Ashoj','Kartik','Mangshir','Poush','Magh','Falgun','Chaitra']
    month = {
        month_list.index(month_name)+1 : month_name for month_name in month_list
    }
    return month
def YearData():
    year_list = [x for x in range(2080,2085)]
    return year_list

def RoomData():
    room_list = ['Grounfloor Front','Groundfloor Back','1. First Floor Front','2. First Floor Back','3. Second Floor Front','4. Second Floor Back','Kitchen']
    room = {
        room_list.index(room_name)+1 : room_name for room_name in room_list
    }
    return room