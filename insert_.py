def insert():
    import pandas as pd
    from calculate_ import calculate
    df = pd.read_excel('data.xlsx')
    data = ['luke','h','15','f','60','160']
    columns = ['名字','身分證字號','年紀','性別','體重','身高']
    data = []
    #data2 = ['1','2','3','4','5']
    #columns2 = ['BMI','BMI判定體位','理想體重','體脂率','體脂率判定體位']
    #data2 = []
    for i in columns:
        a = input("請輸入"+i+":")
        data.append(a)

    df2 = pd.DataFrame([data],columns=columns)
    df = pd.concat([df2,df],ignore_index=True)
    df.to_excel('data.xlsx',index=False)
    calculate(name=data[0],id=data[1])
if __name__ == "__main__":
    insert()        