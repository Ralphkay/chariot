import datetime

from PIL import Image
from django.db import models

from groups.models import Group

# Create your models here.

# from welfare.models import WelfareContribution

GENERIC_BOOLEAN = (
    (0, 'No'),
    (1, 'Yes'),
)


class Member(models.Model):
    OCCUPATIONS = (
        ('teacher', 'Teacher'),
        ('lecturer', 'Lecturer'),
        ('nurse', 'Nurse'),
        ('doctor', 'Doctor'),
    )

    SECTORS = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    EDUCATION_LEVEL = (
        ('no-school', 'Not Applicable'),
        ('primary', 'Primary'),
        ('jhs', 'JHS'),
        ('shs', 'SHS'),
        ('vocational', 'Vocational'),
        ('certificate', 'Certificate'),
        ('diploma', 'Diploma'),
        ('diploma', 'Diploma'),
        ('hnd', 'HND'),
        ('degree', 'Degree'),
        ('masters', 'masters'),
        ('phd', 'PHD'),
    )

    GENDER_TYPE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    LIVING_STATUS = (
        ('deceased', 'Deceased'),
        ('alive', 'Alive'),
    )

    RELATIONSHIP = (
        ('brother', 'Brother'),
        ('sister', 'Sister'),
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('son', 'Son'),
        ('cousin', 'Cousin'),
        ('friend', 'Friend'),
    )

    MARITAL_STATUS_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
        ('co-habitating', 'Co-habitating'),
        ('engaged', 'Engaged'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('religious', 'religious'),
    )

    first_name = models.CharField(max_length=255, blank=False, null=False)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    gender = models.CharField(max_length=255, null=False, blank=False, default=None, choices=GENDER_TYPE)
    email = models.EmailField(max_length=255, blank=True, null=True, db_index=True, unique=True)
    date_of_birth = models.DateField(blank=False, null=False)
    primary_phone = models.CharField(max_length=255, blank=False, null=False)
    secondary_phone = models.CharField(max_length=255, blank=True, null=True)
    residential_address = models.CharField(max_length=255, blank=True, null=True)
    city_or_town = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=False, null=False)
    occupation = models.CharField(max_length=255, blank=False, null=False, choices=OCCUPATIONS)
    sector = models.CharField(max_length=255, blank=False, null=False, choices=SECTORS)
    education_level = models.CharField(max_length=255, blank=False, null=False, choices=EDUCATION_LEVEL)
    marital_status = models.CharField(max_length=20, blank=False, null=False,
                                      choices=MARITAL_STATUS_CHOICES, default=MARITAL_STATUS_CHOICES[0])

    # family data 
    father_name = models.CharField(max_length=255, blank=False, null=False)
    father_hometown = models.CharField(max_length=255, blank=False, null=False)
    father_living_status = models.CharField(max_length=255, null=False, blank=False, default=None,
                                            choices=LIVING_STATUS)
    mother_name = models.CharField(max_length=255, blank=False, null=False)
    mother_hometown = models.CharField(max_length=255, blank=False, null=False)
    mother_living_status = models.CharField(max_length=255, null=False, blank=False, default=None,
                                            choices=LIVING_STATUS)
    # next of kin
    next_of_kin_name = models.CharField(max_length=255, blank=False, null=False)
    next_of_kin_relationship = models.CharField(max_length=255, blank=False, null=False, choices=RELATIONSHIP)
    next_of_kin_primary_phone = models.CharField(max_length=255, blank=False, null=False)
    next_of_kin_email = models.EmailField(max_length=255, blank=True, null=True)
    next_of_kin_location = models.CharField(max_length=255, blank=True, null=False, )

    # emergency contact
    emergency_name = models.CharField(max_length=255, blank=False, null=False)
    emergency_primary_phone = models.CharField(max_length=255, blank=False, null=False)

    # organisation
    organisations = models.ManyToManyField(Group, blank=True)
    profile_photo = models.ImageField(default='default_profile_photo.jpg', blank=True, null=True,
                                      upload_to='profile_photos')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def get_profile_photo_url(self):
        if self.profile_photo and hasattr(self.profile_photo, 'url'):
            return self.profile_photo.url
        else:
            return "/media/default_profile_photo.jpg"

    def save(self):
        try:
            super().save()
            profile_photo = Image.open(self.profile_photo.path)  # Open image
            # resize image
            if profile_photo.height > 150 or profile_photo.width > 150:
                output_size = (150, 150)
                profile_photo.thumbnail(output_size)  # Resize image
                profile_photo.save(self.profile_photo.path)  # Save it again and override the larger image
        except:
            pass

    @property
    def fullname(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"

    def __str__(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"


class MemberReligiousCV(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)

    #    baptism_cv
    baptism_status = models.BooleanField(default=True, blank=True, null=False, choices=GENERIC_BOOLEAN)
    baptism_date = models.DateField(null=True, blank=True)
    baptism_location = models.CharField(max_length=255, blank=True, null=True)
    baptised_by = models.CharField(max_length=255, blank=True, null=True)

    #    holy_communion_cv
    holy_communion_status = models.BooleanField(default=True, blank=True, null=False, choices=GENERIC_BOOLEAN)
    holy_communion_date = models.DateField(null=True, blank=True)
    holy_communion_location = models.CharField(max_length=255, blank=True, null=True)
    holy_communion_given_by = models.CharField(max_length=255, blank=True, null=True)

    #    confirmation_cv
    confirmation_status = models.BooleanField(default=True, blank=True, null=False, choices=GENERIC_BOOLEAN)
    confirmation_date = models.DateField(null=True, blank=True)
    confirmation_location = models.CharField(max_length=255, blank=True, null=True)
    confirmed_by = models.CharField(max_length=255, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Member Christian Information'
        verbose_name_plural = 'Members Christian Information'