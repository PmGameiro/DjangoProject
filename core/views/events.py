from django.views import generic
from core.models import Event


class EventsView(generic.ListView):
    """
    List view used for our Events page.
    **Template: **
    :template: 'core/events.html'
    """
    model = Event
    template_name = "core/events.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
