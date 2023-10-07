from django.views import generic
from core.models import Blog


class BlogsView(generic.ListView):
    """
    List view used for our Blogs page.
    **Template: **
    :template: 'core/blogs.html'
    """
    model = Blog
    template_name = "core/blogs.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
