from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    full_text = request.GET['fulltext']

    word_split = full_text.split()

    word_dictionary = {}

    for word in word_split:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'count.html', {'fulltext':full_text, 'total':len(word_split), 'dictionary':word_dictionary.items})