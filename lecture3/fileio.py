from time import sleep

filename = "lecture3/junk.txt"
out_lines = ['this', 'is', 'some', 'text']
add_lines = ['to', 'be', 'written', 'out']

# Write mode
with open(filename, 'w', encoding='utf-8') as f:
    for line in out_lines:
        f.write(line + '\n')

sleep(3)

# Append mode
with open(filename, 'a', encoding='utf-8') as f:
    for line in add_lines:
        f.write(line + '\n')

# Read mode
with open(filename, 'r', encoding='utf-8') as f:
    print("Contents: ")
    print(f.read())
