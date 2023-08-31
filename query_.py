def query():
    import pandas as pd  
    df = pd.read_excel('data.xlsx')
    from calculate_ import calculate
    name = input('請輸入名字:')
    id  = input('請輸入身分證字號:')
    while True:
        try:
            print(df[(df['名字']==name) & (df['身分證字號']==id)])
            calculate(name,id)
            break
        except:
            print("查無此人")

if __name__ == "__main__":
    query()