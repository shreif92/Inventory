from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from .filters import *
from django_filters.views import FilterView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



class StocklistView(FilterView):
    queryset = Stock.objects.filter(is_deleted=False)
    filterset_class = StockFilter
    template_name = "inventory.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stocks'] = context['object_list']  # نقل البيانات إلى مفتاح جديد
        return context


class CreateStock(SuccessMessageMixin,generic.CreateView):
    model = Stock
    form_class = StockForm
    template_name = "create_Stock.html"
    success_url = "/"
    success_message = "Stock created successfully..."


class UpdateStock(SuccessMessageMixin,generic.UpdateView):
    model = Stock
    form_class = StockForm
    template_name = "edit_stock.html"
    success_message = "Stock Updated successfully..."


class DeleteStock(generic.View):
    template_name = "delete_stock.html"
    success_message = "Stock Deleted successfully"

    def get(self, request, pk):
        # Render a confirmation page instead of directly deleting
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'stock': stock})

    def post(self, request, pk):
        # Perform deletion only on POST request
        stock = get_object_or_404(Stock, pk=pk)
        if not stock.is_deleted:  # Check if already deleted
            stock.is_deleted = True
            stock.save()
            messages.success(request, self.success_message)
        return redirect('Stocklist')
