from django.views import generic
from core.models import Policy


class PoliciesView(generic.ListView):
    """
    List view used for our Policies page.
    **Template: **
    :template: 'core/policies.html'
    """
    model = Policy
    template_name = "core/policies.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
