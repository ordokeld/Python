import itertools
import string

def brute_password(password, min_len, max_len):
    chars = string.ascii_letters+string.digits
    attempt=0

    for length in range(min_len, max_len+1):
        for guess in itertools.product(chars, repeat=length):
            attempt += 1
            guess_str=''.join(guess)
            print(f"Try №{attempt}, {guess_str}")
            if guess_str==password:
               print(f"Password found: {guess_str}")
               return

password='123'
brute_password(password, 1, 5)
