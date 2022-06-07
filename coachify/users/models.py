from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class BaseUserData(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    phone = models.CharField(max_length=255, verbose_name=_("Phone"))
    email = models.EmailField(max_length=255, verbose_name=_("Email"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    avatar = models.ImageField(upload_to="avatars/", verbose_name=_("Avatar"))

    class Meta:
        abstract = True


class Teacher(BaseUserData, models.Model):
    students = models.ManyToManyField("Student", related_name="teachers", blank=True)

    def __str__(self):
        return self.name


class Parent(BaseUserData, models.Model):
    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="classes"
    )
    students = models.ManyToManyField("Student", related_name="classes", blank=True)

    def __str__(self):
        return self.name


class Student(BaseUserData, models.Model):
    parent = models.ForeignKey("Parent", related_name="students", blank=True)

    def __str__(self):
        return self.name


class User(BaseUserData, AbstractUser):
    """
    Default custom user model for Coachify.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    Students = models.ManyToManyField("users.Student", blank=True)

    #: First and last name do not cover name patterns around the globe
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
