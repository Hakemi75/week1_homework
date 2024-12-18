class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return "{} {}".format(self.first_name, self.family_name)

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif self.age < 65:
            return 1500
        else:
            return 1200

    def info_csv(self):
        # if self.first_name == "Ken":
        return "{},{},{}".format(self.full_name(), self.age, self.entry_fee())
        # return "{},{},{}".format(ken.full_name(), ken.age, ken.entry_fee())
        # elif self.first_name == "Tom":
        # return "{},{},{}".format(tom.full_name(), tom.age, tom.entry_fee())

        # return "{},{},{}".format(tom.full_name(), tom.age, tom.entry_fee())
        # else:
        # return "{},{},{}".format(ieyasu.full_name(), ieyasu.age, ieyasu.entry_fee())
        # return "{},{},{}".format(ieyasu.full_name(), ieyasu.age, ieyasu.entry_fee())


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)

# 以降で各問のコードを追加していく

print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力


print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力


print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力

print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
