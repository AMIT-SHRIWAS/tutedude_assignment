# Demonstrate List Slicing

def list_slicing():
    original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sliced = original[:5:1]
    rev = sliced[::-1]

    print(f'Original list : {original}')
    print(f'Extracted first five elements : {sliced}')
    print(f'Reversed extracted elements ; {rev}')

if __name__ == '__main__':
    list_slicing()