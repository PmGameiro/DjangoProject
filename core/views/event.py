from django.views import generic
from core.models import Event


class EventView(generic.DetailView):
    """
    DetailView used for our Event page

    **Template:**
    :template:'core/event.html'
    """
    model = Event
    template_name = "core/event.html"
    paginate_by = 10

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs['slug'])
