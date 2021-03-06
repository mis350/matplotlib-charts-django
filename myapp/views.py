from django.shortcuts import render

from .plots import line_plot, pie_plot, bar_plot

# Create your views here.
def index_view(request):
  data = {}

  # prepare chart data
  # You would typically get it from a db
  # here we are using test data

  x = [1,2,3,5,6,7]
  y = [3,2,6,5,5,5]

  # prepare chart and put in context
  c = line_plot(x,y)
  data["chart"] = c

  # you can havle multiple charts
  c2 = pie_plot([5,5,1,6], ["Acc", "MIS", "MGT","MKT"])
  data["chart2"] = c2

  # bar plots
  c3 = bar_plot(["Jan", "Feb", "Mar"], [10,20,10])
  data["chart3"] = c3
  
  return render(request, "index.html", context=data)