import io

from django.shortcuts import render
from django.http import HttpResponse
import xlsxwriter
from offerings.models import Offering


def setup_cashbook(request):
    return render(request, 'cashbook/setup.html')


def generate_total_contributions(request):
    file = io.BytesIO()
    workbook = xlsxwriter.Workbook(file, {'remove_timezone': True})
    worksheet = workbook.add_worksheet('Offerings')
    headers = ['Service', 'Type of Offering', 'Amount', 'Created on']
    workbook.add_format({'num_format': 'mm/dd/yyyy', 'align': 'left'})

    worksheet.set_column(0, 0, 30)
    worksheet.set_column(1, 1, 20)
    worksheet.set_column(2, 2, 20)
    worksheet.set_column(3, 3, 20)

    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    for row, order in enumerate(Offering.objects.all().values_list()):
        row += 1
        worksheet.write(row, 0, order[''])
        worksheet.write(row, 1, order[:2])
        worksheet.write(row, 2, order[:3])
        worksheet.write(row, 3, order[:4])

    workbook.close()

    file.seek(0)
    filename = 'offerings.xlsx'
    response = HttpResponse(
        file,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
    return response