from django.shortcuts import render

def test(request):
    return render(request,'samplewebpage.html')
def test1(request):
    return render(request,'selectjq.html')
def calc(request):
    return render(request,'Calculator.html')
def final(request):
    return render(request,'FinalProject.html')
def finaladmin(request):
    return render(request,'adminside.html')
def finaluser(request):
    return render(request,'userside.html')
