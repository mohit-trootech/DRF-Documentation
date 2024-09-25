from django.views.generic import TemplateView
from utils.constants import Templates


class IndexView(TemplateView):
    template_name = Templates.BASE.value


index_view = IndexView.as_view()


class AboutView(TemplateView):
    template_name = Templates.ABOUT.value


about_view = AboutView.as_view()
