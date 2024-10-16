class solution:
    def longestDiverseString(self,a : int,b: int,c: int)->str:
        counts = [('a', a),('b', b), ('c', c)]
        result = []
        while True:
            counts.sort(key=lambda x: -x[1])
            found = False
            for i in range(3):
                letter,count = count[i]
                if count > 0 and (len(result)<2 or not (result[-1] == result[-2] == letter)):
                    result.append(letter)
                    count[i] = (letter, count -1)
                    found = True
                    break
            if not found:
                break
        return ''.join(result)