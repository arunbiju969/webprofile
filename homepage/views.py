from django.shortcuts import render
from .models import About, Certificates, Contact, Projects, CatOneCards, CatTwoCards, CatThreeCards
from django.views.generic.base import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = About.objects.first()
        certificates = Certificates.objects.all()
        social = Contact.objects.all()
        projects = Projects.objects.first()
        cat_headings = [projects.cat_one_heading, projects.cat_two_heading,projects.cat_three_heading]
        cat_cards = [CatOneCards.objects.all(), CatTwoCards.objects.all(), CatThreeCards.objects.all()]
        cat_zip = zip(cat_headings, cat_cards)
      
    
        context["about"] = about
        context["certificates"] = certificates
        context["social"] = social
        context["projects"] = projects
        context["cat_zip"] = cat_zip
        return context
    
