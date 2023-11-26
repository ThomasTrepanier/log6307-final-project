def doubles(S):
    return any(set(enumerate(S))&set(enumerate(S,1)))

print(doubles("akdgjg"))     # False
print(doubles("dkjhfkddhk")) # True
