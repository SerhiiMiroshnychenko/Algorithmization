class StrInt(str):
    def __add__(self, b):
        ans = int(self) + int(b)
        return str(ans)

a = StrInt('10')
b = StrInt('20')

print(a + b)
