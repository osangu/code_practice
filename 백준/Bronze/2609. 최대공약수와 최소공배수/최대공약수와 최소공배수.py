N, M = map(int, input().split())


def gcd(N, M):
    if M <= 0:
        return N
    return gcd(M, N % M)


def lcm(N, M, GCD):
    return (N * M) // GCD


if __name__ == '__main__':
    print(gcd_ := gcd(N, M))
    print(lcm(N, M, gcd_))
