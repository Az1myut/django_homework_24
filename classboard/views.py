from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Classboard
from students.models import Group, Student
from subjects.models import SubjectByDayChoices, SubjectPairChoices
from django.views.generic.base import TemplateView
from icecream import ic
# Create your views here.


def filters_students_options(request, pk=None):
    if request.method == "POST":
        filter_q = Q(group__pk=request.POST.get("group_choice"))
        if request.POST.get("pair_choice"):
            filter_q &= Q(class_pair=request.POST.get("pair_choice"))
        if request.POST.get("day_choice"):
            filter_q &= Q(class_day=request.POST.get("day_choice"))

        return (
            Classboard.objects.filter(filter_q)
            .prefetch_related("teacher")
            .select_related("subject_name", "group")
        )

    return (
        Classboard.objects.all()
        .prefetch_related("teacher")
        .select_related("subject_name", "group")
    )


def classboard_view(request, pk=None) -> render:
    """
    Отображает пару "предмет - учитель" или, при наличии параметрах
    пути pk, конкретную пару "предмет - учитель"

    """
    if not pk:
        template_ = "classboard_all.html"

        classboard_all = filters_students_options(request)

        context = {
            "classboard_all": classboard_all,
            "group": Group.objects.all(),
            "days": SubjectByDayChoices.choices,
            "pair": SubjectPairChoices.choices,
        }
    else:
        template_ = "classboard_item.html"

        classboard_current = get_object_or_404(Classboard, pk=pk)
        students_filter_q = Q(group_id=classboard_current.group)
        students = Student.objects.filter(students_filter_q).select_related("group")

        context = {
            "classboard_current": classboard_current,
            "students": students,
        }

    return render(request=request, template_name=template_, context=context)

class ShowWeekClassboardView(TemplateView):
    template_name = 'week_classboard.html'
   
    def get_data(self):
        groups = Group.objects.all()
        days = SubjectByDayChoices.choices
        # pairs = SubjectPairChoices.choices
        main_dict_classes = {}
        
        for group in groups:
            tmp_lst=[]
            for i in range(6):
                
                lst_with_dat_values = ['','','','','','','','',days[i][1]]
                tmp_lst.append(lst_with_dat_values)
            for classboard  in group.classboard_group.all():
                day = int(classboard.class_day) -1
                pair = int(classboard.class_pair) -1
                tmp_lst[day][pair] = classboard
                ic(tmp_lst)
            for lst in tmp_lst:
                day = lst.pop()
                lst.insert(0,day)
            main_dict_classes[group] = tmp_lst
        return main_dict_classes

        
             
    

    
            
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classboard_week'] = self.get_data()
        context['pairs'] = SubjectPairChoices.choices
        return context