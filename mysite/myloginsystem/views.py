from django.shortcuts import render
from myloginsystem import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from myloginsystem.forms import RegistrationForm
from django.contrib.auth.models import User, AbstractUser
from django.views.generic.edit import UpdateView
from myloginsystem.models import MyProfile
from django.contrib.auth import get_user_model, authenticate,login
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def register(request):
#	if request.method == 'POST':
#		form = RegistrationForm(request.POST)
#		if form.is_valid():
#			user = User.objects.create_user(username = form.cleaned_data['enrolment_no'], password = form.cleaned_data['password1'],email = '')
#		return HttpResponseRedirect('/register/success/')
#	else:
#		form = RegistrationForm()
#		return render(request, 'registration/register.html',{'form':form} )
	if request.method =='POST':
		form = RegistrationForm(request.POST)
		
		try:
			u = get_user_model().objects.get(username = request.POST['enrolment_no'])
		except(get_user_model().DoesNotExist):
			print('User with specified userid doesnt exist')
			if(request.POST['password1']!=request.POST['password2']):
				return render(request, 'registration/register.html', {'form':form,'error_message': "Passwords do not match",
 })
			elif(form.is_valid()):
#			else:
#				return HttpResponse(request.POST['enrolment_no'])
				print(request.POST['enrolment_no'])
				print(request.POST['password1'])
				user = get_user_model().objects.create_user(form.cleaned_data['enrolment_no'], '', form.cleaned_data['password1'])
#				user = User.objects.create_user(request.POST['enrolment_no'],'', request.POST['password1'])
#				u = User.objects.get(username = form.cleaned_data['enrolment_no'])
				print (user.username)
				print('should return to success page now')
				new_user = authenticate(username=request.POST['enrolment_no'],password=request.POST['password1'])
				login(request, new_user)
                        	return HttpResponseRedirect('/myloginsystem/register/success/%d/' % user.username)

		else:
				return render(request, 'registration/register.html', {'form':form,'error_message': "Enrolment no already exists",
 })
		
#		if(request.POST['password1']!=request.POST['password2']):
#			return render(request, 'registration/register.html', {'form':form,'error_message': "Passwords do not match",
# })
#		elif (form.is_valid()):
#              		user = User.objects.create_user(username = form.cleaned_data['enrolment_no'], password = form.cleaned_data['password1'],email = '')
#       			return HttpResponseRedirect('/register/success/')
	else:
		form = RegistrationForm()
		return render(request,'registration/register.html', {'form':form,})


def SignUpProcessing(request):
	form = RegistrationForm()
	if(User.objects.get(pk = request.POST['enrolment_no'])):


		return render(request, 'registration/register.html', {'form':form,'error message': "Enrolment no already exists",
 })
	elif(request.POST['password1']!=request.POST['password2']):

		return render(request, 'registration/register.html', {'form':form,'error message': "Passwords do not match",
 })

	elif (form.is_valid()):
		user = User.objects.create_user(username = form.cleaned_data['enrolment_no'], password = form.cleaned_data['password1'],email = '')
		
	return HttpResponseRedirect('/register/success/'+user.username)

# @login_required
def home(request):
#	try:
#		u = request.user
#		return render(request , 'home.html', {'user':request.user})
#	except(User.DoesNotExist):
#		return render(request, '/login/')
#consider from here
	if request.user.is_authenticated():
		print('user is authenticated')
		return render(request , 'home.html', {'user':request.user})
	else:
		print('user is not authenticated. now redirecting')
		return HttpResponseRedirect('/myloginsystem/')
	return HttpResponse("you are at the home page")



@login_required
def logout_page(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponseRedirect('/myloginsystem/')

#def register_success(request):
#	 if request.user.is_authenticated():
#		u  = request.user
		
	        

#	       	elif (form.is_valid()):
#                userDetails = User.objects.create_user(username = form.cleaned_data['enrolment_no'], password = form.cleaned_data['password1'],email = '')
#       return HttpResponseRedirect('/register/success/')

class UpdateProfile(UpdateView):
    model = MyProfile
    fields = ['first_name', 'last_name','image',] # Keep listing whatever fields 
    # the combined UserProfile and User exposes.
    template_name = 'user_update.html'
    slug_field = 'username'
    slug_url_kwarg = 'slug'
    success_url = '/myloginsystem/home/'
    def user_passes_test(self, request):
        if request.user.is_authenticated():
	    print('request.user.isauthenticated')
            self.object = self.get_object()
            print('self.object = self.get_object')
            print((request.user.first_name))
            print(type(self.object))
            return self.object == request.user
        return False
    def dispatch(self, request, *args, **kwargs):
        #some other code to check 
	if not self.user_passes_test(request):
	
            print('user doesnt pass test')
            return HttpResponseRedirect('/myloginsystem/')
        return super(UpdateProfile, self).dispatch(
            request, *args, **kwargs)

def launch_page(request):
	if(request.user == None or request.user.is_anonymous()):
		print('request.user = none. now redirecting to login page')
		return HttpResponseRedirect('/myloginsystem/accounts/login')
	else:
		print(request.user)
		return HttpResponseRedirect('/myloginsystem/home/')

def password_change(request):
	if(request.method == 'POST'): 
		print('request method is post')
		form = PasswordChangeForm(user = request.user, data= request.POST)
		if(form.is_valid()):
			form.save()
			update_session_auth_hash(request, form.user)
	
#		if(request.user.check_password(request.POST['old_password'])):

#			request.user.set_password(request.POST['new_password'])i
#			request.user.save()
#			print('password has been reset')
#			return HttpResponse("Password Changed Successfully")
#		else:
#			error_message = 'old password does not match'
#			return render(request, 'changepassword.html',{'form' = form, 'error_message' = error_message })
	else:
		print('request method is not post')
		form = PasswordChangeForm(user = request.user)
		return render(request,'changepassword.html',{'form' : form } )
		
	

