from django.shortcuts import render
from django.shortcuts import HttpResponse
from datadisplay.forms import filterform
from datadisplay.models import winedata
from  datadisplay.forms import loginform
from datadisplay.models import logininfo
# Create your views here.

def key(item):
    return item.price

def datadisplay(request):
    if request.method == "POST":
        filterdata = filterform(request.POST)
        filt = filterdata.data['filter']

        sortcheck = filterdata.data['sortcheck']
        print(sortcheck)
        if filt == "dispall" and sortcheck=='on':
            dispobj = winedata.objects.all()
            return render(request, "display.html", {"results": dispobj})
        elif filt == "dispall" and sortcheck=="nosort":
            dispobj = winedata.objects.all()
            return render(request, "display.html", {"results": dispobj})
        if filterdata.is_valid():
             filt = filterdata.cleaned_data['filter']
             val = filterdata.cleaned_data['value']
             sortcheck = filterdata.cleaned_data['sortcheck']
             print('WORKING')

             if (sortcheck == "on"):
                 if filt == "country":
                     dispobj = winedata.objects.filter(country=val).order_by('price')
                     print(dispobj)
                 elif filt == "winery":
                     dispobj = winedata.objects.filter(winery=val).order_by('price')
                 elif filt == "designation":
                     dispobj = winedata.objects.filter(designation=val).order_by('price').all()
                 elif filt == "province":
                     dispobj = winedata.objects.filter(province=val).order_by('price').all()
             else:
                if filt == "country":
                    dispobj = winedata.objects.filter(country=val)
                elif filt == "winery":
                    dispobj = winedata.objects.filter(winery=val)
                elif filt == "designation":
                    dispobj = winedata.objects.filter(designation=val)
                elif filt == "province":
                    dispobj = winedata.objects.filter(province=val)
             if dispobj:

                 return render(request, "display.html", {"results": dispobj})
             else:
                 return HttpResponse("""<h1>Search query returned empty set</h1>""")
        else:
            return HttpResponse("""<h1>Invalid query details</h1>""")
    else:
        return HttpResponse("""<h1>Please use POST method</h1>""")

def login(request):
    if request.method == "POST":
        logindata = loginform(request.POST)
        if logindata.is_valid():
            username = logindata.cleaned_data['username']
            password = logindata.cleaned_data['password']
            loginobj = logininfo.objects.get(username=username)
            if loginobj!=None and loginobj.password==password:
                return render(request,"datadisplay.html")
            else:
                return HttpResponse("""Toro""")
        else:
            return HttpResponse("""<script> alert("Invalid Credentials"); </script>""")
def firstpage(request):
    return render(request, "login.html")


