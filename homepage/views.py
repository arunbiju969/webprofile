from django.shortcuts import render
from .models import About, Certificates, Contact
from django.views.generic.base import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = About.objects.first()
        certificates = Certificates.objects.all()
        social = Contact.objects.all()
        context["about"] = about
        context["certificates"] = certificates
        context["social"] = social
        return context
    
