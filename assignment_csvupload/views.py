from django.shortcuts import render
from django.conf import settings
import csv, io
import logging
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from assignment_csvupload.models import EventsForm
from django.db import models
# Create your views here.
def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "upload_csv.html", data)
  # if not GET, then proceed
	try:
		print("helo")
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("upload_csv"))
    #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("upload_csv"))
 
		file_data = csv_file.read().decode("utf-8")		
 		
		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		for line in lines:						
			fields = line.split(",")
			data_dict = {}
			data_dict[0] = fields[0]
			data_dict[1] = fields[1]
			data_dict[2] = fields[2]
			data_dict[3] = fields[3]
			
			try:
				
				form = EventsForm(data_dict)

				if form.is_valid():
					print(data_dict)
					form.save()					
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())												
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))					
				pass
 
	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))
 
	return HttpResponseRedirect(reverse("upload_csv"))
