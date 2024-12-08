# שימוש בתמונה בסיסית של Python
FROM python:3.9-slim

# הגדרת תיקיית עבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קובץ הדרישות (requirements.txt) והתקנת ספריות Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל הקבצים והתיקיות מהפרויקט לתוך הקונטיינר
COPY . /app/

# הגדרת הפקודה להפעלת האפליקציה
CMD ["python", "main.py"]
