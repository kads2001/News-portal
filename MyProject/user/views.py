from django.shortcuts import render
from .models import *
from django.db.models import Q


# Create your views here.
def index(request):
    data=slider.objects.all().order_by('-id')[0:2]
    d=ncategory.objects.all().order_by('-id')[0:6]
    cd=mynews.objects.all().order_by('-id')
    x=mynews.objects.all().order_by('-id')[0:8]
    vdo=videonews.objects.all().order_by('-id')
    ct=city.objects.all().order_by('-id')[0:6]
    mydict={"res":data,"data":d,"dm":cd,"city":ct,"vdata":vdo}
    return render(request,'user/index.html',mydict)
##################################################
def about(request):
    return render(request,'user/about.html')
##################################################

def contact(request):
    status=False
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mob')
        message=request.POST.get('msg')
        contactus(Name=name,Email=email,Mobile=mobile,Message=message).save()
        status=True

    return render(request,'user/contact.html',context={"msg":status})

#######################################
def gallery(request):
    d=igallery.objects.all().order_by('-id')
    mydict={"data":d}
    return render(request,'user/gallery.html',context=mydict)

#################################################
def video(request):

   vdata=videonews.objects.all().order_by('-id')
   if request.method=="GET":
       s=request.GET.get('search')
       if s is not None:
        vdata=videonews.objects.all().filter(Q(vhead__icontains=s) |Q (vcategory__icontains=s)|Q (vcity__icontains=s)|Q (vdec__icontains=s))


   md={"data":vdata}
   return render(request,'user/video.html',md)
#####################################
def news(request):
    x=ncategory.objects.all().order_by('-id')
    y=city.objects.all().order_by('-id')
    z=mynews.objects.all().order_by('-id')
    mydict={"cat":x,"ct":y,"ndata":z}


    return render(request,'user/news.html',mydict)
#############################################
def ndetails(request):
    nid=request.GET.get('n')
    x=mynews.objects.all().filter(id=nid)
    myd={"ndata":x}
    return render(request, 'user/ndetails.html',myd)
###############################################
def login(request):
    return render(request,'user/login.html')
#################################################
def viewnews(request):
    a=request.GET.get('msg')
    c=request.GET.get('cid')
    if a is not  None:

       x=mynews.objects.all().filter(category=a).order_by('-id')
    elif c is not None:
        x = mynews.objects.all().filter(ncity=c)

    mydict={"ndata":x}


    return render(request,'user/viewnews.html',mydict)
###################################################
def vdetail(request):

    a=request.GET.get('vid')
    x=videonews.objects.all().filter(id=a)
    mydict={"vdata":x}
    return render(request,'user/vdetail.html',mydict)
######################################################
def developer(request):
    return render(request,'user/developer.html')


