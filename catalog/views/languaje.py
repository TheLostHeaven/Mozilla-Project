from django.views import generic

from ..models.languaje import Language

class LanguageListView(generic.ListView):
    model = Language
    context_object_name = 'language_list'
    template_name = 'catalog/languaje/languaje_list.html'

class LanguageDetailtView(generic.DetailView):
    model = Language
    context_object_name = 'language_detail'
    template_name = 'catalog/languaje/languaje_detail.html'

class LanguageCreateView(generic.CreateView):
    model = Language
    fields = [
        'name',
    ]
    template_name = 'catalog/languaje/languaje_form.html'