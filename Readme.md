# SHA-256 Implementation and Book of Mark Hash

### What I Did
I implemented the SHA-256 hashing algorithm manually in Python using `sha256_custom.py`.  
Then I downloaded the full text of the Book of Mark from the University of Michigan RSV Bible website and used my algorithm to produce the hash value.

### How to Run
1. Install dependencies:
pip install requests beautifulsoup4
2. Run The Program:
python hash_mark.py
3. The result is saved in `mark_sha256.txt`.

File name And Purpose:

sha256_custom.py: This file contains your own SHA-256 algorithm (the logic of how hashing works).

hash_mark.py	: This file downloads the text of the Book of Mark and uses your SHA-256 function to calculate the hash.

mark_sha256.txt: The output text file that stores the final hash value you got.

README.md: A short note explaining what your project does and how to run it.
