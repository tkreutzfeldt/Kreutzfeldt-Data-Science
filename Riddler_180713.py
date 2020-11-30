import operator as op
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom

prob = 0;

for ii in range(0,5):
    make = ii;
    miss = ii - 5;
    
    ind_prob = (ncr(5,make) * 0.75^make * 0.25^miss)^2
    out = 'Probability of tie with ' + repr(make) + '(s): ' + repr(ind_prob)
    print(out)
    prob = prob + ind_prob

out = 'Probability of tie:' + repr(make)
print(out)