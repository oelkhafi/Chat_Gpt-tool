'' INPUT in format: <number> <unit_from> in <unit_to>
Convert from one unit to another'''

value, unit_from, unit_to = [i for i in input().split() if i != ""in""]
value = float(value)

dict = dict(mile=[1609, ""m""],
            km=[1000, ""m""],
            foot=[0.3048, ""m""],
            inch=[0.0254, ""m""],
            m=[1, ""m""],
            yard=[0.9144, ""m""],
            cm=[0.01, ""m""],
            mm=[0.001, ""m""],
            )

temp = dict[unit_from]
temp_value = temp[0]*value      #calculate the result in meters
if temp[1] != unit_to:
    temp = dict[unit_to]
    temp_value = temp_value / temp[0]
    print(""{:.2e}"".format(temp_value))
else:
    print(""{:.2e}"".format(temp_value))


 