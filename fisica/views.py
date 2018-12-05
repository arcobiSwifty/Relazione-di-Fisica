import numpy
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound

from django.shortcuts import render
from .models import Misurazione, Esperimento

# Create your views here.
def home(request, nomeesperimento):
    es = Esperimento.objects.get(name=nomeesperimento)
    return render(request, "home.html", {"esperimento": es})

def default(request):
    es = Esperimento.objects.get(name="Esperimento1")

    #v = (math.sqr(2gh))
    #h = 5 +/- 0,5

    xs = list()
    ys = list()

    for x in range(1, 13):
        s1 = "es.es{0}.lunghezza".format(x)
        xs.append(float(eval(s1)))
        s2 = "es.es{0}.media".format(x)
        ys.append(float(eval(s2)))

        #obj = Misurazione.objects.get(lunghezza=eval(s1))
        #obj.salva()
        #obj.save()


    z = numpy.polyfit(xs, ys, 1)
    p = numpy.poly1d(z)
    print("z", z)
    print("p", p[0])
    return render(request, "home.html", {"es": es})

def do_polyfil(request):
    xs_Data = request.POST.getlist("xs[]", "")
    ys_Data = request.POST.getlist("ys[]", "")
    xs_Data = list(map(lambda x: float(x), xs_Data))
    ys_Data = list(map(lambda x: float(x), ys_Data))
    z = numpy.polyfit(xs_Data, ys_Data, 1)
    p = numpy.poly1d(z)
    print(z[0], z[1])
    return JsonResponse({"m": z[0], "k": p[1]})
