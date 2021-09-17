from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from shortner.forms import urlForm
from shortner.models import urlShortner, generate_public_id


@csrf_exempt
def list(request):
    if request.method=="GET":
        form=urlForm()
        return render(
            request, "shortner/input.html", {"form": form}
        )
    if request.method=="POST":
        data=request.POST['url']
        public_id=generate_public_id()
        url=urlShortner()
        url.public_key=public_id
        url.url=data
        url.save()
        form = urlForm()
        host = request.get_host()
        print(host)
        new_url=host+"/"+public_id
        print(data)
        return render(
            request, "shortner/input.html", {"form": form,"new_url":new_url}
        )


@csrf_exempt
def search(request, public_id):
    url=urlShortner.objects.filter(public_key=public_id).first()

    return redirect(url.url)
