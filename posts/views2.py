from .models import post
from django.views import generic

class postlist(generic.ListView):
    model=post

    #1-- compiler looking for (post_list ااو Object_list)
    #2-- Template: Post_list.html

class postdetail(generic.DetailView):
    model=post    