from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def homePage(request):
    return render(request, "index.html")


def markSheet(request):
    if request.POST.get('m1') == "":
        return render(request, "marks.html", {'err': True})
    elif request.POST.get('m2') == "":
        return render(request, "marks.html", {'err': True})
    elif request.POST.get('m3') == "":
        return render(request, "marks.html", {'err': True})
    elif request.POST.get('m4') == "":
        return render(request, "marks.html", {'err': True})

    m1 = int(request.POST.get('m1'))
    m2 = int(request.POST.get('m2'))
    m3 = int(request.POST.get('m3'))
    m4 = int(request.POST.get('m4'))
    res = (m1+m2+m3+m4)
    data = {
        'marks1': int(request.POST.get('m1')),
        'marks2': int(request.POST.get('m2')),
        'marks3': int(request.POST.get('m3')),
        'marks4': int(request.POST.get('m4')),
        'result': res
    }
    return render(request, "marks.html", data)
