from django.views import generic
from core.models import Policy


class PolicyView(generic.DetailView):
    """
    DetailView used for our Policy page

    **Template:**
    :template:'core/policy.html'
    """
    model = Policy
    template_name = "core/policy.html"
    paginate_by = 10

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs['slug'])
