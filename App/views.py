from django.shortcuts import render

def test(request):
    return render(request,'samplewebpage.html')
def test1(request):
    return render(request,'gridex.html')
def test2(request):
    return render(request,'ex2.html')
def final(request):
    return render(request,'FinalProject.html')