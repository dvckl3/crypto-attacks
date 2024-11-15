#chall.sage
from Crypto.Util.number import *

FLAG  = b"REDACTED"

p = getPrime(256)
q = getPrime(256)
e = 7
n = p*q
d = int(pow(e, -1, (p-1)*(q-1)))

c = pow(bytes_to_long(FLAG), e, n)
print(f"n = {n}")
print(f"c = {c}")
print(f"d_low = {hex(d)[70:]}")

"""
n = 9537465719795794225039144316914692273057528543708841063782449957642336689023241057406145879616743252508032700675419312420008008674130918587435719504215151
c = 4845609252254934006909399633004175203346101095936020726816640779203362698009821013527198357879072429290619840028341235069145901864359947818105838016519415
d_low = b9b24053029f5f424adc9278c750b42b0b2a134b0a52f13676e94c01ef77
"""
#solve.sage
python from Crypto.Util.number import *
from sage.all import *
N = 9537465719795794225039144316914692273057528543708841063782449957642336689023241057406145879616743252508032700675419312420008008674130918587435719504215151
c = 4845609252254934006909399633004175203346101095936020726816640779203362698009821013527198357879072429290619840028341235069145901864359947818105838016519415
leak = int("b9b24053029f5f424adc9278c750b42b0b2a134b0a52f13676e94c01ef77",16)

t = leak.bit_length()
e = 7


for k in range(1,e + 1):
    p = var('p')
    f = e*leak*p -k*p*(N - p + 1) + k*N - p
    result = solve_mod([f==0], 2**t)
    for root in result:
        root = ZZ(root[0])
        p_hi = PolynomialRing(Zmod(N),'p_hi').gen()
        k = p_hi*2**t + root
        k = k.monic()
        roots = k.small_roots(X=2**(16), beta=0.49)
        if roots:
            p = int(roots[0]*2**t + root)
            q = N//p
            phi = (p-1)*(q-1)
            d = inverse(e,phi)
            m = pow(c,d,N)
            print(long_to_bytes(int(m)).decode())


