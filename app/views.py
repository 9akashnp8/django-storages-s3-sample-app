from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import InvoiceUploadForm
from .models import Invoice

# manual upload to boto3 also possible
# this can get us maybe the url post upload
# using which we can maybe allow user to view/embed
# download

# Create your views here.
def home(request):
    invoices = Invoice.objects.all()
    context = {'invoices': invoices}
    return render(request, 'home.html', context)

def upload(request):
    form = InvoiceUploadForm()
    if request.method == "POST":
        form = InvoiceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'form': form}
    return render(request, 'upload.html', context)
    

def download(request, id):
    invoice = Invoice.objects.get(id=id)
    doc = invoice.invoice_doc
    response = HttpResponse(doc, headers={
        'Content-Disposition': f'attachment; filename={doc.name}'
    })
    return response