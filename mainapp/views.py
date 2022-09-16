from django.http import HttpRequest
from django.shortcuts import render
from .models import *
from .forms import *

from django.http import HttpResponseRedirect
from django.urls import reverse

# from django.core.paginator import Paginator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.


def index(request):
    slider_objects = Slidermodel.objects.all()

    services = Ourserver.objects.all()

    ourproject = Ourproject.objects.all()

    ourrecentproject = Ourproject.objects.all()[4:]
    companyvalue = Companyvalue.objects.all().first()

    # projects = Project.objects.all()

    ourteams = Expertteams.objects.all()

    ourmission = Ourmission.objects.all().first()
    ourvision = Ourvision.objects.all().first()

    latesnewss = News.objects.all()[:3]

    ourreports = Ourreport.objects.all().first()

    companyprofile = Companyprofile.objects.all().last()
    ourgallery = Gallery.objects.all()[:6]

    if request.method == 'POST':
        email = request.POST.get('email')
        user = Emailsusbction(email=email)
        user.save()

    context = {
        'slider_objects': slider_objects,
        'services': services,
        'ourproject': ourproject,
        'ourrecentproject': ourrecentproject,
        'ourteams': ourteams,
        'latesnewss': latesnewss,
        'companyvalue':companyvalue,
        'ourmission':ourmission,
        'ourvision':ourvision,
        'ourreports':ourreports,
        'companyprofile':companyprofile,
        'ourgallery':ourgallery,
    }

    return render(request, 'index.html', context)


def ourmission(request):
    ourmission_all = Ourmission.objects.all().first()
    context = {
        'ourmission_all': ourmission_all,
    }
    return render(request, 'subpage/ourmission.html', context)


def service(request):
    services = Ourserver.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'subpage/service.html', context)


def servicedetails(request, id):
    service_details = Ourserver.objects.get(pk=id)
    related_service = Ourserver.objects.all().exclude(pk=id)
    print(related_service)

    if request.method == 'POST':
        service_id = request.POST.get('serviceId')
        # service_id = int(service_id)
        service_name = request.POST.get('servicename')
        customer_name = request.POST.get('customername')
        company_name = request.POST.get('companyname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        user = Contactservice(service_id=service_id, service_name=service_name, customer_name=customer_name,
                              company_name=company_name, phone=phone, email=email, message=message)
        user.save()

    context = {
        'service_details': service_details,
        'related_service': related_service,
    }
    return render(request, 'subpage/servicedetails.html', context)


def ourproject(request):
    ourprojects = Ourproject.objects.all()
    context = {
        'ourprojects': ourprojects,
    }
    return render(request, 'subpage/ourprojects.html', context)


def ourprojectdetails(request, id):
    ourproject_details = Ourproject.objects.get(pk=id)
    context = {
        'ourproject_details': ourproject_details,
    }
    return render(request, 'subpage/ourprojectsdetails.html', context)


def ourvision(request):
    ourvision = Ourvision.objects.all().first()
    context = {
        'ourvision': ourvision,
    }
    return render(request, 'subpage/ourvision.html', context)


def ourreport(request):
    ourreports = Ourreport.objects.all().first()
    context = {
        'ourreports': ourreports,
    }
    return render(request, 'subpage/ourreport.html', context)


def gallery(request):
    gallery_all = Gallery.objects.all()
    context = {
        'gallery_all': gallery_all,
    }
    return render(request, 'subpage/gallery.html', context)


def gallerydetails(request, id):
    gallery_details = Gallery.objects.get(pk=id)
    context = {
        'gallery_details': gallery_details,
    }
    return render(request, 'subpage/gallery_details.html', context)


def boardofdirectors(request):
    boardofdirectors = BoardofDirector.objects.all()
    context = {
        'boardofdirectors': boardofdirectors,
    }
    return render(request, 'subpage/BoardOfDirectors.html', context)

def boardofdirectorsdetails(request, slug):
    boardofdirectorsdetails = BoardofDirector.objects.get(slug=slug)
    context = {
        'boardofdirectorsdetails': boardofdirectorsdetails,
    }
    return render(request, 'subpage/BoardOfDirectorsDetails.html', context)


def historymilestones(request):
    historymilestones = Historymilestones.objects.all()
    context = {
        'historymilestones': historymilestones,
    }
    return render(request, 'subpage/history_milestones.html', context)


def historymilestonesdetails(request, slug):
    historymilestonesdetails = Historymilestones.objects.get(slug=slug)
    context = {
        'historymilestonesdetails': historymilestonesdetails,
    }
    return render(request, 'subpage/historymilestonedetails.html', context)


def boardmeetingsagm(request):
    boardmeetingsagm = Boardmeetingsagm.objects.all()
    context = {
        'boardmeetingsagm': boardmeetingsagm,
    }
    return render(request, 'subpage/boardmeetingsagm.html', context)


