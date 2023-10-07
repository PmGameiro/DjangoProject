from django.views import generic
from core.models import Contact
from core.forms import ContactForm


class ContactView(generic.FormView):
    """
    FormView used for our Contact page

    **Template:**
    :template:'core/blog.html'
    """
    form_class = ContactForm
    template_name = "core/contact.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)
