from django.shortcuts import render,redirect
from django.http import HttpResponse
from fishapp.models import fish
from fishapp.models import pfish
from fishapp.models import rfish
from . models import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models.aggregates import Sum

# Create your views here.
def windex2(request):
    data= fish.objects.all()
    data1 = pfish.objects.all()
    data5 = freg.objects.all()
    return render(request,'findex2.html',{'data':data,'data1':data1,'data5':data5})

def wproduct(request,category):
    if category == "all":
        data = pfish.objects.all()
    else:
        data = pfish.objects.filter(cate=category)
    return render(request,'fishpro.html',{'data':data})

def wabout(request):
    return render(request,'aboutpro.html') 

def wcontact(request):
    return render(request,'fcontact.html')   

def view_contact(request):
    if request.method == "POST" :
        message = request.POST.get('fmessage')
        name = request.POST.get('cname')
        email = request.POST.get('cemail')
        subject = request.POST.get('fsubject')
        data6 = Fview_contact(message=message,name=name,email=email,subject=subject)
        data6.save()
        return redirect('windex2')


def wcart(request):
    u = request.session.get('id')
    data7 = Fwcart.objects.filter(userid=u,status=0)
    total=Fwcart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'fcart.html',{'data7':data7,'total':total})  

def fish_cart(request,sid):
    if 'id' in request.session:
        total = request.POST.get('total')
        quantity = request.POST.get('quan')
        userid = request.POST.get('id')
        data7 = Fwcart(productid=pfish.objects.get(id=sid),quantity=quantity,total=total,userid=freg.objects.get(id=userid),status=0)
        data7.save()
        return redirect('wcart')   

@csrf_exempt
def cart_update(request):
    if request.method == "POST":
        cartid = request.POST.get('pid')
        q = request.POST.get('qty')
        print(q)
        p = request.POST.get('price')
        tot = float(q)*float(p)
        print(tot)
        Fwcart.objects.filter(id=cartid).update(total=tot,quantity=q)
    return HttpResponse()


def wdelete(request,did):
    data7=Fwcart.objects.filter(id=did)
    data7.delete()
    return redirect('wcart')

def wcheckout(request):
    u = request.session.get('id')
    data=Fwcart.objects.filter(userid=u,status=0)
    count=Fwcart.objects.filter(userid=u,status=0).count()
    total=Fwcart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'fcheckout.html',{'data':data,'count':count,'total':total}) 

def w_check(request):
    if request.method =="POST":
        fname = request.POST.get('fname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        u = request.session.get('id')
        order = Fwcart.objects.filter(userid=u,status=0)
        for i in order:
            data=FCheckout(cartid=Fwcart.objects.get(id=i.id),fname=fname,mobile=mobile,email=email,address=address)
            data.save()
            Fwcart.objects.filter(id=i.id).update(status=1)
    return redirect('windex2')

def viewcheck(request):
    u=request.session.get('id')
    pdata=Fwcart.objects.filter(userid=u,status=0) 
    count=Fwcart.objects.filter(userid=u,status=0).count() 
    total=Fwcart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'orderconform.html',{'pdata':pdata,'count':count,'total':total})

def Fdelete(request,cid):
    if 'id' in request.session:
        pdata=Fwcart.objects.filter(id=cid,status=0)  
        pdata.delete()
    return redirect('windex2')    

def wsinglepro(request,fid):
    data2=pfish.objects.filter(id=fid)
    return render(request,'fsinglepro.html',{'data2':data2})

def wrecipe(request):
    data3=rfish.objects.all()
    return render(request,'frecipe.html',{'data3':data3}) 

def wsinglerecipe(request,frid):
    data4=rfish.objects.filter(id=frid)
    return render(request,'fsinglerecipe.html',{'data4':data4})

def wlogin(request):
    return render(request,'login1.html') 

def wlog(request):
    username = request.POST.get('name')
    password = request.POST.get('password')
    if freg.objects.filter(uname=username,password=password).exists():
        data5=freg.objects.filter(uname=username,password=password).values('adrs','img','number','location','email','id').first()
        request.session['address']=data5['adrs']
        request.session['email']=data5['email']
        request.session['number']=data5['number']
        request.session['location']=data5['location']
        request.session['img']=data5['img']
        request.session['username']=username
        request.session['password']= password
        request.session['id']=data5['id']
        return redirect('windex2') 
    else:
        return render(request,'login1.html',{'msg':"Sorry... Invalid username or password"})  

def wlogout(request):
    del request.session['email']
    del request.session['username']
    del request.session['password']
    del request.session['address']
    del request.session['location']
    del request.session['number']
    del request.session['img']
    del request.session['id']
    return redirect('windex2') 

def wreg(request):
    return render(request,'fregister.html')  

def wdisplay(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        adrs = request.POST.get('adrs')
        email = request.POST.get('email')
        location = request.POST.get('location')
        number = request.POST.get('number')
        img = request.FILES['img']
        data5 = freg(uname=uname,password=password,repassword=repassword,adrs=adrs,location=location,email=email,number=number,img=img)
        data5.save()
    return redirect('wlogin')                   