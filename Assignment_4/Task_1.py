def read_file(filename):
    try:
        with open(filename, "rt") as fh:
            fd = fh.readlines()
            line_num = 1
            for line in fd:
                print(f"line {line_num} : {line}", end="")
                line_num += 1
    except FileNotFoundError:
        print(f"\nError : The file {filename} was not found")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except IndexError:
        print()

if __name__ == "__main__":
    read_file("sample.txt")
