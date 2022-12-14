from django.shortcuts import render
from four_app.models import Examination


def images(request):
    context = Examination.objects.all()
    return render(template_name='indez.html', request=request, context={"exam_list": context})
# Create your views here.
