from insert_ import insert
from query_ import query
from delete_ import delete
from update_ import update
while True:
    choice =input("(1)新增資料(2)查詢資料(3)更新資料(4)刪除資料(5)結束程式：")
    if choice =='1':
        insert()
    elif choice=='2':
        query()
    elif choice=='3':
        update()
    elif choice=='4':
        delete()
    elif choice=='5':
        print("結束程式！")
        break
    else:
        print("無效指令！")