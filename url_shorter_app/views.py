from django.db.models import F
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, RedirectView

from .models import RedirectModel
from .services import generate_short_url


class RedirectListView(ListView):
    model = RedirectModel
    template_name = "url_shorter_app/index.html"
    context_object_name = 'objects'


class RedirectCreateView(CreateView):
    model = RedirectModel
    fields = ['target_url', ]
    template_name = "url_shorter_app/create_url.html"

    def form_valid(self, form):
        form.short_path = generate_short_url(self.model, 'short_path')
        return super().form_valid(form)


class RedirectCounterView(RedirectView):
    permanent = False

    def dispatch(self, request, *args, **kwargs):
        short_path = kwargs['short_path']
        RedirectModel.objects.filter(short_path=short_path).update(redirect_counter=F("redirect_counter") + 1)
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        short_path = kwargs['short_path']
        redirect_page = get_object_or_404(RedirectModel, short_path=short_path)
        return redirect_page.target_url


class RedirectDetailView(DetailView):
    model = RedirectModel
    slug_field = 'short_path'
    slug_url_kwarg = 'short_path'
    template_name = "url_shorter_app/detail.html"
    context_object_name = 'object'
