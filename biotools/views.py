from django.shortcuts import render
from .forms import SeqContentForm, RevComp
from . import utils 
from .utils import rev_comp
# Create your views here.
def seqcontent_view(request):
    if request.method == 'POST':
        form = SeqContentForm(request.POST)
        if form.is_valid():
            seq = form.cleaned_data['sequence']
            word_size = form.cleaned_data['word_size']
            d = utils.count_words(seq, word_size)
            seq_len = len(seq)
            return render(request, 'biotools/seqcontent.html', {'results': d, 'seq_len': seq_len})
    else:
        form = SeqContentForm()

    return render(request, 'biotools/seqcontent.html', {'form': form})


def revcomp_view(request):
    if request.method == 'POST':
        form = RevComp(request.POST)
        if form.is_valid():
            seq = form.cleaned_data['sequence']
            results = rev_comp(seq)
            return render(request, 'biotools/revcomp.html', {'results': results, 'seq': results['original'], 'reverse_seq': results['reverse_complement']})
    else:
        form = RevComp()

    return render(request, 'biotools/revcomp.html', {'form': form})

