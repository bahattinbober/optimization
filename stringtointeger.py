class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading/trailing spaces
        if not s:
            return 0

        sign, i, res = 1, 0, 0

        # Check for sign
        if s and s[0] == '-':
            sign = -1
            i += 1
        elif s and s[0] == '+':
            i += 1

        # Process numerical characters
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])

            # Handle overflow
            if sign * res > 2**31 - 1:
                return 2**31 - 1
            if sign * res < -2**31:
                return -2**31

            i += 1

        return sign * res

# Buradan sonrası programı çalıştırınca test edilmesi için eklendi
if __name__ == "__main__":
    solution = Solution()
    
    # Test örneği
    s = "   -42"
    result = solution.myAtoi(s)
    print(result)  # Beklenen çıktı: -42
