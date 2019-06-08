class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x>y:
            x,y = y,x
        count = 0
        bx = str(bin(x)).replace('0b','')
        by = str(bin(y)).replace('0b','')

        bx = '0'*(len(by)-len(bx))+bx

        print(bx)
        print(by)

        for i in zip(bx,by):
            print(i)
            if i[0] != i[1]:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    a = s.hammingDistance(1,4)
    print(str(bin(10)))
    print(str(bin(4)))
    print(a)