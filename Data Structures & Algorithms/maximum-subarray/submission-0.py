class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        wir können mit prefix sum die sumen berechnen und dann jede kombination
        also n^2 mit O(1) berechnen. Prefix bauen kostet O(n) vielleicht geht es ja
        schneller 
        Wir können auch einfach durch das array gehen und sobald wir wieder negativ 
        sind wissen wir alles davor egal wo wir angefangen hätten wäre nicht besser 
        gewesen weil wir immer neutral anfangen. 
        Deswegen kann man hier einfach durch das array gehen und sobald man negativ ist
        skipped man alles über das negative und fängt bei null an. Bei jedem step checkt 
        man den größten. Da man jeden einmal besucht ist das O(n) time O(1) space
        """
        best = None
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            if best is None:
                best = cur
            else:
                best = max(best,cur)

            if cur < 0:
                cur = 0

        return best