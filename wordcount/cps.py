from django.http import HttpResponse
from django.shortcuts import render

def count(request):
    fulltext=request.GET['fulltext']
    sp=fulltext.split()
    #print(fulltext)
    worddic={}
    for x in sp:
        if x in worddic:
            worddic[x]=worddic[x]+1
        else:
            worddic[x]=1
    for c,d in worddic.iteritems():
        print c
        print d
    return render(request,'count.html',{'worddic':worddic,'fulltext':fulltext})
def address(request):
    return render(request,'home.html',{'dic':'Be Honest'})
