import openpyxl


class ReadXlsxService:
    def __init__(self, file):
        self.file = file
        self.headers = []

    def read(self):
        datos = []
        wb = openpyxl.load_workbook(self.file)
        ws = wb.worksheets[0]

        for row in ws.rows:
            for cell in row:
                self.headers.append(str(cell.value).strip().lower().replace(' ', '_'))
            break

        header_range = range(len(self.headers))

        for row in ws.iter_rows(min_row=2):
            record = []
            for i in header_range:
                record.append((self.headers[i], row[i].value))
            datos.append(dict(record))

        return datos
