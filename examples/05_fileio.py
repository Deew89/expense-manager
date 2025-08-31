# examples/05_fileio.py
from pathlib import Path

p = Path("sample.txt")

# write text
p.write_text("line1\nline2\nline3\n")

# read text
content = p.read_text()
print("File content:")
print(content)
print(p.read_text())
