from rest_framework import serializers
from .models import ConversionRecord

class ConversionRecordSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)  # Add this field for file upload
    converted_format = serializers.ChoiceField(choices=ConversionRecord.FORMAT_CHOICES)  # Restrict format choices

    class Meta:
        model = ConversionRecord
        fields = ["id", "file","file_name", "converted_format", "upload_date"]
        #read_only_fields = ["file_name", "upload_date"]

    '''def create(self, validated_data):
        """Override create to ensure file_name is handled separately"""
        validated_data["file_name"] = self.context["file_name"]  # Injected from the view
        return super().create(validated_data)'''