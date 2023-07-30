from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    phone = models.CharField(max_length=255,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="media/upload")
    is_manager = models.BooleanField(default=False)
    def __str__(self):
        return self.phone


class Order(models.Model):
    name = models.CharField(null=True, max_length=255,blank=True)
    email = models.EmailField(null=True, blank=True)
    device = models.CharField(null=True, max_length=255, blank=True)
    model = models.CharField(null=True, max_length=255, blank=True)
    problems = models.CharField(null=True, max_length=255, blank=True)
    others = models.TextField(null=True, max_length=2555, blank=True)
    my_place = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    phone = models.CharField(max_length=255, blank=True,null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(Profile,blank=True,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Webpack(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    icon = models.ImageField(null=True)
    email = models.EmailField(null=True,blank=True)
    tiktok = models.CharField(max_length=2555,null=True,blank=True)
    instagram = models.CharField(max_length=2555,null=True,blank=True)
    facebook = models.CharField(max_length=2555,null=True,blank=True)
    telegram = models.CharField(max_length=2555,null=True,blank=True)
    whatsup = models.CharField(max_length=2555,null=True,blank=True)
    youtube = models.CharField(max_length=2555,null=True,blank=True)
    twitter = models.CharField(max_length=2555,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.name



class About(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    p1 = models.TextField(null=True,max_length=2555)
    p2 = models.TextField(null=True,max_length=2555,blank=True)
    p3 = models.TextField(null=True,max_length=2555,blank=True)
    p4 = models.TextField(null=True,max_length=2555,blank=True)
    def __str__(self):
        return self.title


class Faq(models.Model):
    question=models.CharField(null=True,blank=True,max_length=255)
    answer=models.TextField(null=True,blank=True,max_length=2555)
    def __str__(self):
        return self.question


class Apply(models.Model):
    name = models.CharField(null=True,blank=True,max_length=255)
    email = models.EmailField(null=True,blank=True)
    file = models.FileField(null=True,upload_to='uploads',blank=True)
    phone = models.CharField(null=True,blank=True,max_length=255)
    more = models.TextField(null=True,max_length=2555,blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(null=True,blank=True,max_length=255)
    disc = models.TextField(null=True,blank=True,max_length=300)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.name

levels = (
    ("one","one"),
    ("two","two"),
    ("three","three"),
    ("four","four"),
    ("five","five"),
)


class Post(models.Model):
    level = models.CharField(null=True,blank=True,max_length=255,choices=levels)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    profile = models.ImageField(blank=True,upload_to="upload/blog")
    one_topic = models.CharField(null=True,blank=True,max_length=255)
    one_p1 = models.CharField(null=True,blank=True,max_length=2555)
    one_p2 = models.TextField(null=True,blank=True,max_length=2555)
    one_p3 = models.TextField(null=True,blank=True,max_length=2555)
    profile_two = models.ImageField(blank=True,upload_to="upload/blog")
    two_topic = models.CharField(null=True,blank=True,max_length=255)
    two_p1 = models.TextField(null=True,blank=True,max_length=2555)
    two_p2 = models.TextField(null=True,blank=True,max_length=2555)
    two_p3 = models.TextField(null=True,blank=True,max_length=2555)
    profile_three = models.ImageField(blank=True,upload_to="upload/blog")
    three_topic = models.CharField(null=True,blank=True,max_length=255)
    three_p1 = models.TextField(null=True,blank=True,max_length=2555)
    three_p2 = models.TextField(null=True,blank=True,max_length=2555)
    three_p3 = models.TextField(null=True,blank=True,max_length=2555)
    profile_four = models.ImageField(blank=True,upload_to="upload/blog")
    four_topic = models.CharField(null=True,blank=True,max_length=255)
    four_p1 = models.TextField(null=True,blank=True,max_length=2555)
    four_p2 = models.TextField(null=True,blank=True,max_length=2555)
    four_p3 = models.TextField(null=True,blank=True,max_length=2555)
    publisher = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    link = models.CharField(null=True,blank=True,max_length=5000)
    link_url = models.CharField(null=True,blank=True,max_length=500)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.one_topic


class Brand(models.Model):
    name = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=255,null=True)
    brand = models.ForeignKey(Brand,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Problem(models.Model):
    name = models.CharField(max_length=255,null=True)
    model = models.ForeignKey(Model,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Price(models.Model):
    amount = models.CharField(max_length=255,null=True)
    brand = models.ForeignKey(Brand,null=True,on_delete=models.CASCADE)
    model = models.ForeignKey(Model,null=True,on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.amount


class New(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    disc = models.TextField(max_length=2555,null=True,blank=True)
    image = models.ImageField(upload_to="new/",blank=True)
    def __str__(self):
        return self.name
        
        
class Password(models.Model):
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.first_name