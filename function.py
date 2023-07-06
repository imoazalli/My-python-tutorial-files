def percent(marks):
    return((marks[0]+marks[1]+marks[2]+marks[3])/400*100)

marks=[45,78,75,88]
percentage=percent(marks)

marks2=[35,98,77,56]
percentage2=percent(marks2)
print(percentage, percentage2)