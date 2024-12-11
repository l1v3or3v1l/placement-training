players = int(input())
max = 0
maxi = 0
for i in range(players):
    score = 0
    no_boxes = int(input())
    boxes = list(map(int, input().split()))
    score += no_boxes
    d = {}
    for b in boxes:
        d[b] = 1
    if len(d) > 3:
        score += min(len(d) - 3, 4)
    if score > max:
        max = score
        maxi = i
    print(score)
print(maxi + 1)
