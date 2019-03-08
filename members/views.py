from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import operator
from django.db.models import Q

from .models import Member

class MemberIndexView(generic.ListView):
    template_name = 'members/index.html'
    context_object_name = 'latest_member_list'
    def get_queryset(self):
        """
        Return the member names.
        """
        query = self.request.GET.get('q')
        if query:
            return Member.objects.filter(Q(last_name__contains=query)|Q(first_names__contains=query)).order_by('first_names', 'last_name')
        else:
            return Member.objects.all().order_by('first_names', 'last_name')

class MemberDetailView(generic.DetailView):
    model = Member
    fields = ['last_name', 'first_names', 'date_of_birth', 'gender']
    template_name = 'members/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Member.objects.all()