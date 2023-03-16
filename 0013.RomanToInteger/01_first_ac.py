class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0

        while i < len(s):
            symbol = s[i]

            if symbol == 'I':
                if i+1 < len(s) and s[i+1] == 'V':
                    sum += 4
                    i += 1
                elif i+1 < len(s) and s[i+1] == 'X':
                    sum += 9
                    i += 1
                else:
                    sum += 1

            elif symbol == 'X':
                if i+1 < len(s) and s[i+1] == 'L':
                    sum += 40
                    i += 1
                elif i+1 < len(s) and s[i+1] == 'C':
                    sum += 90
                    i += 1
                else:
                    sum += 10

            elif symbol == 'C':
                if i+1 < len(s) and s[i+1] == 'D':
                    sum += 400
                    i += 1
                elif i+1 < len(s) and s[i+1] == 'M':
                    sum += 900
                    i += 1
                else:
                    sum += 100

            elif symbol == 'V':
                sum += 5
            elif symbol == 'L':
                sum += 50
            elif symbol == 'D':
                sum += 500
            elif symbol == 'M':
                sum += 1000

            i += 1

        return sum