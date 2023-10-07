from django.views import generic


class AboutView(generic.TemplateView):
    """
    Template view used for our about page.
    **Template: **
    :template: 'core/about.html'
    """
    template_name = "core/about.html"
