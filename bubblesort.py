def scoresort(score):
    n = len(score)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if score[j] > score[j+1]:
                score[j], score[j+1] = score[j+1], score[j]
    return score

scores = [7, 8, 2, 1, 3, 2, 23]
sorted_scores = scoresort(scores)
print(sorted_scores)


