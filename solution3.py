import numpy as np

def get_indices(N, n_batches, split_ratio):
    """Generates splits of indices from 0 to N-1 into uniformly distributed\
       batches. Each batch is defined by 3 indices [i, j, k] where\
       (j-i) = split_ratio*(k-j). The first batch starts with i = 0,\
       the last one ends with k = N - 1.
    Args:
        N (int): total counts
        n_batches (int): number of splits
        split_ratio (float): split ratio, defines position of j in [i, j, k].

    Returns:
        generator for batch indices [i, j, k]
    """
    inds = np.array([0, 0, 0])
    s=0.2
    j=0.2
    k=1
    #while ((s%10)!=0) or ((j%10)!=0):
     #   s=(99-k)/4
      #  j=k - 0.2*k
       # k=k+1
    counterS=1
    for k in range(N):
        s=(99-k)/4
        j=0.8*k
        if (s.is_integer()) and (j.is_integer()):
            for st in range(4):
                if ((st+1)*s < (k+s*st)):
                    counterS = 0
                else: counterS = 1
            if (counterS == 0):
                break
    #k=k-1
    #while ((j%10)!=0):
     #   s=(99-k)/4
      #  j=k - 0.2*k
       # k=k+1
    print (s)
    print (j)
    #k=k-1
    for i in range(n_batches):
        step=s*i
        inds[0]=step
        inds[1]=0.8*k + step
        inds[2]=k+step
        # todo: move forward batch
        # calculate new indices
        yield inds

def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]

if __name__ == "__main__":
    main()