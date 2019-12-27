from django.shortcuts import render
from Post.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

# def Index(request):

#     if request.user.is_authenticated:
#         post=Post.objects.filter(author=request.user).all()
#         post_count=Post.objects.filter(author=request.user).count()
#         pending_count=Post.objects.filter(status=0,author=request.user).count()
#         admin_pending_count=Post.objects.filter(status=0).exclude(author=request.user).count()

#         context= {
#             "post":post,
#             "pending_count":pending_count,
#             "admin_pending_count":admin_pending_count,
#             "post_count":post_count,
#         }
#         return render(request,'index.html',context)

#     return render(request,'index.html',{})



class Index(LoginRequiredMixin,ListView):
    login_url = 'account/login/'
    redirect_field_name = 'login'
    model = Post
    paginate_by=2
    context_object_name ='post'
    template_name="index.html"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).all()

        