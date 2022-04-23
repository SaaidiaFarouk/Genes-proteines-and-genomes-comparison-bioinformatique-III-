from collections import defaultdict


def defdict():
    return []


def reverse_complement(seq):
    """
    reverse complement of a sequence, which is the other strand the seq binds to
    """
    dct = {"A": "T", "T": "A", "C": "G", "G": "C"}
    mer = ""
    for char in seq:
        mer = dct[char] + mer
    return mer


def shared_kmers(k, sta, stb):
    """
    get all shared k-mers between sta and stb
    """

    b_dct = defaultdict(defdict)
    for i, _ in enumerate(stb[: -k + 1]):
        b_dct[stb[i : i + k]].append(i)

    matches = []
    for i, _ in enumerate(sta[: -k + 1]):
        match = sta[i : i + k]
        rev_match = reverse_complement(match)

        for compare in (match, rev_match):
            if compare in b_dct.keys():
                for v in b_dct[compare]:
                    matches.append((i, v))

    return matches



if __name__ == "__main__":
    with open("dataset.txt","r") as f : 
        k=f.readline()
        k=int(k)
        sta=f.readline()
        stb=f.readline()
        sta=sta.rstrip("\n")
        stb=stb.rstrip("\n")
    

    out = shared_kmers(k, sta, stb)
    
    print(len(set(out)))
with open("answear.txt","w") as d : 
    for a in out :
        stro="("
        stro+=str(a[0])
        stro+=", "
        stro+=str(a[1])
        stro+=")"
        d.write(stro)
        if out.index(a)!=len(out)-1:
            d.write("\n")

