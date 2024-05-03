#Customizing UserCreationForm

#If the default fields (username, password1, password2) are not sufficient and you want to add more
# fields like email, you will need to extend UserCreationForm. Here’s how you can customize it:

'''from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user   '''


#-------------------------------------------------------------------------------
#Yes, that's correct! Django includes built-in views and forms for common tasks like user authentication, 
#including login and logout functionalities. This is part of Django's authentication framework, 
#which makes it very convenient to implement authentication without having to write the views and forms 
#from scratch.

#Using Django's Built-in Authentication Views
#Here's a brief overview of how to use these built-in views:

#Login View
#Django provides a built-in LoginView that handles user login. You can use it by simply mapping it to a URL in your urls.py file:

'''from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    ...
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    ...
]
'''

#You will need to create a registration/login.html template for the login form. Here’s a simple 
#example of what that template might look like:


'''{% extends 'base.html' %}

{% block content %}
<h1>Login</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
{% endblock %}
'''

#Logout View
#Similarly, Django provides a LogoutView. Here's how you can use it:

'''urlpatterns = [
    ...
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),
    ...
]
'''

#This LogoutView will log the user out and then redirect them to the URL specified by next_page. 
#In this case, it redirects the user to the 'home' URL pattern after logging out.

#Customizing Authentication Views
#Although Django's default authentication views cover many use cases, you might want to customize 
#these to fit specific needs or to integrate better with the rest of your site's styling and user flow. 
#You can do this by subclassing the views and overriding their attributes or methods, or by providing 
#custom templates.



