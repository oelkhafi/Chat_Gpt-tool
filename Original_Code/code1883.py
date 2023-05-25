from itertools import permutations as per

box1, box2 = (int(input()), int(input()), int(input())), (int(input()), int(input()), int(input()))
pr = False

for i in list(per(box1)):
    for j in list(per(box2)):
        if i == j:
            print(""Boxes are equal"")
            pr = True
            break
        elif tuple(i[q] <= j[q] for q in range(3)) == (True, True, True):
            print(""The first box is smaller than the second one"")
            pr = True
            break
        elif tuple(i[q] >= j[q] for q in range(3)) == (True, True, True):
            print(""The first box is larger than the second one"")
            pr = True
            break
    if pr:
        break

else:
    print(""Boxes are incomparable"")
 