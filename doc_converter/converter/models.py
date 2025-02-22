from django.db import models
from django.contrib.auth.models import User

class ConversionRecord(models.Model):
    FORMAT_CHOICES = [
        ("pdf", "PDF"),
        ("docx", "DOCX"),
        ("txt", "TXT"),
        ("png", "PNG"),
        ("xlsx", "XLSX"),
        ("csv", "CSV"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    converted_format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    upload_date = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return f"{self.file_name} ({self.input_format} → {self.output_format})"
