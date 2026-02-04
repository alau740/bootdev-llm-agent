from functions.write_files_content import write_file

def test():
    # Tests to ensure functionality
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(write_file)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(write_file)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(write_file)


if __name__ == "__main__":
    test()