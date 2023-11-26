L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            # always validate the input
            return []
        res=[]
        def dfs(i,cur):
            if len(cur)==len(digits):
                res.append(cur)
                return
            for letter in L[digits[i]]:
                dfs(i+1,cur+letter)
        dfs(0,"")
        return res
