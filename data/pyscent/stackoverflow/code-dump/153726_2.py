def roundRobin(T):
    P = T[1:]+len(T)%2*[None]
    for _ in range(len(T)-1):
        yield [g for g in zip(T[:1]+P[1:len(P)//2+1],P[:1]+P[::-1])]
        P.append(P.pop(0))

    
# Odd number of teams (7) 
for games in roundRobin(["A","B","C","D","E","F","G"]):
    print(games)

[('A', 'B'), ('C', None), ('D', 'G'), ('E', 'F')] # C sits out
[('A', 'C'), ('D', 'B'), ('E', None), ('F', 'G')] # E sits out
[('A', 'D'), ('E', 'C'), ('F', 'B'), ('G', None)] # G sits out
[('A', 'E'), ('F', 'D'), ('G', 'C'), (None, 'B')] # B sits out
[('A', 'F'), ('G', 'E'), (None, 'D'), ('B', 'C')] # D sits out
[('A', 'G'), (None, 'F'), ('B', 'E'), ('C', 'D')] # F sits out

# Even number of teams (10)
for games in roundRobin(["A","B","C","D","E","F","G","H","I","J"]):
    print(games) 

[('A', 'B'), ('C', 'J'), ('D', 'I'), ('E', 'H'), ('F', 'G')]
[('A', 'C'), ('D', 'B'), ('E', 'J'), ('F', 'I'), ('G', 'H')]
[('A', 'D'), ('E', 'C'), ('F', 'B'), ('G', 'J'), ('H', 'I')]
[('A', 'E'), ('F', 'D'), ('G', 'C'), ('H', 'B'), ('I', 'J')]
[('A', 'F'), ('G', 'E'), ('H', 'D'), ('I', 'C'), ('J', 'B')]
[('A', 'G'), ('H', 'F'), ('I', 'E'), ('J', 'D'), ('B', 'C')]
[('A', 'H'), ('I', 'G'), ('J', 'F'), ('B', 'E'), ('C', 'D')]
[('A', 'I'), ('J', 'H'), ('B', 'G'), ('C', 'F'), ('D', 'E')]
[('A', 'J'), ('B', 'I'), ('C', 'H'), ('D', 'G'), ('E', 'F')]
