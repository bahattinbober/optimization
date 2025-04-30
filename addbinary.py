class Solution:
    def addBinary(self, a, b):
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry == 1:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            result.append(str(carry % 2))
            carry //= 2

        return ''.join(reversed(result))


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("1010", "1011"))  # Beklenen çıktı: 10101
