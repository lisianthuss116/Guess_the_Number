# class Testing:
#     def test():
#         x = 5
#         return x

# def check():
#     Choices = {
#         "1": (Testing.test, "qwe"),
#         "2": ("2", "asd"),
#         "3": ("3", "zxc"),
#         "4": "Exit",
#     }

#     return Choices.get("1")[0]()


# check()

class Testing:
    def __init__(self):
        self.x = 0
        self.y = 0

    def win(self):
        choices = {
            "player": 'y',
            "computer": 'x',
        }

        xuser = choices.get("player")
        return xuser


obj = Testing()
# atr = obj.win()

# print(obj.__dict__)

print(getattr(Testing, obj.win()))

# new_val = getattr(Testing, atr) + 1
# print(f"new val : {new_val}")
# print(getattr(Testing, atr) = new_val)

# print(Testing.y)
