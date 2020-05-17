from django.shortcuts import render


def cargo(request):
    return render(request, 'cargo/cargo.html')