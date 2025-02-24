# Document Format Converter API

## Project Overview

The **Document Format Converter API** is a backend service built with Django and Django REST Framework (DRF) that allows authenticated users to upload files, convert them into different formats, and download the converted files. It supports multiple file types and ensures that only conversion metadata is stored in the database.

## Supported File Conversions

- **PDF → DOCX**
- **DOCX → PDF**
- **TXT → PDF**
- **PNG → PDF**
- **XLSX → PDF**
- **XLSX → DOCX**
- **CSV → PDF**
- **CSV → DOCX**

## Features

- **User Authentication:** Only registered users can perform file conversions and view their history.
- **Synchronous Processing:** The API processes file conversion in real time, ensuring users receive the converted file immediately.
- **Metadata Storage:** Only stores details like file name, format, and upload date; actual files are not stored.
- **Admin Controls:** Admins can view all conversion records, update, and delete them if necessary.

## Installation & Setup

### Prerequisites

- Python (>= 3.8)
- Django (>= 4.0)
- Django REST Framework
- Required Python Libraries:
  ```sh
  pip install django djangorestframework pdf2docx python-docx reportlab openpyxl pillow
  ```

### Run the Server

1. Clone the repository and navigate to the project directory:
   ```sh
   git clone <repo_url>
   cd doc_converter
   ```
2. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
3. Start the Django development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### 1. Convert a File

**Endpoint:**

```
POST /converter/convert/
```

**Request:** (multipart/form-data)

```json
{
  "file": <upload_file>,
  "converted_format": "pdf"
}
```

**Response:**

- If successful, the converted file is downloaded immediately.
- If failed, an error message is returned.

🔗 [Django File Upload Handling](https://docs.djangoproject.com/en/stable/topics/http/file-uploads/)

### 2. View Conversion History

**Endpoint:**

```
GET /converter/history/
```

**Response:**

```json
[
  {
    "id": 1,
    "file_name": "example.docx",
    "converted_format": "pdf",
    "upload_date": "2025-02-22T12:00:00Z"
  }
]
```

🔗 [Django QuerySet Filtering](https://docs.djangoproject.com/en/stable/topics/db/queries/)

### 3. Admin - View All Conversions

**Endpoint:**

```
GET /converter/admin-history/
```

🔗 [DRF Permissions](https://www.django-rest-framework.org/api-guide/permissions/)

### 4. Admin - Delete/Update Records

**Endpoint:**

```
DELETE /converter/history/<id>/
PATCH /converter/history/<id>/
```

## Challenges & Solutions

### Challenge: **File Access Issues on Windows**

- **Problem:** Windows locks files, causing `PermissionError` when attempting to delete them.
- **Solution:** Used `del` statement to release file handles before attempting deletion.

🔗 [Python File Handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

### Challenge: **Downloading Files via API**

- **Problem:** Browsers do not directly handle file downloads from API responses.
- **Solution:** Use **Postman** or **cURL** to properly receive the file.

🔗 [Django FileResponse](https://docs.djangoproject.com/en/stable/ref/request-response/#fileresponse-objects)

## Important Notes ⚠️

- The **browser cannot download converted files** directly from API responses.
- Use **Postman** to send a request and receive the converted file.
- **Swagger UI** or other API testing tools do not support direct file downloads.

## Example Walkthrough

**Convert a DOCX file to PDF using Postman:**

1. Open Postman.
2. Select **POST** and enter `http://127.0.0.1:8000/converter/convert/`.
3. In **Body**, choose `form-data` and add:
   - `file` (upload a `.docx` file)
   - `converted_format`: `pdf`
4. Click **Send**.
5. The converted file will be available for download in Postman.

## Future Enhancements 🚀

- Add **Celery & Redis** for background processing (optional if needed later).
- Support **more file formats** for conversion.
- Implement a **frontend UI** to interact with the API.
- Store files temporarily in **cloud storage** for accessibility.

---

This project is built to demonstrate **backend development skills** using Django and DRF without a UI. 🚀



