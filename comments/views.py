from django.db.models import Count
from django.shortcuts import redirect, get_object_or_404, get_list_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Comment, City
from .forms import *


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('comment_list')


def load_cities(request):
    region_id = request.GET.get('region')
    cities = City.objects.filter(region_id=region_id).order_by('name')
    return render(request, 'city_dropdown_list.html', {'cities': cities})


class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
    context_object_name = 'comment_list'

    def get_queryset(self):
        return Comment.objects.all()


def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('comment_list')


def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    return render(request, 'comment_detail.html', {'comment': comment})


def stat(request):
    context = Comment.objects.values('region', 'region__name').annotate(number=Count('region')).\
        filter(number__gt=5).order_by('region')
    return render(request, 'stat.html', {'context': context})


def stat_region(request, region_id):
    context = get_list_or_404(Comment.objects.values('region__name', 'city', 'city__name').
                              filter(region_id=region_id).annotate(number=Count('city')).order_by('city'))
    return render(request, 'stat_region.html', {'context': context})
