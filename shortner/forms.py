from django.forms import ModelForm

from shortner.models import urlShortner


class urlForm(ModelForm):
    class Meta:
        model = urlShortner
        fields = ("url",)