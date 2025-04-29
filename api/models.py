# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    event_category = models.CharField(max_length=20, blank=True, null=True)
    max_attendees = models.IntegerField()

    class Meta:
        db_table = 'event'


class Host(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)  # The composite primary key (event_id, venue_id) found, that is not supported. The first column is selected.
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)

    class Meta:
        db_table = 'host'
        unique_together = (('event', 'venue'),)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'payment'


class Registration(models.Model):
    user = models.OneToOneField('Users', on_delete=models.CASCADE, primary_key=True)  # The composite primary key (user_id, ticket_id, event_id) found, that is not supported. The first column is selected.
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField()
    registration_status = models.CharField(max_length=20)

    class Meta:
        db_table = 'registration'
        unique_together = (('user', 'ticket', 'event'),)


class Sponsor(models.Model):
    sponsor_id = models.AutoField(primary_key=True)
    sponsor_name = models.CharField(max_length=50)
    sponsorship_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'sponsor'


class Support(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)  # The composite primary key (event_id, sponsor_id) found, that is not supported. The first column is selected.
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    support_date = models.DateTimeField()

    class Meta:
        db_table = 'support'
        unique_together = (('event', 'sponsor'),)


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_type = models.CharField(max_length=20)
    is_ticket_free = models.BooleanField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'ticket'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=10)

    class Meta:
        db_table = 'users'


class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=9)
    state = models.CharField(max_length=25)

    class Meta:
        db_table = 'venue'
