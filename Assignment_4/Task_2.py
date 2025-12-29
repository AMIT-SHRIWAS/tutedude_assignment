def write_and_append_file(filename):
    try:
        # Take user input and write to file (overwrite mode)
        user_input = input("Enter text to write to the file: ")
        with open(filename, "wt") as fh:
            fh.write(user_input + "\n")
            print(f'Data successfully written to file "{filename}"')
            print()

        # Append additional data
        extra_input = input("Enter additional text to append: ")
        with open(filename, "at") as fh:
            fh.write(extra_input + "\n")
            print(f'Data successfully appended to file "{filename}"')

        # Read and display final content
        print(f"\nFinal content of {filename}:")
        with open(filename, "r") as f:
            for line in f:
                print(line.rstrip())

    except PermissionError:
        print(f"Error: You do not have permission to write to '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    write_and_append_file("output.txt")
