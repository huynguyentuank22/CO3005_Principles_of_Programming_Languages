import re

# path = r'C:\Users\Huy\Documents\Tuan_Huy\CO3005_PPL\Assignment_1\initial\initial\src\test\LexerSuite.py'
# path = r'C:\Users\Huy\Documents\Tuan_Huy\CO3005_PPL\Assignment_1\initial\initial\src\test\ParserSuite.py'
# path = r"C:\Users\Huy\Documents\Tuan_Huy\CO3005_PPL\Assignment_2\initial\initial\src\test\ASTGenSuite.py"
path = r"C:\Users\Huy\Documents\Tuan_Huy\CO3005_PPL\Extra\assignment-initial\initial\src\test\VMSuite.py"
with open(path, 'r') as f:
    data = f.readlines()

# đánh lại các testcase từ sau testcase có index và bắt đầu từ index start
index = 401
start = 401
pattern = 'def test_'
flag = False

for i, line in enumerate(data):  # Duyệt từng dòng với index
    if pattern in line:
        data[i] = line.replace('test_', 'test_' + str(start) + '_')  # Cập nhật trực tiếp
        start += 1
        print(data[i])

with open("output.txt", 'w') as f:
    for line in data:
        f.write(line)