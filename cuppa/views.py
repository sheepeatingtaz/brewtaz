from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, FormView

from cuppa.forms import NameForm, NotesForm
from cuppa.models import Brew


class Home(TemplateView):
    template_name = 'index.html'


class Sugars(TemplateView):
    template_name = 'sugars.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beverage'] = self.kwargs.get('beverage')
        return context


class Milk(Sugars):
    template_name = 'milk.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sugars'] = self.kwargs.get('sugars')
        return context


class Who(FormView):
    template_name = 'name.html'
    form_class = NameForm

    def get_success_url(self):
        url = reverse_lazy("cuppa:notes", kwargs={
            'beverage': self.kwargs.get('beverage'),
            'sugars': self.kwargs.get('sugars'),
            'milk': self.kwargs.get('milk'),
            'name': self.request.POST.get('your_name'),
        })

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beverage'] = self.kwargs.get('beverage')
        context['sugars'] = self.kwargs.get('sugars')
        context['milk'] = self.kwargs.get('milk')
        return context


class Notes(Who):
    template_name = 'notes.html'
    form_class = NotesForm

    def get_success_url(self):
        return reverse_lazy("thanks", args=[self.brew])

    def form_valid(self, form):
        brew = Brew(
            name=self.kwargs.get('name'),
            beverage=self.kwargs.get('beverage'),
            sugars=self.kwargs.get('sugars'),
            milk=self.kwargs.get('milk'),
            notes=form.cleaned_data['notes']
        )
        brew.save()
        self.brew = brew.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.kwargs.get('name')
        return context


class Thanks(TemplateView):
    template_name = "thanks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brew'] = Brew.objects.get(pk=self.kwargs.get("brewid"))
        return context