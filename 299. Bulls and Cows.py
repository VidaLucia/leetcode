class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b=0
        c=0
        secret_counter = Counter()
        guess_counter = Counter()
        for s, g in zip(secret, guess):
            if s == g:
                b += 1
            else:
                secret_counter[s] += 1
                guess_counter[g] += 1
        for digit in secret_counter:
            c+=min(secret_counter[digit],guess_counter[digit])

        return f"{b}A{c}B"
        # done in python3 cus i wanted to use f strings lol