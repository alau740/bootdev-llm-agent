from functions.run_python_file import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py") # outside allowed working dir
    print(result)

    result = run_python_file("calculator", "nonexistent.py") # test validation
    print(result)

    result = run_python_file("calculator", "lorem.txt") # not a python file
    print(result)


if __name__ == "__main__":
    test()