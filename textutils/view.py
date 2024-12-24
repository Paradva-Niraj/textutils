# file created by admin for redirection a pages

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'nicxx'}
    return render(request,'index.html',params)
    # return HttpResponse("<h2>hello from nicxx</h2>")

# def removepunc(request):
#     text=request.GET.get('text')
#     analyzed=""
#     punc=""".,!?;:"'()[]{<>}-–—…"""
#     for i in text:
#         if i not in punc:
#             analyzed+=i
#     params={'analyzed':analyzed}
#     return render(request,'displaypuch.html',params)
    
# def capitalizefirst(request):
#     return HttpResponse("<h3>from capitalize</h3>")
    
# def newlineremove(request):
#     return HttpResponse("<h3>from newlineremover</h3>")
    
# def spaceremove(request):
#     return HttpResponse("<h3>spaceremove</h3>")
    
# def charcount(request):
#     return HttpResponse("<h3>from char count</h3>")


def textutils(request):
    text=request.GET.get('text','')
    req=request.GET.get('action','')
    print(req)
    if (req == 'remove_punct'):
        analyzed=""
        punc=""".,!?;:"'()[]@{<>}-–—…"""
        for i in text:
            if i not in punc:
                analyzed+=i
        params={'analyzed':analyzed}
        return render(request,'displaypuch.html',params)
    elif (req == 'uppercase'):
        analyzed=text.upper()
        params={'uppercase':analyzed}
        return render(request,'uppercase.html',params)
    elif (req == 'lowercase'):
        analyzed=text.lower()
        params={'lowercase':analyzed}
        return render(request,'lowercase.html',params)
    elif (req == 'word_count'):
        list=[]
        count=[]
        c=0
        for i in text:
            if(i not in list):
                list.append(i)
                count.append(text.count(list[c]))
                c+=1
        data=zip(list,count)
        params={'data':data}
        return render(request,'count.html',params)

