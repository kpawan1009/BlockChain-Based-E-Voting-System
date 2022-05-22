from django.db import models
from twilio.rest import Client


# from twilio.rest import Client
class Candidateudma(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    party=models.CharField(max_length=30)
    constituency=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Candidateaura(models.Model):
    objects = None
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    party=models.CharField(max_length=30)
    constituency=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Candidatepalg(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    party=models.CharField(max_length=30)
    constituency=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Votergovt(models.Model):
    name=models.CharField(max_length=40)
    pannumber=models.CharField(max_length=10)
    constituency=models.CharField(max_length=40)
    age=models.IntegerField(default=18)

    def __str__(self):
        return self.name

class Voterregisteredudma(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    address=models.TextField()
    phonenumber=models.CharField(max_length=10)
    pannumber=models.CharField(max_length=10)
    email=models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Voterregisteredpalghar(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    address=models.TextField()
    phonenumber=models.CharField(max_length=10)
    pannumber=models.CharField(max_length=10)
    email=models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Voterregisteredamroha(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    address=models.TextField()
    phonenumber=models.CharField(max_length=10)
    pannumber=models.CharField(max_length=10)
    email=models.CharField(max_length=40)

    def __str__(self):
        return self.name


class UIDudma(models.Model):
    pannumber=models.CharField(max_length=10)
    uniqueid=models.CharField(max_length=10)
    # phonenumber=models.IntegerField(max_length=15)
    def __str__(self):
        return self.uniqueid



class UIDamroha(models.Model):
    pannumber=models.CharField(max_length=10)
    uniqueid=models.CharField(max_length=10)
    # phonenumber=models.IntegerField(max_length=15)

    def __str__(self):
        return self.uniqueid

    # def save(self):
    #     account_sid = 'ACfa814df1d6fa8277160942dbbee3d51a'
    #     auth_token = '9abe2acc167a8869fe64ab644a7d1062'
    #     client = Client(account_sid, auth_token)
    #
    #     message = client.messages.create(
    #         body=super.uniqueid,
    #         # from='+19896536301',
    #         to='+919801777249'
    #     )
    #
    #     print(message.sid)


class UIDpalghar(models.Model):
    pannumber=models.CharField(max_length=10)
    uniqueid=models.CharField(max_length=10)
    # phonenumber = models.IntegerField(max_length=15)
    def __str__(self):
        return self.uniqueid

    # def save(self):
    #     account_sid = 'ACfa814df1d6fa8277160942dbbee3d51a'
    #     auth_token = '9abe2acc167a8869fe64ab644a7d1062'
    #     client = Client(account_sid, auth_token)
    #
    #     message = client.messages.create(
    #         body=super.uniqueid,
    #         # from='+19896536301',
    #         to='+919801777249'
    #     )
    #
    #     print(message.sid)


class Feedback(models.Model):
    name2 = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    feedback=models.TextField()

    def __str__(self):
        return self.name2