from django import forms
 
class CafeForm(forms.Form):
	Nombre = forms.CharField(max_length=100)
	Stock = forms.CharField(max_length=100)
	Descripcion = forms.CharField(widget=forms.Textarea)#campo de tipo textarea 
