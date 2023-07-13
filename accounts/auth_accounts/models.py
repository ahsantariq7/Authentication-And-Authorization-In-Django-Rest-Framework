from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator
from django_countries.fields import CountryField

phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")

class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, first_name,last_name,gender,age,marital_status,children,professional_category,annual_income,annual_net_income_after_any_charges,deposit_amount,country,address,agreement_1,agreement_2,password=None,password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            age=age,
            marital_status=marital_status,
            children=children,
            professional_category=professional_category,
            annual_income=annual_income,
            annual_net_income_after_any_charges=annual_net_income_after_any_charges,
            deposit_amount=deposit_amount,
            country=country,
            address=address,
            agreement_1=agreement_1,
            agreement_2=agreement_2,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, first_name,last_name,gender,age,marital_status,children,professional_category,annual_income,annual_net_income_after_any_charges,deposit_amount,country,address,agreement_1,agreement_2, password=None):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            email,
            password=password,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            age=age,
            marital_status=marital_status,
            children=children,
            professional_category=professional_category,
            annual_income=annual_income,
            annual_net_income_after_any_charges=annual_net_income_after_any_charges,
            deposit_amount=deposit_amount,
            country=country,
            address=address,
            agreement_1=agreement_1,
            agreement_2=agreement_2,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Phone",
        validators=[phone_validator],
        unique=True,
    )
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    genre=[
        ('male','male'),
        ('female','female'),
        ('unknown','unknown')
    ]
    gender=models.CharField(max_length=40,choices=genre,default='unknown')
    age=models.IntegerField()
    marital_status=models.BooleanField()
    children=models.IntegerField(blank=True,null=True,default=5)
    professional_category=models.CharField(max_length=200,null=True,blank=True,default='unknown')
    annual_income=models.FloatField(null=True,blank=True,default=10000)
    annual_net_income_after_any_charges=models.FloatField(null=True,blank=True)
    deposit_amount=models.FloatField(null=True,blank=True,default=1000)
    country=CountryField()
    address=models.CharField(max_length=300)
    agreement_1=models.BooleanField()
    agreement_2=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name",'phone','last_name','gender','age','marital_status','children','professional_category','annual_income','annual_net_income_after_any_charges','deposit_amount','country','address','agreement_1','agreement_2']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


