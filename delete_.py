def delete():
    import pandas as pd
    name=input('請輸入要刪除的名字:')
    id=input('請輸入身分證字號:')
    df = pd.read_excel('data.xlsx')
    a=len(df[(df['名字'] == name)&(df['身分證字號'] == id)].to_dict('records'))
    if a==0:
        print("查無此人")
    else:
        df = df.drop(df[(df['名字'] == name)&(df['身分證字號'] == id)].index)
        df.to_excel('data.xlsx',index=False)
        print("刪除成功")

if __name__ == "__main__":
    delete()