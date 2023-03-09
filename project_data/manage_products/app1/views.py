from django.shortcuts import redirect, render
from .models import Company_data
# Create your views here.
def Company_login(request):
        if request.POST:
            em =request.POST['email']
            ps = request.POST['pass']
            # try:
            var =Company_data.objects.get(com_em= em)
            print(var)
            if var.com_pass == ps:
               request.session['comp_data'] = var.id
               return redirect('Comdashboard')
            else:
                return HttpResponse("<h1>wrong pw..!</h1>")
            # except:
            #     return HttpResponse("<h1>not registered..!</h1>")
        return render(request,'company/login/login.html')


def Company_regi(request):
    if request.POST:
        nm =request.POST['name']
        em =request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']
       
        try:
            var =Company_data.objects.get(com_em= em)
            return HttpResponse("<h1>emil id already registered..</h1>")
        except:
         if pass1 == pass2:
           obj = Company_data()
           obj.com_name = nm
           obj.com_em = em
           
           obj.save()
           return redirect('login')
         else:
            return print("wrong pass...     ")
    return render(request,'company/login/regi.html')

def Comdashboard(request):
    if 'comp_data' in request.session.keys():
        var =Company_data.objects.get(id = int(request.session['comp_data']))
        return render(request,'company/dash/index.html',{'USERS':User})
    else:
        return redirect('login')