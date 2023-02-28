def sol(cards1, cards2, goal):
    answer = 'Yes'
    index_one = index_two = 0

    for i in goal:
        if len(cards1) > index_one and i == cards1[index_one]:
            index_one += 1
        elif len(cards2) > index_two and i == cards2[index_two]:
            index_two += 1
        else:
            answer = 'No'

    return answer
