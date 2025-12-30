Task 1: Read File with Error Handling
Purpose: Opens sample.txt, reads line-by-line, handles FileNotFoundError gracefully.

Key Concepts:

1. with open() ensures automatic file closure

2. try-except catches FileNotFoundError

3. file iterable reads line-by-line

Task 2: Write, Append, and Read File
Purpose: Creates output.txt, writes initial data, appends more, then displays final content.

Key Concepts:

'w' mode: Write (overwrites existing file)

'a' mode: Append (adds to end)

'r' mode: Read final content

file.write() requires manual \n for newlines