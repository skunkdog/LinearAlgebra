def findxindex(part,s):
    for i,j  in enumerate(part):
        if "x" in j:
            s.append(i)

def sumx(sumx1,part,X_index):
    for i in X_index:

        if i-1 >= 0 and part[i-1] == "-":
            sumx1.append(int("-" + part[i][1:-2]))
        else:

            sumx1.append(int(part[i][1:-2]))

def replacesum(X_index,part,ITEMS,sumx):
    for i in sorted(X_index, reverse=True):
        del part[i]
        if i-1>=0 and part[i-1] in ITEMS:
                del part[i-1]
    if sumx > 0:
        part.append("+")
        part.append("["+ str(sumx) + "x" + "]")
    if sumx < 0:
        part.append("-")
        part.append("[" + str(sumx)[1::] + "x" + "]")

def findnotxindex(part,s,ITEMS):
    for i,j  in enumerate(part):
        if "x" not in j and j not in ITEMS:
            s.append(i)


def sumnotx(sumx1,part,X_index):
    for i in X_index:

        if i-1 >= 0 and part[i-1] == "-":
            sumx1.append(int("-" + part[i][1:-1]))
        else:

            sumx1.append(int(part[i][1:-1]))

def replacesum_notx(X_index,part,ITEMS,sumx):
    for i in sorted(X_index, reverse=True):
        del part[i]
        if i-1>=0 and part[i-1] in ITEMS:
                del part[i-1]
    if sumx > 0:
        part.append("+")
        part.append("["+ str(sumx) + "]")
    if sumx < 0:
        part.append("-")
        part.append("[" + str(sumx)[1::] + "]")

A  = input("Enter the equation in this format [ax] + [b] = [cx]: ")
ITEMS  = "+ = - / *"

list_A = A.split()

index_equal = list_A.index("=") # Index of equal sign

left_part = " ".join(list_A [ 0:index_equal ] ).strip().split() #Left part
right_part = " ".join( list_A [ index_equal:: ] ).replace("=" , '').strip().split() #Right part

right_X_index = [] #Index of all x on right side
left_X_index = []
findxindex(right_part, right_X_index )
findxindex(left_part, left_X_index )



sumx_right = []
sumx(sumx_right, right_part, right_X_index)
sumx_right = sum( sumx_right)

replacesum(right_X_index, right_part, ITEMS, sumx_right)


sumx_left = []
sumx(sumx_left, left_part, left_X_index)
sumx_left = sum( sumx_left )


replacesum(left_X_index, left_part, ITEMS, sumx_left)

right_X_index = []
left_X_index = []
findxindex(right_part, right_X_index )
findxindex(left_part, left_X_index )

posx = None
for i in right_X_index:
    if right_part[i-1] == "+" and i-1 >= 0:
        posx = True
    else:
        posx = False

for i in right_X_index:
    sumx_right = right_part[i]
    del right_part[i]
    if right_part[i - 1] in ITEMS and i - 1 >= 0:
        del right_part[i-1]
if posx == None:
    pass
elif posx == True:
    left_part.append("-")
    left_part.append(sumx_right)
else:
    left_part.append("+")
    left_part.append(sumx_right)


left_X_index = []
findxindex(left_part, left_X_index)

sumx_left = []
sumx(sumx_left, left_part, left_X_index)
sumx_left = sum(sumx_left)

replacesum(left_X_index, left_part, ITEMS, sumx_left)

left_not_X_index = []
findnotxindex(left_part, left_not_X_index, ITEMS)

sumnotx_left = []
sumnotx(sumnotx_left, left_part, left_not_X_index)
sumnotx_left = sum(sumnotx_left)


replacesum_notx(left_not_X_index, left_part, ITEMS, sumnotx_left)


right_not_X_index = []
findnotxindex(right_part, right_not_X_index, ITEMS)

sumnotx_right = []
sumnotx(sumnotx_right, right_part, right_not_X_index)
sumnotx_right = sum(sumnotx_right)

replacesum_notx(right_not_X_index, right_part, ITEMS, sumnotx_right)


left_not_X_index = []
findnotxindex(left_part, left_not_X_index, ITEMS)

for i in left_not_X_index:
    if left_part[i-1] == "+" and i-1 >= 0:
        posx = True
    else:
        posx = False

    if posx == True:
        right_part.append("-")
        right_part.append(left_part[i])
    else:
        right_part.append("+")
        right_part.append(left_part[i])
    if i - 1 >= 0:
        del left_part[i]
        del left_part[i-1]
    else:
        del left_part[i]

right_not_X_index = []
findnotxindex(right_part, right_not_X_index, ITEMS)

sumnotx_right = []
sumnotx(sumnotx_right, right_part, right_not_X_index)
sumnotx_right = sum(sumnotx_right)


replacesum_notx(right_not_X_index, right_part, ITEMS, sumnotx_right)

delit = str(left_part[0])+str(left_part[1])[1:-2]
res = str(right_part[0])+str(right_part[1])[1:-1]



print(left_part, "=", right_part)

print("x = ",int(res)/int(delit))
