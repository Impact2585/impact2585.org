from django.shortcuts import render

from users.models import UserProfile
from django.contrib.auth.models import User

# Create your views here.

def register(request):
	context = RequestContent(request)

	registered = False

	if request.method = 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			registered = True

		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render_to_response(
		'login.html',
		{'user_form':user_form, "profile_form": profile_form, "registered": registered},
		context)
