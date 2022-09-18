import datetime
import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from shortner.models import Url


def shorten(request):
    if request.user.is_authenticated:
        return render(request, 'shortner/shorten.html')
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        hash_ = hashlib.md5()
        hash_.update(url.encode())
        hash_.update(request.user.username.encode())
        short_id = hash_.hexdigest()[:10]
        new_url = Url(link=url, short_id=short_id,
                      created_at=datetime.date.today(),
                      expires_at=datetime.date.today() + datetime.timedelta(days=14),
                      created_by=request.user)
        new_url.save()
        return HttpResponse(short_id)


def redirect_url(request, short_id):
    print(request.META.get('REMOTE_ADDR'), request.META.get('HTTP_X_FORWARDED_FOR'))
    url_details = Url.objects.get(short_id=short_id)
    return redirect(url_details.link)
