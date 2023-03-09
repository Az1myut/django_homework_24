from itertools import chain

from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from articles.models import Article, Comment
from testimonials.models import Testimonial

from icecream import ic


# Create your views here.
class SearchResultsView(View):
    """
    Поиск по сайту
    """

    template_name = "search/search_results.html"


    def get(self, request, *args, **kwargs):
        return self.get_queryset(request, *args, **kwargs)
    
    def get_queryset(self, request, *args, **kwargs):
        context = {}
 
        q = request.GET.get('q')
        if q:
            query_sets = []  # QuerySet
 
            # Searching for all models

            query_sets.append(Article.objects.search(query=q))
            query_sets.append(Comment.objects.search(query=q))
            query_sets.append(Testimonial.objects.search(query=q))

 
            # Формируем смешанный вывод
            final_set = list(chain(*query_sets))
            final_set.sort(key=lambda x: x.updated_at, reverse=True)  # Сортировка

            context['query'] = f'?q={q}'

            current_page = Paginator(final_set, 2, orphans=1)

            page = request.GET.get('page')
            try:
                context['object_list'] = current_page.page(page)
            except PageNotAnInteger:
                context['object_list'] = current_page.page(1)
            except EmptyPage:
                context['object_list'] = current_page.page(current_page.num_pages)
 
        return render(request=request, template_name=self.template_name, context=context)