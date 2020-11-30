from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters long"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters long"
        if len(post_data['email']) < 8:
            errors['length_email'] = "Email must be at least 8 characters long"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['invalid_email'] = "Invalid Email. Please try again"
        if len(post_data['password']) < 8:
            errors['length_password'] = "Password must be at least 8 characters long"
        if post_data['password'] != post_data['confirm_password']:
            errors['invalid_password'] = "Password and confirm doesn't match"
        return errors
    def login_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['email']) < 8:
            errors['email_length'] = "Email must be at least 8 characters long"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['invalid_email'] = "Invalid email. Please try again"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager ()
    def __repr__(self):
        return f'{self.first_name}-{self.last_name}-{self.email}-'

class JobManager(models.Manager):
    def job_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = "Title cannot be less than 2 characters"
        if len(post_data['description']) < 2:
            errors['description'] = "Description cannot be less than 2 characters"
        if len(post_data['location']) < 2:
            errors['location'] = "Location cannot be less than 2 characters"
        return errors

class Job(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    submitted_by = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    objects = JobManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f'{self.title}-{self.description}-{self.location}-'


# Create your models here.
