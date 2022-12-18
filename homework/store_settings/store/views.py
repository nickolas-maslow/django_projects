from django.shortcuts import render
from django.http import HttpResponse
import xlwt
from store.models import Product


def index(request):
    return render(request, "store/home.html")


def export_products_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="products.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Products')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Label', 'Amount', 'Not bubble price', 'Bubble percentage', 'Final price', 'VAT price', 'Overall']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Product.objects.all().values_list('label', 'amount', 'not_bubble_price', 'bubble_percentage', 'final_price', 'VAT_price', 'overall')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

