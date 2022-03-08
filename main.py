class RomanNumeralsConverter:
    roman_nums = {
        "M" : 1000, "CM" : 900, "D" : 500, "CD" : 400,
        "C" : 100, "XC" : 90, "L" : 50, "XL" : 40,
        "X" : 10,  "IX" : 9, "V" : 5, "IV" : 4, "I" : 1
    }
    
    def __init__(self):
        self.entry = ""

    def start(self):
        entry = input("Enter numbers or roman numerals to convert\n")

        try:
            self.entry = int(entry)
        except ValueError:
            if False in [i in self.roman_nums for i in entry.upper()]:
                return "Error occured!\nPlease enter a number or a valid roman numerals"
            else:
                self.entry = entry.upper()

        return self.to_check()

    def to_check(self):
        is_integer = isinstance(self.entry, int)
        
        return self.to_roman_numerals(self.entry) if is_integer \
            else self.to_numbers(self.entry)

    def to_roman_numerals(self, num):
        converted_string = ""
    
        for key, value in self.roman_nums.items():
            while num >= self.roman_nums[key]:
                converted_string += key
                num = num - self.roman_nums[key]
            
        return converted_string
    
    def to_numbers(self, str):
        converted_value = 0
    
        for i in range(len(str)):
            if i > 0 and self.roman_nums[str[i]] > self.roman_nums[str[i - 1]]:
                converted_value += self.roman_nums[str[i]] - 2 * self.roman_nums[str[i - 1]]
            else:
                converted_value += self.roman_nums[str[i]]
                
        return converted_value


roman_numerals_converter = RomanNumeralsConverter()
print(roman_numerals_converter.start())