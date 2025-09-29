#Eg:
'''def students(scores):
    grade ={
        'A' : [],
        'B' : [],
        'C' : [],
        'D' : [],
        'F' : []
}
    for name, score in scores:
        if score >= 90:
            grade['A'].append(name)
        elif score>=70:
            grade['B'].append(name)
        elif score>=50:
            grade['C'].append(name)
        elif score>=40:
            grade['D'].append(name)
        else:
            grade['F'].append(name)
    return grade
Names = {('Axlin',92),('Alice',55),('Anu',77),('Eve',30),('Bob',44),('Emil',66)}
result = students(Names)
print(result)'''


#Eg:
def calculate_average_scores(student_scores):
    average_scores = {}    
    for name, scores in student_scores.items():
        average_scores[name] = sum(scores) / len(scores)
    return average_scores

students = {
    "Alice": [85, 90, 95],
    "Bob": [78, 82, 88],
    "Charlie": [92, 87],
    "Eve": [60, 65]
}
result = calculate_average_scores(students)
print(result)


































