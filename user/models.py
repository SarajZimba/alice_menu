# import datetime
# import random
# import uuid

# from django.conf import settings
# from django.contrib.auth.models import AbstractUser
# from django.core.mail import send_mail
# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from alice_menu.utils import BaseModel
# # from organization.models import Branch, Organization
# # from root.utils import BaseModel


# class User(BaseModel):
#     full_name = models.CharField(max_length=255, null=False, blank=False)
#     email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
#     image = models.ImageField(upload_to="user/images/", null=True, blank=True)
#     phone_number = models.CharField(max_length=255, null=True, blank=True)
#     address = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return f"{self.full_name} - ({self.email})"

#     def save(self, *args, **kwargs):
#         if not self.email:
#             self.email = f"{self.username}@silverlinepos.com"
#         super().save(*args, **kwargs)