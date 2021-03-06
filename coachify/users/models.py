import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class BaseUserData(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    firstname = models.CharField(_("first name"), max_length=30, blank=True, default="")
    lastname = models.CharField(_("last name"), max_length=150, blank=True, default="")

    phone = models.CharField(max_length=255, verbose_name=_("Phone"))
    email = models.EmailField(max_length=255, verbose_name=_("Email"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    gender = models.CharField(_("Gender"), max_length=255, default="male")

    avatar = models.ImageField(
        upload_to="avatars/", verbose_name=_("Avatar"), blank=True
    )

    class Meta:
        abstract = True


class Teacher(BaseUserData, models.Model):
    students = models.ManyToManyField("Student", related_name="teachers", blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Parent(BaseUserData, models.Model):
    def __str__(self):
        return f"{self.firstname} {self.lastname}"


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
    parent = models.ForeignKey(
        "Parent", related_name="students", blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class User(BaseUserData, AbstractUser):
    """
    Default custom user model for Coachify.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    teachers = models.ManyToManyField(Teacher, related_name="principal", blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
