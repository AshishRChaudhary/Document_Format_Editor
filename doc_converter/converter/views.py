from rest_framework import generics, permissions
from django.http import FileResponse
from django.utils.timezone import now
from .models import ConversionRecord
from .serializers import ConversionRecordSerializer
import os
from django.conf import settings
from .utils import convert_file

class ConversionListCreateView(generics.ListCreateAPIView):
    serializer_class = ConversionRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ConversionRecord.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        uploaded_file = self.request.FILES.get("file")  # Fetch file
        target_format = self.request.data.get("converted_format")  # Correct key

        if not uploaded_file or not target_format:
            raise ValueError("File and format must be provided.")

        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)

        # Save uploaded file temporarily
        with open(file_path, "wb") as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        # Convert the file
        converted_path = convert_file(file_path, target_format)

        # Save metadata with conversion date
        conversion_record = serializer.save(
            user=self.request.user,
            file_name=uploaded_file.name,
            converted_format=target_format,
            upload_date=now(),  # Explicitly set the conversion date
        )

        # Prepare file response for download
        response = FileResponse(open(converted_path, "rb"), as_attachment=True)

        # Clean up files after download
        os.remove(file_path)
        os.remove(converted_path)

        return response


class ConversionHistoryView(generics.ListAPIView):
    serializer_class = ConversionRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ConversionRecord.objects.filter(user=self.request.user)


class ConversionHistoryDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConversionRecord.objects.all()
    serializer_class = ConversionRecordSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can delete/update
