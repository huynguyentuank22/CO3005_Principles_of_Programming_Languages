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
pattern = 'self.assertTrue'
flag = False

for i, line in enumerate(data):  # Duyệt từng dòng với index
    if pattern in line:
        if str(index) in line and not flag:
            print(line)
            flag = True
            start += 1
        elif flag:
            print(line)
            number = re.search(r'\b\d+\b', line)
            if number:  # Kiểm tra nếu tìm thấy số
                data[i] = line.replace(str(number.group()), str(start))  # Cập nhật trực tiếp
            start += 1
            print(data[i])  # Kiểm tra kết quả đã thay đổi  

with open("output.txt", 'w') as f:
    for line in data:
        f.write(line)