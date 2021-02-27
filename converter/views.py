from django.shortcuts import render

def home(request):

    return render(request, 'converter/home.html')

def converter(request):

        currency = float(request.GET.get('currency', 1))

        sr = currency * 0.077
        jyp = currency * 2.19
        us = currency * 0.041
        cd = currency * 0.026
        uae = currency * 0.075


        return render(request, 'converter/converter.html', {

        'sr': sr,
        'jyp': jyp,
        'us': us,
        'cd': cd,
        'uae': uae,





        })


