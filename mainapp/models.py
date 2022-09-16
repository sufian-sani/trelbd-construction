from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField
from django.core.validators import RegexValidator
from django.utils.timezone import now

# Create your models here.
class Slidermodel(models.Model):
    title = models.CharField(max_length=200)
    url_field = models.URLField(blank=True,null=True)
    subtitle = models.CharField(max_length=500)
    background_image = models.ImageField(upload_to='slider_image')

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Slider Model"
        verbose_name_plural = "Slider Model"

class Ourserver(models.Model):
    heading = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='weoffer')
    brochure_file = models.FileField(upload_to='brochure/',blank=True,null=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.heading
    @property
    def file_url(self):
        if self.brochure_file and hasattr(self.brochure_file, 'url'):
            return self.brochure_file.url

    class Meta: 
        verbose_name = "Our Service"
        verbose_name_plural = "Our Service"
    
    

class Ourproject(models.Model):
    image = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=200)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Our Project"
        verbose_name_plural = "Our Project"

# class Project(models.Model):
#     image = models.ImageField(upload_to='project')
#     street_location = models.CharField(max_length=200)
#     location = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)

# class Ourteam(models.Model):
#     image = models.ImageField(upload_to='ourteam')
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=50)

# class Latesnews(models.Model):
#     image = models.ImageField(upload_to='latesnews')
#     title = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=100)

