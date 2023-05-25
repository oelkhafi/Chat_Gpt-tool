ch = {
    '0': ["" -- "", ""|  |"", ""|  |"", ""    "", ""|  |"", ""|  |"", "" -- ""],
    '1': [""    "", ""   |"", ""   |"", ""    "", ""   |"", ""   |"", ""    ""],
    '2': ["" -- "", ""   |"", ""   |"", "" -- "", ""|   "", ""|   "", "" -- ""],
    '3': ["" -- "", ""   |"", ""   |"", "" -- "", ""   |"", ""   |"", "" -- ""],
    '4': [""    "", ""|  |"", ""|  |"", "" -- "", ""   |"", ""   |"", ""    ""],
    '5': ["" -- "", ""|   "", ""|   "", "" -- "", ""   |"", ""   |"", "" -- ""],
    '6': ["" -- "", ""|   "", ""|   "", "" -- "", ""|  |"", ""|  |"", "" -- ""],
    '7': ["" -- "", ""   |"", ""   |"", ""    "", ""   |"", ""   |"", ""    ""],
    '8': ["" -- "", ""|  |"", ""|  |"", "" -- "", ""|  |"", ""|  |"", "" -- ""],
    '9': ["" -- "", ""|  |"", ""|  |"", "" -- "", ""   |"", ""   |"", "" -- ""]
    }
nums = str(input())
n = len(nums)
print('x' + '-' * (5 * n - 1) + 'x')
for i in range(7):
    row = '|'
    for number in nums[:-1]:
        row += ch[number][i] + ' '
    row += ch[nums[-1]][i] + '|'
    print(row)
print('x' + '-' * (5 * n - 1) + 'x')
 