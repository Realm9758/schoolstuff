def get_test_scores(students):
    scores = []
    for i in range(1, students + 1):
        while True:
            try:
                score = int(input(f"Enter test score for student {i} (0-100): "))
                if 0 <= score <= 100:
                    scores.append(score)
                    scores.sort()
                    break
                else:
                    print("Enter a number between 0 and 100")
            except ValueError:
                print("enter a valid number")
    return scores

num_students = int(input("Enter number of students are in your class: "))


test_scores = get_test_scores(num_students)
average_score = sum(test_scores) / len(test_scores)
print("Test scores entered:", test_scores)
print(f"{test_scores[0]} is the lowest score")
print(f"{max(test_scores)} is the highest score")
print(f"{average_score} is the average score")




