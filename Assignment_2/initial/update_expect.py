import re
import sys

SOLUTIONS_FOLDER = r"C:\Users\Huy\Documents\Tuan_Huy\CO3005_PPL\Assignment_2\initial\initial\src\test\solutions"
TEST_FILE = r"C:\Users\Huy\Documents\Tuan_Huy\CO3005_PPL\Assignment_2\initial\initial\src\test\ASTGenSuite.py"

def update_expect_strings(start=None, end=None):
    with open(TEST_FILE, "r", encoding="utf-8") as file:
        test_file_content = file.read()

    test_functions = re.findall(r"def (test_[a-zA-Z0-9_]+)\(self\):", test_file_content)
    print(len(test_functions))
    print(f"Test cases found: {test_functions}")

    if start is not None and end is not None:
        test_functions = [t for t in test_functions if start <= int(t.split("_")[1]) <= end]
    print(f"Test cases to update: {test_functions}")

    tests = [f"test_{i}" for i in range(301, 402)]
    # if not test_functions:
    #     print("No matching test cases found. Check the regex or test file format.")
    #     return

    for i in range(len(test_functions)):
        test_num = tests[i]
        solution_file = f"{SOLUTIONS_FOLDER}/{test_num[5:]}.txt"
        try:
            with open(solution_file, "r", encoding="utf-8") as file:
                expect_output = file.read().strip()

            new_expect_statement = f"str({expect_output})"

            # Remove any existing 'expect =' line in the function and replace it with the new one
            test_file_content = re.sub(
                rf'(def {test_functions[i]}\(self\):\s*\n(?:\s+.*\n)*?\s*)expect\s*=([\s\S]*?)(?=\n\s*(?:self\.assertTrue|def |\Z))',
                rf'\1expect = {new_expect_statement}',
                test_file_content,
                flags=re.MULTILINE
            )
            print(f"✅ Updated {test_functions[i]} with expect string from {solution_file}")
        except FileNotFoundError:
            print(f"⚠️ Solution file not found for {test_functions[i]}")

    # Write the updated content back to the test file
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        file.write(test_file_content)

    print("🎉 Expect strings updated successfully!")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            start_test = int(sys.argv[1])
            end_test = int(sys.argv[2])
            update_expect_strings(start=start_test, end=end_test)
        except ValueError:
            print("❌ Invalid arguments. Use: python script.py <start> <end>")
    else:
        update_expect_strings()
