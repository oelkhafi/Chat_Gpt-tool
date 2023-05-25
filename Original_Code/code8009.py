import operator
x = float(input())
y = float(input())
z = str(input())

ops = { ""+"": operator.add, 
        ""-"": operator.sub,
        ""*"": operator.mul,
        ""/"": operator.truediv,
        ""div"": operator.floordiv,
        ""mod"": operator.mod,
        ""pow"": operator.pow }
if y == 0.0:
    if ((z == ""/"") or (z == ""div"") or (z == ""mod"")):
        print(""Деление на 0!"")
    else:
        result = ops[z](x, y)
        print(result)
else:
    result = ops[z](x, y)
    print(result) 