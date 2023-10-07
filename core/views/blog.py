from django.views import generic
from core.models import Blog


class BlogView(generic.DetailView):
    """
    DetailView used for our Blog page

    **Template:**
    :template:'core/blog.html'
    """
    model = Blog
    template_name = "core/blog.html"
    paginate_by = 10

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs['slug'])
