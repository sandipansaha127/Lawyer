from django.shortcuts import render, get_object_or_404
from .models import Category, Lawyer
from lawyer.forms import CategoryForm,LawyerForm
from django.contrib.auth.decorators import login_required

@login_required
def Home(request):
    return redirect('lawyer_list')
    # from lawyer.forms import CategoryForm,LawyerForm
    # context = {
    # 'category_form': CategoryForm(),
    # 'lawyer_form': LawyerForm(),
    # }
    # if request.user.profile.role == "LAWYER":
    #     return render(request, 'registration/lawyer_registration.html', context)

    # return redirect('lawyer_list')
def lawyer_save(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST)
        if cat_form.is_valid():
            cat_obj = cat_form.save(commit=False)
            cat_obj.profile = request.user.profile
            cat_obj.save()
            return HttpResponseRedirect('/')

def lawyer_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    lawyers = Lawyer.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        lawyers = Lawyer.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'lawyers': lawyers
    }
    return render(request, 'lawyer/list.html', context)


def lawyer_detail(request, id, slug):
    lawyer = get_object_or_404(Lawyer, id=id, slug=slug, available=True)
    context = {
        'lawyer': lawyer
    }
    return render(request, 'lawyer/detail.html', context)