class Ourmission(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='ourmission', blank=True, null=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Our Mission"
        verbose_name_plural = "Our Mission"

class Companyvalue(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='ourmission', blank=True, null=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Company Value"
        verbose_name_plural = "Company Value"

class Contactservice(models.Model):
    service_id = models.IntegerField()
    service_name = models.CharField(max_length=200)
    customer_name = models.CharField(max_length = 200)
    company_name = models.CharField(max_length = 200, blank=True, null=True)
    phone = models.CharField(max_length = 15)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.customer_name

    class Meta: 
        verbose_name = "Contact Service"
        verbose_name_plural = "Contact Service"

class Ourvision(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='ourvision',blank=True,null=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Our Vision"
        verbose_name_plural = "Our Vision"

class Ourreport(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='ourreport',blank=True,null=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Our Report"
        verbose_name_plural = "Our Report"

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=200)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"

class Historymilestones(models.Model):
    image = models.ImageField(upload_to='historymilestones')
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "History And Milestones"
        verbose_name_plural = "History And Milestones"

class Boardmeetingsagm(models.Model):
    image = models.ImageField(upload_to='Boardmeetingsagm')
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Board Meetings and AGM"
        verbose_name_plural = "Board Meetings and AGM"

class Corporategovernance(models.Model):
    image = models.ImageField(upload_to='Corporategovernance')
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    textfiled=RichTextUploadingField(blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta: 
      verbose_name = "Corporate Governance"
      verbose_name_plural = "Corporate Governance"

# -------report and statement
class Reportstatement(models.Model):
    title = models.CharField(max_length=500)
    file = models.FileField(upload_to='reportFILE/')
    publish_date = models.DateField(auto_now=False)

    def __str__(self):
            return self.title

    class Meta: 
        verbose_name = "Report and Statement"
        verbose_name_plural = "Report and Statement"

class Events(models.Model):
  title = models.CharField(max_length=500)
  slug = AutoSlugField(populate_from='title', unique=True)
  image=models.ImageField(upload_to='Events')
  publish_date = models.DateTimeField(auto_now_add=True)
  description=RichTextUploadingField(blank=True,null=True)

  def __str__(self):
        return self.title

  class Meta: 
        verbose_name = "Events"
        verbose_name_plural = "Events"

class CarrerModel(models.Model):
  title=models.CharField(max_length=200)
  slug = AutoSlugField(populate_from='title', unique=True)
  salary=models.CharField(max_length=8, validators=[RegexValidator(r'^\d{1,10}$')], blank=True)
  post_date=models.DateTimeField(default=now)
  description=RichTextUploadingField(blank=True,null=True)

  def __str__(self):
    return self.title

  class Meta: 
    verbose_name = "Carrer Model"
    verbose_name_plural = "Carrer Model"

class Application(models.Model):
  job_id = models.CharField(max_length=3)
  job_title = models.CharField(max_length=300)
  name=models.CharField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
  phone = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
  email=models.EmailField()
  expected_salary = models.CharField(max_length=7, validators=[RegexValidator(r'^\d{1,10}$')], blank=True)
  resume=models.FileField(upload_to='resume/cv')
  message=models.TextField()

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Job Application"
    verbose_name_plural = "Job Applications"

class News(models.Model):
    title=models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    image=models.ImageField(upload_to='news')
    publish_date = models.DateTimeField(auto_now_add=True)
    description=RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "News"
        verbose_name_plural = "News"

class Emailsusbction(models.Model):
    email = models.EmailField()

    class Meta: 
        verbose_name = "Email Susbction"
        verbose_name_plural = "Email Susbction"
    

class Expertteams(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to='teams')
    description=RichTextUploadingField(blank=True,null=True)

    class Meta: 
        verbose_name = "Expert Team Member"
        verbose_name_plural = "Expert Team Member"

class MessagefromMD(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to='teams')
    description=RichTextUploadingField(blank=True,null=True)

    class Meta: 
        verbose_name = "Message from MD"
        verbose_name_plural = "Message from MD"

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    customer_name = models.CharField(max_length = 200)
    company_name = models.CharField(max_length = 200, blank=True, null=True)
    phone = models.CharField(max_length = 15)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta: 
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.customer_name

class CorporateSocialResponsibility(models.Model):
    description=RichTextUploadingField(blank=True,null=True)

    class Meta: 
        verbose_name = "Corporate Social Responsibility"
        verbose_name_plural = "Corporate Social Responsibility"

# ---------------------product--start
class Category(models.Model):
  name = models.CharField(max_length=200)
  description=models.TextField(blank=True,null=True)

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Category"
    verbose_name_plural = "Category"

class Brand(models.Model):
  name = models.CharField(max_length=200)
  description=models.TextField(blank=True,null=True)

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Brand"
    verbose_name_plural = "Brand"

class Products(models.Model):
  name = models.CharField(max_length=200)
  slug = AutoSlugField(populate_from='name', unique=True)
  image=models.ImageField(upload_to='Products')
  subtitle=models.CharField(max_length=200, default="",blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
  description=RichTextUploadingField(blank=True,null=True)
  seriel_no = models.IntegerField(blank=True, null=True)
  is_published = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Products"
    verbose_name_plural = "Products"

# ---------------------product--end

class Quotationinquiry(models.Model):
  product_name=models.CharField(max_length=200)
  product_quantity = models.IntegerField(default=1)
  customer_name=models.CharField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{11,14}$', message="Phone number must be entered in the format: '+8801711111000'.")
  customer_phone_number = models.CharField(validators=[phone_regex], max_length=14) # Validators should be a list
  customer_email = models.EmailField(blank=True,null=True)
  customer_address=models.CharField(max_length=200,blank=True,null=True)
  message = models.TextField(blank=True,null=True)

  def __str__(self):
    return self.product_name

  class Meta: 
    verbose_name = "Quotation Inquiry"
    verbose_name_plural = "Quotation Inquiry"


class BoardofDirector(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to='teams')
    description=RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Board Of Directors"
        verbose_name_plural = "Board Of Directors"

class NoticeSection(models.Model):
  title = models.CharField(max_length=500)
  file = models.FileField(upload_to='notice/')
  publish_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.title

  class Meta: 
    verbose_name = "Notice"
    verbose_name_plural = "Notice"

class Companyprofile(models.Model):
    file = models.FileField(upload_to='companyprofile/',blank=True,null=True)

    @property
    def file_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url

    class Meta: 
        verbose_name = "Company Profile"
        verbose_name_plural = "Company Profile"

class Aboutus(models.Model):
    description=RichTextUploadingField(blank=True,null=True)

    class Meta: 
        verbose_name = "About us"
        verbose_name_plural = "About us"



