from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView ,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



class HomePage(ListView):
    model = Post
    template_name = "home.html"

    context_object_name = "post_list"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = "__all__"



class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title', 'body']



class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url =  reverse_lazy('home')



class BlogDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    redirect_field_name = "accounts/login"


class BlogCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = "accounts/login"

class BlogUpdateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = "accounts/login"


