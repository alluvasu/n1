from django.shortcuts import render
from a1.forms import SignUpForm

def BookInfo(f):
    form=SignUpForm()
    if f.method=="POST":
        form=SignUpForm(f.POST)
        if form.is_valid():
            print("form is valid")
            print('name:',form.cleaned_data['name'])
            print('psw:',form.cleaned_data['psw'])
            print('rpsw:',form.cleaned_data['rpsw'])
    my_dict={'form':form}
    return render(f,'a1/index.html',context=my_dict)

# Create your views here.
