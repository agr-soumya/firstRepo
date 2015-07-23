import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import django.core.exceptions
class RegistrationForm(forms.Form):
	
	enrolment_no = forms.IntegerField(widget = forms.NumberInput(attrs = dict(required = True)),label = _("enrolment no"), error_messages = {'invalid': _("This value must be an integer")})
	password1 = forms.CharField(widget = forms.PasswordInput(attrs = dict(required = True, render_value = False)), label = _("Password"))
	password2 = forms.CharField(widget = forms.PasswordInput(attrs = dict(required = True, render_value = False)), label = _("Password Again"))
#	def clean_enrolment_no(self):
#		raise forms.ValidationError(_(self.cleaned_data['password1']+" " + self.cleaned_data['password2']))
#		try:
#			user = User.objects.get(username__iexact = self.cleaned_data['enrolment_no'])
#		print ('Clean_enrolment_no running')
#			print self.cleaned_data['enrolment_no']
#		except User.DoesNotExist:
#			return self.cleaned_data['enrolment_no']
#		raise forms.ValidationError(_("The enrolment no already exists"))

#	def clean(self):
#		print ('clean self running')
#		print self.cleaned_data['password1']
#		print self.cleaned_data['password2']
#		print self.cleaned_data['enrolment_no']
#		raise forms.ValidationError(_(self.cleaned_data['password1']+" " + self.cleaned_data['password2']))

#		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
#		if self.cleaned_data['password1']!=self.cleaned_data['password2']:
#			print('True')
#			raise ValidationError(_('Passwords do not match'))
#		return self.cleaned_data

class UserProfile(forms.Form):
	email = forms.EmailField(widget = forms.EmailInput(attrs = dict(required = True)), label = _("Email Id"))
	phone = forms.IntegerField(widget = forms.NumberInput(attrs = dict(required = True)),label = _("phone"), error_messages = {'invalid': _("This value must be an integer")})
