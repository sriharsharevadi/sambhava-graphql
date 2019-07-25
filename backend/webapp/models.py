from django.db import models


class Student(models.Model):
    rollNumber = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    individual = models.BooleanField(default=True)
    organizationId = models.IntegerField()
    batchId = models.IntegerField()
    mobileNumber = models.CharField(max_length=15)
    verified = models.BooleanField(default=False)
    verifiedTime = models.DateTimeField()
    expiryDate = models.DateTimeField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.mobileNumber


class Institute(models.Model):
    name = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    verifiedTime = models.DateTimeField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    studentCap = models.IntegerField()
    mobileNumber = models.CharField(max_length=15)
    alternateNumber = models.CharField(max_length=15)
    expiryDate = models.DateTimeField()

    def __str__(self):
        return self.mobileNumber



class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    instituteId = models.ForeignKey(
        Institute, related_name='instituteId', on_delete=models.CASCADE, default=1)
    # studentId = models.ForeignKey(
    #     Student, related_name='studentId', on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
