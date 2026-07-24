class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        int_lookup = {
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            '0' : 0
        }

        str_lookup = {
            1 : '1',
            2 : '2',
            3 : '3',
            4 : '4',
            5 : '5',
            6 : '6',
            7 : '7',
            8 : '8',
            9 : '9',
            0 : '0'
        }

        Inum1 = 0
        Inum2 = 0
        num1_decimals = 1

        for i in range(-1, -len(num1) - 1, -1):
            Inum1 += int_lookup[num1[i]] * num1_decimals
            num1_decimals *= 10
        
        num2_decimals = 1
        for k in range(-1, -len(num2) - 1, -1):
            Inum2 += int_lookup[num2[k]] * num2_decimals
            num2_decimals *= 10
        
        val = Inum1 + Inum2
        
        sys.set_int_max_str_digits(10000)

        return str(val)
            


