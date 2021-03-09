
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''For Entertainment youtube video''',
             '''For Interaction Facebook''',
             '''For Insight   Ted Talk''',
             '''For Internship   Intenship''',
             ]
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    x=False
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext=analyzed
        x=True
        # params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext=analyzed
        x=True
        # params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # # Analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext=analyzed
        x=True
        # params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if (char != "\n" and char!="\r"):
                analyzed = analyzed + char
            else: print("no")    
        djtext=analyzed
        x=True
    if x:
        params = {'purpose': 'Analyzed Text', 'analyzed_text': djtext}
        # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")





