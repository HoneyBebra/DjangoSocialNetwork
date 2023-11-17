from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    return render(
        request,
        'account/dashboard.html',
        {'section': 'dashboard'}
    )


def images(request):
    return render(
        request,
        'account/images.html',
        {'section': 'images'}
    )


def people(request):
    return render(
        request,
        'account/people.html',
        {'section': 'people'}
    )
