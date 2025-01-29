import sys
input = sys.stdin.readline

# 1) Read all queries first and find maximum n
nums = []
while True:
    n = int(input())
    if n == 0:
        break
    nums.append(n)
max_n = max(nums)  # largest n

# 2) Sieve up to 2*max_n
limit = 2 * max_n
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, limit+1, i):
            is_prime[j] = False

# 3) Build prefix sums where prefix[i] = number of primes <= i
prefix = [0] * (limit + 1)
for i in range(1, limit + 1):
    prefix[i] = prefix[i-1] + (1 if is_prime[i] else 0)

# 4) For each n, output number of primes in (n, 2n]
for n in nums:
    # prime count in range (n, 2n] = prefix[2n] - prefix[n]
    print(prefix[2*n] - prefix[n])
