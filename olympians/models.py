from django.db import models

class Company(models.Model): 
    company_name        =   models.CharField(max_length=200, blank=True, null=True)  
    company_email       =   models.CharField(max_length=200, blank=True, null=True)   
    company_address     =   models.TextField(blank=True, null=True)
    company_description =   models.TextField(blank=True, null=True)
    company_logo       =   models.ImageField(blank=True,null=True)
    created_at          =   models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at          =   models.DateTimeField(auto_now=True)

    class Meta:
            ordering = ["-created_at", "-updated_at"]        
            
    def __str__(self):
        return str(str(self.company_name))