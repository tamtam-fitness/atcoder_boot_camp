
#n is this time's vertex counts
n, m = map(int, input().split(" "))

vertex_li = [ [] for _ in range(n)]
print(vertex_li)

for _ in range(n) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    vertex_li[a].append(b)
    vertex_li[b].append(a)




for i in range(len(vertex_li[0])):
    already_visited_place = [ False for _ in range(n)]
    already_visited_place[0] = True
    next_place = vertex_li[0][i]

    while True:
        for place in vertex_li[next_place] :
            if already_visited_place[place] == True:
                pass
            else :
                next_place = place
                already_visited_place[next_place] = True
                if all(already_visited_place)



print(vertex_li)