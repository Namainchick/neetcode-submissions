class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        dfs with two inputs i j which are pointers to both strings
        in this case it makes sense to start from the end
        if its a point we just move both pointers
        if its a star 
            -   we look at the character before and decide 
            -   if before is a normal character we can check if we are garuanteed that before star is a char
            -   so we move j down and have a state where we say star
            -   so now we have state star and a char so 
                -   move j pointer and pretend star is zero and end star state
                -   check directly if match dfs with i 
            -   if its a point 
                -   move j pointer and pretend star is zero and end star state
                -   return dfs with i next 
        if no star we just check and move if same else return False
        if we end at -1 for both it means we reached the end and return True
        if j or i is over at the end each then return false

        """
        ns,np = len(s),len(p)

        def dfs(i,j,star):
            if i == -1 and j == -1:
                return True

            if j == -1:
                return False

            if p[j] == "*":
                return dfs(i,j-1,True)

            if star:
                zero = dfs(i, j - 1, False)                  
                one = False
                if i >= 0 and (p[j] == "." or s[i] == p[j]):
                    one = dfs(i - 1, j, True)              
                return zero or one

            if i == -1:
                return False

            if p[j] == "." or s[i] == p[j]:
                return dfs(i - 1, j - 1, False)

            return False

        return dfs(ns-1,np-1,False)