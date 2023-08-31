def calculate(name,id):
    import pandas as pd
    df = pd.read_excel('data.xlsx')
    try:
        data = df[(df['名字']==name) & (df['身分證字號']==id)].to_dict('records')[0]
        BMI = round(data['體重']/(data['身高']/100)**2,2)
        if data['性別'] == "m":
            x=1
        elif data['性別'] == "f":
            x=2
        print("BMI:",BMI)
        BMR = (1.2*int(BMI)+0.23*(data['年紀'])-5.4-10.8*(2-x))
        print("BMI判定體位:",end='')
        if BMI<18.5:
            print("過輕")
        elif 18.5<=BMI<24:
            print("健康體重(理想體重)")
        elif 24<=BMI<27:
            print("過重")
        else:
            print("肥胖")
        print("理想體重:",round(18.5*(data['身高']/100)**2,2),"到",round(24*(data['身高']/100)**2,2))
        print("體脂率:",round(BMR,2))
        print("體脂率判定體位:",end='')
        if x==1:
            if 2<=BMR<=5:
                print("基礎脂肪")
            elif 6<=BMR<=13:
                print("運動員")
            elif 14<=BMR<=17:
                print("健康")
            elif 18<=BMR<=24:
                print("正常")
            else:
                print("肥胖")
        else:
            if 10<=BMR<=13:
                print("基礎脂肪")
            elif 14<=BMR<=20:
                print("運動員")
            elif 21<=BMR<=24:
                print("健康")
            elif 25<=BMR<=31:
                print("正常")
            else:
                print("肥胖")
    except:
        print("查無此人")
if __name__ == "__main__":
    name = input('請輸入名字:')
    id  = input('請輸入身分證字號:')
    calculate(name,id)