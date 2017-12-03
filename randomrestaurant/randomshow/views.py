from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from django.views import generic
from randomshow.models import TempRestaurant

from django.contrib.auth import get_user_model
User = get_user_model()

import random

class RandomshowList(generic.ListView):
    model = TempRestaurant

    template_name = 'randomshow/show.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     ran_choice = random.SystemRandom()
    #     ran_chosen = ran_choice.choice(queryset)
    #     print(ran_chosen)
    #     return ran_chosen
