result = []
result = [int(x) for x in input("データを入力してください(スペース区切り)").split(" ")]


def goukei():
    total = 0
    for i in result:
        total += i

    print(f"合計値: {total}")


goukei()


def ookii():
    saidai = 0
    for i in result:
        if saidai < i:
            saidai = i
        else:
            pass

    print(f"最大値: {saidai}")


ookii()


def tiisai():
    # 合計関数の戻り値をsaishou変数に代入する方法もある
    saishou = float("inf")
    for i in result:
        if saishou < i:
            pass
        else:
            saishou = i

    print(f"最小値: {saishou}")


tiisai()


def mannaka():
    kotae = 0
    heikin = 0
    # 合計関数の戻り値を利用する方法もある
    for i in result:
        heikin += i

    kotae = heikin / len(result)
    print(f"平均値: {int(kotae)}")


mannaka()
