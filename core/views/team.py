
from django.views import generic
from core.models import Team


class TeamView(generic.DetailView):
    """
    TeamView used for our Team page

    **Template:**
    :template:'core/team.html'
    """
    model = Team
    template_name = "core/team.html"
    paginate_by = 10

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs['slug'])
