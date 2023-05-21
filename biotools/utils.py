from Bio.Seq import Seq

def count_words(seq, word_size):
    d = {}
    seq_len = len(seq)
    for i in range(0, len(seq)- word_size + 1):
        word = seq[i:i+word_size]
        if word not in d:
            d[word] = {'count': 0, 'percent': 0}
        d[word]['count'] += 1
        d[word]['percent'] = d[word]['count']/seq_len*100

    return  d

def rev_comp(seq):
    d = {}
    original_seq = Seq(seq)
    d['original'] = str(original_seq)
    reverse_comp_seq = str(original_seq.reverse_complement())
    d['reverse_complement'] = reverse_comp_seq
    return d
