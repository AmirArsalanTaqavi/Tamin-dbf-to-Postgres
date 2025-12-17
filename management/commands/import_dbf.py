import dbfread
from django.core.management.base import BaseCommand
from app.models import Employee, Workplace, MonthlyWorkshopList
# Import other models...

class Command(BaseCommand):
    help = 'Imports legacy DBF files into PostgreSQL'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the .dbf file')
        parser.add_argument('--type', type=str, help='Type of file: employee, workplace, montly_list')

    def decode_text(self, text_bytes):
        """
        THIS IS WHERE YOUR MAGIC ENCODING LOGIC GOES.
        Most Iranian DBFs use 'IranSystem' or 'CP1256'.
        """
        if not text_bytes:
            return None
        try:
            # Example: Try decoding as Windows-1256 (Arabic/Farsi)
            return text_bytes.decode('cp1256').strip()
        except:
            # Fallback or custom mapping logic
            return text_bytes.decode('utf-8', errors='ignore').strip()

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        file_type = kwargs['type']

        self.stdout.write(f"Reading {file_path}...")
        
        # Load DBF (encoding=None is crucial to get raw bytes for manual decoding)
        table = dbfread.DBF(file_path, encoding=None, char_decode_errors='ignore')

        count = 0
        for record in table:
            if file_type == 'employee':
                self.import_employee(record)
            # Add other types...
            count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} records.'))

    def import_employee(self, record):
        # Map DBF columns (DSK_ID, DSK_NAME, etc.) to Django Fields
        # You need to know the DBF column names here
        try:
            Employee.objects.create(
                id=int(record.get('DSK_ID', 0)),
                first_name=self.decode_text(record.get('DSK_NAME')),
                last_name=self.decode_text(record.get('DSK_FNAME')),
                personnel_number=record.get('DSK_PERNO'),
                # ... map the rest of the fields
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error importing row: {e}"))