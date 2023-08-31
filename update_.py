def update():
    import pandas as pd
    from calculate_ import calculate
    df = pd.read_excel('data.xlsx')
    name = input('請輸入名字:')
    id = input('請輸入身分證號:')
    ele = ['年紀','性別','體重','身高']
    if len(df[(df['名字'] == name)&(df['身分證字號'] == id)].to_dict('records'))==0:
        print("查無此人")
    else:
        for i in ele:
            answer = input('請輸入'+i+'，不輸即不修改:')
            if answer!="":
                df.loc[df['名字'] ==name, i] = answer
        df.to_excel('data.xlsx',index=False)
    calculate(name,id)
if __name__=="__main__":
    update()