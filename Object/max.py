student_score = {'james':85, 'jackson':99, 'lily': 81}
l=max(student_score.values())

for key,value in student_score.items():
    if(value == max(student_score.values())):
        print (key,value)