from django.db import models

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
        return self.name

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    rollNumber = models.CharField(max_length=100, null=True)
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    individual = models.BooleanField(default=True)
    batchId = models.IntegerField()
    mobileNumber = models.CharField(max_length=15)
    verified = models.BooleanField(default=False)
    verifiedTime = models.DateTimeField(null=True)
    expiryDate = models.DateTimeField(null=True)
    city = models.CharField(max_length=100, null=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)
    institute = models.ForeignKey(
        Institute, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.email




