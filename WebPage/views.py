# manually created file
from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    # params = {'name': 'harry', 'place': 'Mars'}
    return render(request, 'index.html')
# def removepunc (request):
#     return HttpResponse("This is punctuation <a href = '/'>Back</a>")
# def capfirst (request):
#     return HttpResponse('This is Capitalize')
# def newlineremove (request):
#     return HttpResponse('This is newline remover')
# def spaceremove (request):
#     return HttpResponse("This is spaceremover <a href = '/'>Back</a>")
# def charcount (request):
#     return HttpResponse('This is charcount')
