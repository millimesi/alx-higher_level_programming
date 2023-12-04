#!/usr/bin/python3

class human:
    def __init__(self, sex):
        self.sex = sex
        self.leg = 2
        self.eye = 2
    def work(self):
        print("I can work")
        print(f"{self.sex} are ordered to submit for her husband")
    def live(self):
        print("human live in the world")
class ethio(human):
    def __init__(self, nation, sex):
        super().__init__(sex)
        self.nation = nation
    def nations(self):
        print("we have 85 nations")
        print(f"{self.nation} is one in ethiopia")
    def live(self):
        super().live()
        print("ethiopian live in east africa!")
milli = ethio("gurage", "womens")
milli.nations()
milli.live()
milli.work()
print(f"leg = {milli.leg} eye = {milli.eye}")
print(ethio.mro())