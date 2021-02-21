class Number:
    def sum(self):
        return(self.a + self.b)

num = Number()
# num is a object of class Number.

num.a = int(input("enter a number\n"))
num.b = int(input("enter a number\n"))
s = num.sum()
print(f"sum of {num.a} and {num.b} is ",s)



