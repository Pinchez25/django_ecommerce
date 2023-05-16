### A Django e-commerce project

```python
   def user_registration(request):
       if request.method == 'POST':
           form = UserRegistrationForm(request.POST)
           if form.is_valid():
               cd = form.cleaned_data
               user = form.save(commit=False)
               user.set_password(cd['password'])
               user.save()
               return render(request, 'account/register_done.html', {'user': user})
       else:
           form = UserRegistrationForm()
       return render(request, 'account/register.html', {'form': form}
```