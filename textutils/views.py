#  I have created this File
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'sashank','place':'Bhubaneswar'}

    return render(request,'index.html',params)
    #return HttpResponse("HOME")
def analyze(request):
    djtext = request.POST.get("text","default")
    remove = request.POST.get('removepunc','off')
    fullcap = request.POST.get('fullcap','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    #analyzed = djtext
    punctuations = '''!"#$%&'()*+,-./:;?@[\]^_`{|}~'''

    analyzed = ""
    if remove == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        djtext =analyzed
        param = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        
    if(fullcap == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        djtext =analyzed
        param = {'purpose' : 'changed to Uppercase','analyzed_text':analyzed}
    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if (char != '\n' and char !='\r'):
                analyzed += char
        djtext =analyzed
        param = {'purpose': 'New line removed', 'analyzed_text': analyzed}
    if(spaceremover == 'on'):
        analyzed = ""
        for char in djtext:
            if (char != ' '):
                analyzed += char
        djtext =analyzed
        param = {'purpose': 'Space removed', 'analyzed_text': analyzed}

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
         if not (djtext[index] == " " and djtext[index + 1] == " "):
            analyzed += char

            param = {'purpose': 'extra space removed', 'analyzed_text': analyzed, }
    
    return render(request,'analyze.html', param)

    

# def capitalizefirst(request):
#     return HttpResponse("capitalize first<br> <a href = '/' >Back</a>")
# def newlineremove(request):
#     return HttpResponse("newlineremove<br> <a href = '/' >Back</a>")
# def spaceremove(request):
#     return HttpResponse("<h1>spaceremove</h1><a href = '/' >Back</a>")
# def charcount(request):
#     return HttpResponse("charcount <br> <a href = '/' >Back</a>")