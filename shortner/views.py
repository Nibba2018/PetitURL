import datetime
import hashlib

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from accounts.models import User
from shortner.models import Url

FREE_LIMIT = 5


def shorten(request):
    if request.user.is_authenticated:
        return render(request, 'shortner/shorten.html')
    return render(request, 'index.html')


@login_required
def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        if not request.user.has_premium and request.user.url_count >= FREE_LIMIT:
            return HttpResponse("LIMIT REACHED!!")

        hash_ = hashlib.md5()
        hash_.update(url.encode())
        hash_.update(request.user.username.encode())
        short_id = hash_.hexdigest()[:10]
        new_url = Url(link=url, short_id=short_id,
                      created_at=datetime.date.today(),
                      expires_at=datetime.date.today() + datetime.timedelta(days=14),
                      created_by=request.user)
        User.objects.filter(username=request.user.username).update(url_count=request.user.url_count + 1)
        new_url.save()
        return HttpResponse(f'{request.get_host()}/{short_id}')


def redirect_url(request, short_id):
    url_details = Url.objects.get(short_id=short_id)
    return redirect(url_details.link)


@login_required
def list_urls(request):
    username = request.user.username
    urls = Url.objects.filter(created_by__username=username)
    context = {
        'urls': urls
    }
    return render(request, 'shortner/list_urls.html', context)


@login_required
def delete_url(request, short_id):
    url = Url.objects.get(short_id=short_id)
    User.objects.filter(username=request.user.username).update(url_count=request.user.url_count - 1)
    url.delete()
    return HttpResponseRedirect(reverse('urls'))
