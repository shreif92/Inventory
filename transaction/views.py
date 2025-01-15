from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
# from .filters import *
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy


class CreateSupplier(SuccessMessageMixin,generic.CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/create_supplier.html"
    success_url = reverse_lazy('supplier_list')
    success_message = "Supplier Created successfully..."


class SupplierList(generic.ListView,Paginator):
    model = Supplier
    queryset = Supplier.objects.filter(is_deleted=False)
    template_name = "suppliers/suppliers_list.html"
    context_object_name = "page_obj"
    paginate_by = 3


class UpdateSupplier(SuccessMessageMixin,generic.UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/edit_supplier.html"
    success_url = reverse_lazy('supplier_list')
    success_message = "Supplier Updated successfully..."

class DeleteSupplier(SuccessMessageMixin, generic.DeleteView):
    template_name = "suppliers/delete_supplier.html"
    success_message = "Supplier Deleted successfully..."

    def get(self, request, pk):
        # Render a confirmation page instead of directly deleting
        supplier = get_object_or_404(Supplier, pk=pk)
        return render(request, self.template_name, {'supplier': supplier})

    def post(self, request, pk):
        # Perform deletion only on POST request
        supplier = get_object_or_404(Supplier, pk=pk)  # Corrected: Use `Supplier` instead of `supplier`
        if not supplier.is_deleted:  # Check if already deleted
            supplier.is_deleted = True
            supplier.save()
            messages.success(request, self.success_message)
        return redirect('supplier_list')