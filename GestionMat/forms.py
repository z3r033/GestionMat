from django import forms
from django.contrib.auth.models import User

from GestionMat.models import material


class LoginForm(forms.Form):
 if not User.objects.all():
  user = User.objects.create_user('admin', 'admin@admin.com', 'admin')
  user.is_staff = True
  user.is_superuser = True
  user.save()
 username = forms.CharField()
 password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
 class Meta:
  model = User
  fields = ('username','first_name', 'last_name', 'email')

class UserRegistrationForm(forms.ModelForm):
 password = forms.CharField(label='Password',
 widget=forms.PasswordInput)
 password2 = forms.CharField(label='Repeat password',
 widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ('username', 'first_name', 'email')
 def clean_password2(self):
  cd = self.cleaned_data
  if cd['password'] != cd['password2']:
   raise forms.ValidationError('Passwords don\'t match.')
  return cd['password2']



MAINTENANCE_CHOICES = (
 (True, "Oui"),
 (False, "Non"),
 )
class MaterialForm(forms.ModelForm):
 numero_serie = forms.CharField(label='Numéro de série')
 date_achat = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
 garantie_duree = forms.IntegerField(label="duree de garantie")
 achat_lieu = forms.CharField(label="lieu d'achat")
 achat_prix=forms.DecimalField(label="achat prix",max_digits=9, decimal_places=2)
 marque= forms.CharField(label="marque")
 date_derniere_maintenance = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
 contrat_maintenance= forms.ChoiceField(label="contrat maintenance",choices=MAINTENANCE_CHOICES,required=True,widget = forms.Select(attrs = {'onclick' : "hideorshow",}))
 duree= forms.IntegerField(label="duration")
 lieu_affectation = forms.CharField(label="lieu d'affectation")
 editeur = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select, required=True)

 class Meta:
  model= material
  fields = ('numero_serie','date_achat','garantie_duree','achat_lieu','achat_prix','marque','date_derniere_maintenance','contrat_maintenance',
            'duree','lieu_affectation','editeur')
 @property
 def media(self):
        media = super(MaterialForm, self).medi
        js = ('/static/js/hideshow.js',)
        media.add_js(js)
        return media

YEARS= [x for x in range(1940,2040)]
class MaterialUpdateForm(forms.ModelForm):
 numero_serie = forms.CharField(label='Numéro de série')
 date_achat = forms.DateField( required=True,
        widget=forms.TextInput(
            attrs={'type': 'date'}))
 garantie_duree = forms.IntegerField(label="duree de garantie")
 achat_lieu = forms.CharField(label="lieu d'achat")
 achat_prix=forms.DecimalField(label="achat prix",max_digits=9, decimal_places=2)
 marque= forms.CharField(label="marque")
# date_derniere_maintenance = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
 date_derniere_maintenance = forms.DateField( required=True,
        widget=forms.TextInput(
            attrs={'type': 'date'}))


 contrat_maintenance= forms.ChoiceField(label="contrat maintenance",choices=MAINTENANCE_CHOICES,required=True,widget = forms.Select(attrs = {'onclick' : "hideorshows",}))
 duree= forms.IntegerField(label="duration")
 lieu_affectation = forms.CharField(label="lieu d'affectation")
 editeur = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select, required=True)

 class Meta:
  model= material
  fields = ('numero_serie','date_achat','garantie_duree','achat_lieu','achat_prix','marque','date_derniere_maintenance','contrat_maintenance',
            'duree','lieu_affectation','editeur')
 @property
 def media(self):
        media = super(MaterialUpdateForm, self).medi
        js = ('/static/js/hideshow.js',)
        media.add_js(js)
        return media






#class SearchForm(forms.Form):
# query = forms.CharField()

class SearchForm(forms.Form):
   query = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))