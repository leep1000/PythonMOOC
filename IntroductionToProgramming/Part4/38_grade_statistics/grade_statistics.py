# Write your solution here
'''
one function to get scores
one function to analyse exercises
one function to get overall pass %
one function to make a list with the overall score for each student
one to combine the overall scores (into an array)
one function to get calculate grades
one main one to call other functions and print to the console 
'''

def grade_statistics():
    both_scores = get_scores()
    exam_scores = both_scores[0]
    exercise_scores = exercise_score_analysis(both_scores[1])
    grade_average = points_average(exam_scores, exercise_scores)
    overall_grade = overall_score(exam_scores, exercise_scores)
    passed_percent = pass_percentage(overall_grade)
    grades = grade_calc(overall_grade)
    
    print("Statistics:")
    print(f"Points average: {grade_average}")
    print(f"Pass percentage: {passed_percent}")
    print("Grade distribution: ")   
    for i in range(5,-1,-1):
        print(f"  {i}: {grades[i] * "*"}")


def get_scores():
    exam_scores: list = []
    exercises_complete: list = []
    
    while True:
        exam_and_exercises = input("Exam points and exercises completed: ")
        if exam_and_exercises == "":
            break
        else:
            space = exam_and_exercises.find(" ")
            exam_scores.append(int(exam_and_exercises[:space]))
            exercises_complete.append(int(exam_and_exercises[space + 1:]))
            
    return exam_scores, exercises_complete

def exercise_score_analysis(exercise_list: list):
    exercise_score: list = []
    for score in exercise_list:
        exercise_score.append(score // 10)
    return exercise_score

def points_average(exam_score : list, exercise_score : list):
    sum = 0
    counter = 0
    for score in exercise_score:
        sum += score
        sum += exam_score[counter]
        counter += 1
    average = sum / len(exercise_score)
    return f"{average:.1f}"

def overall_score(exam_score : list, exercise_score : list, ):
    overall_scores_list = []
    counter = 0
    for score in exercise_score:
        if exam_score[counter] < 10:
            overall_scores_list.append(0)
        else:
            overall_scores_list.append(score + exam_score[counter])
        counter += 1
            
    return overall_scores_list

def pass_percentage(overall_score: list):
    passed = 0
    for score in overall_score:
        if score >= 15:
            passed += 1
    all_pass_percentage = (passed / len(overall_score)) * 100
            
    return f"{all_pass_percentage:.1f}"

def grade_calc(overall_score : list):
    grade : list = [0, 0, 0, 0, 0, 0]
    for score in overall_score:
        if score < 15:
            grade[0] += 1
        elif score <= 17:
            grade[1] += 1
        elif score <= 20:
            grade[2] += 1
        elif score <= 23:
            grade[3] += 1
        elif score <= 27:
            grade[4] += 1
        else:
            grade[5] += 1
    return grade

grade_calc([23, 15, 15, 0])

grade_statistics()



