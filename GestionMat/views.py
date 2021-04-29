from datetime import datetime, timedelta

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse

from .forms import MaterialForm, LoginForm, UserRegistrationForm, MaterialUpdateForm, UserEditForm
from .models import material
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger
from django.contrib.auth.decorators import login_required
from dateutil.relativedelta import relativedelta
from .forms import  SearchForm

# Create your views here.

@login_required
def materials_list(request):
 form = SearchForm()
 object_list = material.objects.all()
 paginator = Paginator(object_list, 2)  # 3 posts in each page
 page = request.GET.get('page')
 try:
  mats = paginator.page(page)
 except PageNotAnInteger:
 # If page is not an integer deliver the first page
  mats = paginator.page(1)
 except EmptyPage:
 # If page is out of range deliver last page of results
  mats = paginator.page(paginator.num_pages)
# materials = material.objects.all()
 return render(request,
 'Materials/list.html',
 {'page':page,
  'materials': mats,
   'form':form,
  'section': 'materials_list'})

@login_required
def material_detail(request,year,numero_serie):
 materia = get_object_or_404(material, publish__year=year,
 numero_serie=numero_serie)

# publish__year=year,
 #publish__month=month,
 #publish__day=day)
 return render(request,
 'Materials/detail.html',
 {'material': materia})

def user_login(request):
 if request.method == 'POST':
     form = LoginForm(request.POST)
     if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(request,
         username=cd['username'],
         password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated '\
                'successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
 else:
    form = LoginForm()
 return render(request, 'registration/login.html', {'form': form})


def enregistrer(request):
 if request.method == 'POST':
     user_form = UserRegistrationForm(request.POST)
     if user_form.is_valid():
        new_user = user_form.save(commit=False)
 # Set the chosen password
        new_user.set_password(
            user_form.cleaned_data['password'])
 # Save the User object
        new_user.save()
        return render(request,
            'registration/register_done.html',
            {'new_user': new_user})
 else:
    user_form = UserRegistrationForm()
    return render(request,
                   'registration/register.html',
                   {'user_form': user_form,
                    'section': 'enregistrer'})


@login_required
def addmaterial(request):
     if request.method == 'POST':
         material_form = MaterialForm(request.POST)
         if material_form.is_valid():
             # Create a new user object but avoid saving it yet
             new_material = material_form.save(commit=True)
             return render(request,
                           'Materials/addmat_done.html',
                           {'new_material': new_material})
     else:
         material_form = MaterialForm()
         return render(request,
                       'Materials/addmat.html',
                       {'material_form': material_form,
                        'section': 'addmaterial'})



@login_required
def removematerial(request,num_serie):
      materia = get_object_or_404(material,numero_serie=num_serie)
      if request.method == 'POST':
         materia.delete()
         return redirect(reverse('GestionMat:materials_list'))

      else:
         return render(request,
                       'Materials/delete_material.html',
                       {'martia': materia})


#@login_required
#def updatematerial(request,num_serie):
 #     materia = get_object_or_404(material,numero_serie=num_serie)
  #    if request.method == 'POST':
   #     material_form=MaterialUpdateForm(#instance=request.,
    #                                     data=request
     #                                    .POST)
      #  if material_form.is_valid():
       #     material_form.save()
     #   else:
      #      material_form = MaterialUpdateForm(#instance=request.
       #           data=request.POST)
        #return render(request,
         #              'Materials/editmat.html',
          #             {'martia':material_form })

@login_required
def updatemat(request, num_serie):
    materia = get_object_or_404(material, numero_serie=num_serie)
    material_form = MaterialUpdateForm(request.POST or None,
                        request.FILES or None, instance=materia)
    #material_form.fields["date_achat"].initial = datetime.strptime("07 June 2020", '%d %B %Y')

    #material_form.fields["date_achat"].initial =datetime.strptime( materia.date_achat , '%d %B %Y')
    #material_form.fields["date_derniere_maintenance"].initial =  datetime.strptime(materia.date_derniere_maintenance , '%d %B %Y')
   # material_form = MaterialUpdateForm(data=request.POST)

    if request.method == 'POST':
        #material_form = MaterialForm(request.POST)
        if material_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_material = material_form.save()

            return render(request,
                          'Materials/addmat_done.html',
                          {'new_material': new_material})
    else:
        return render(request,
                      'Materials/editmat.html',
                      {'materia': material_form,
                       'mat':materia,
                       'section': 'updatemat'})


@login_required
def dashboard(request):
 return render(request,
 'Materials/dashboard.html',
 {'section': 'dashboard'})


@login_required
def mat_search(request):
 form = SearchForm()
 query = None
 results = []


 if 'query' in request.GET:
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']

        all_objects=material.objects.all()

        startdate = datetime.today()
        enddate = startdate  + relativedelta(months=2)
  #      Sample.objects.filter(date__range=[startdate, enddate])
        results = []
        for mat in all_objects:
            qt=query - relativedelta(months=mat.duree)
            if(qt==mat.date_derniere_maintenance):
                if results:
                   results.append(material.objects.filter(date_derniere_maintenance=qt))
                else:
                    results=material.objects.filter(date_derniere_maintenance=qt)
            #if  results:
             #   break


     #   qt=datetime.date(year, month, day)
       # results = material.objects.filter(numero_serie=query)

            #.annotate(
       #     search=SearchVector('numero_serie', 'lieu_achat'),
   #)

 return render(request,'Materials/search.html',
 {'form': form,
 'query': query,
 'results': results})




@login_required
def garrenti_search(request):
 form = SearchForm()
 object_list = material.objects.all()
 results = []
 for mat in object_list:
            qt=mat.date_achat - relativedelta(years=mat.garantie_duree)
            if(qt<=mat.date_derniere_maintenance):
                if results:
                   results.append(material.objects.filter(date_achat__lte=qt,contrat_maintenance=False))
                else:
                    results=material.objects.filter(date_achat__lte=qt,contrat_maintenance=False)


 paginator = Paginator(results, 2)  # 3 posts in each page
 page = request.GET.get('page')
 try:
  mats = paginator.page(page)
 except PageNotAnInteger:
 # If page is not an integer deliver the first page
  mats = paginator.page(1)
 except EmptyPage:
 # If page is out of range deliver last page of results
  mats = paginator.page(paginator.num_pages)
# materials = material.objects.all()
 return render(request,
 'Materials/list.html',
 {'page':page,
  'materials': mats,
  'form':form})



@login_required
def edituser(request):
 if request.method == 'POST':
     user_form = UserEditForm(instance=request.user,
            data=request.POST)
     if user_form.is_valid():
        user_form.save()
 else:
    user_form = UserEditForm(instance=request.user)
 return render(request,
 'registration/edituser.html',
{'user_form': user_form})