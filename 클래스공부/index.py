class icd:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("%s 가격은 %s입니다." % (name, price))
    def __del__(self):
        print("%s %s원 계산이 완료되었습니다" % (self.name, self.price))

obj = icd('브라보콘', 10000)
obj = icd('쌍쌍바', 5000)
