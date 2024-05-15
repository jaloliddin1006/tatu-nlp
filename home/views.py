from django.shortcuts import render, redirect
from .short_names import words, shorts
from .utilits import check_word
from .sinonimlar import change_sinonim
from .ner_technology import ner
from .sinonim_antonim import change_antonim
# Create your views here.


def home(request):
    return render(request, 'home.html')

def check_words(matn):
    new_matn = []
    other = []
    for soz in matn.split():
        diffres = check_word([soz])
        # print(diffres, soz)
        if soz.lower() in shorts.keys():
            new_matn.append(shorts[soz.lower()])
        else:
            diffres = check_word([soz])
            
            if soz not in diffres:
                other.append(soz)
                
            new_matn.append(soz)
            
    return ' '.join(new_matn), other
    


def short_name(request):
    context = {}
    if request.method == 'POST':
        word = request.POST.get('short_name')
        correct = ""
        if word and word in words:
            check = True
            
        else:
            if word.upper() in words:
                correct = word.upper()
            check = False
        context = {
            'correct': correct,
            'value': word,
            'check': check
        }
    return render(request, 'index.html', context)




def sentence(request):
    context = {}
    if request.method == 'POST':
        matn = request.POST.get('short_name')
        new_word, other = check_words(matn)
        context = {
            'old': matn,
            'new_word': new_word,
            'other': other
        }
    return render(request, 'sentence.html', context)









def add_name(request):
    if request.method == 'POST':
        word = request.POST.get('short_name')
        words.append(word)

    return redirect('home')


def sinonim(request):
    
    context = {}
    if request.method == 'POST':
        sentence_ = request.POST.get('sentence')
        change = change_sinonim(sentence_.strip())
        context = {
            'change': change.split(),
            'old':str(sentence_)
        }
        
        return render(request, 'sinonim.html', context)
    return render(request, 'sinonim.html', context)



def ner_technology(request):
    context = {}
    if request.method == "POST":
        old_sentence = request.POST.get('sentence')
        new_text = ner(old_sentence)
        context = {
            'old': old_sentence,
            'new_data' : new_text
        }

        return render(request, 'ner_technology.html', context)
    return render(request, 'ner_technology.html', context)


def antonim(request):
    context = {}
    if request.method == 'POST':
        sentence_ = request.POST.get('sentence')
        change = change_antonim(sentence_)
        context = {
            'change': change,
            'old':str(sentence_)
        }
        
        return render(request, 'antonim.html', context)
    return render(request, 'antonim.html', context)