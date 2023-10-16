from .models import post
from django.views import generic

class postlist(generic.ListView):
    model=post

    #1-- compiler looking for (post_list ااو Object_list)
    #2-- Template: Post_list.html

class postdetail(generic.DetailView):
    model=post


class addpost(generic.CreateView):
    model=post
    fields=['author','title','content','image','tags']
    success_url='/blog/'
    

class editpost(generic.UpdateView):
    model=post
    fields=['author','title','content','image','tags']
    success_url='/blog/'
    template_name='posts/edit.html'



class deletepost(generic.DeleteView):
    model=post
    success_url='/blog/'
        
        