def boardmeetingsagmdetails(request, slug):
    boardmeetingsagmdetails = Boardmeetingsagm.objects.get(slug=slug)
    context = {
        'boardmeetingsagmdetails': boardmeetingsagmdetails,
    }
    return render(request, 'subpage/boardmeetingsagmdetails.html', context)


def corporategovernance(request):
    corporategovernance = Corporategovernance.objects.all()
    context = {
        'corporategovernance': corporategovernance,
    }
    return render(request, 'subpage/corporategovernance.html', context)

def corporategovernancedetails(request, slug):
    corporategovernance_details = Corporategovernance.objects.get(slug=slug)
    context = {
        'corporategovernance_details': corporategovernance_details,
    }
    return render(request, 'subpage/corporategovernancedetails.html',context)


def reportstatements(request):
    reportstatement = Reportstatement.objects.all()
    context = {
        'reportstatement': reportstatement,
    }
    return render(request, 'subpage/report_statements.html', context)


def event(request):
    events = Events.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'subpage/event.html', context)

def eventdetails(request, slug):
    events_details = Events.objects.get(slug=slug)
    context = {
        'events_details': events_details,
    }
    return render(request, 'subpage/event_details.html', context)


def carrer(request):
    carrer = CarrerModel.objects.all()
    context = {
        'carrer': carrer,
    }
    return render(request, 'subpage/carrer.html', context)


def carrerdetails(request, slug):
    carrer = CarrerModel.objects.get(slug=slug)

    if request.method == 'POST':
        job_id = request.POST['job_id']
        job_title = request.POST['job_title']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        expected_salary = request.POST['expected_salary']
        resume = request.FILES['resume']
        message = request.POST.get('message', True)

        user = Application(job_id=job_id, job_title=job_title, name=name, phone=phone,
                           email=email, expected_salary=expected_salary, message=message, resume=resume)
        user.save()

        return HttpResponseRedirect(reverse('carrer'))

    context = {
        'carrer': carrer,
    }
    return render(request, 'subpage/carrerdetails.html', context)

# def news(request):
#     newses = News.objects.all()
#     paginator = Paginator(newses, 2) # Show 25 contacts per page.

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'page_obj':page_obj,
#     }
#     return render(request, 'subpage/newspage.html',context)


def news(request):
    object_list = News.objects.all()
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 6)  # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'subpage/newspage.html', {'page_obj': page_obj})


def newsdetails(request, slug):
    news_details = News.objects.get(slug=slug)
    context = {
        'news_details': news_details,
    }
    return render(request, 'subpage/newspage_details.html', context)


def expertteam(request):
    expertteams = Expertteams.objects.all()
    context = {
        'expertteams': expertteams,
    }
    return render(request, 'subpage/expertteam.html', context)


def expertteamdetails(request, slug):
    expertteamdetails = Expertteams.objects.get(slug=slug)
    context = {
        'expertteamdetails': expertteamdetails,
    }
    return render(request, 'subpage/expertmember_details.html', context)


def messagefrommd(request):
    messagefrommd = MessagefromMD.objects.all()
    context = {
        'messagefrommd': messagefrommd,
    }
    return render(request, 'subpage/MessageFromMD.html', context)


def contactus(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customername')
        company_name = request.POST.get('companyname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        user = ContactUs(customer_name=customer_name, company_name=company_name,
                         phone=phone, email=email, message=message)
        user.save()

    return render(request, 'subpage/contactus.html')


def corporatesocialresponsibility(request):
    # corporatesocialresponsibility = CorporateSocialResponsibility.objects.all()
    corporatesocialresponsibility_safe = CorporateSocialResponsibility.objects.get(
        pk=1)
    print(corporatesocialresponsibility_safe)
    context = {
        'corporatesocialresponsibility_safe': corporatesocialresponsibility_safe,
    }
    return render(request, 'subpage/CorporateSocialResponsibility.html', context)


def advertisements(request):
    all_products = Products.objects.all()
    context = {
        'all_products': all_products
    }
    return render(request, 'subpage/advertisements.html', context)


def product_details(request, slug):
    product_details = Products.objects.get(slug=slug)

    initial_data = {
        'product_name': product_details.name,
        'product_quantity': 1,
    }

    # print(product_details.name)

    form = QuotationinquirytForm(initial=initial_data)

    if request.method == "POST":
        form = QuotationinquirytForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    context = {
        'product_details': product_details,
        'form': form,
    }

    return render(request, 'subpage/product_details.html', context)

# ----------product--------------end

def notice(request):
  all_notice = NoticeSection.objects.all().order_by('-publish_date')

  context={
    'all_notice':all_notice,
  }

  return render(request,'subpage/notice.html', context)

def companyvalue(request):
    companyvalue = Companyvalue.objects.all().first()
    context={
        'companyvalue':companyvalue,
    }
    return render(request,'subpage/companyvalue.html',context)

def aboutus(request):
    aboutus = Aboutus.objects.all().last()
    context={
        'aboutus':aboutus,
    }
    return render(request,'subpage/aboutus.html',context)

