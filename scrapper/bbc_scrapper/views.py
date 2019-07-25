from django.shortcuts import render, redirect
from django.http import request
from django.http import HttpResponse,HttpResponseNotFound, Http404,  HttpResponseRedirect
from .bbc import bbc_scrap
import json
# Create your views here.


def get_info(request):
    try:
        key_chapter = request.GET['chapter']
        key_news = request.GET['news']
    except:
        return HttpResponse(json.dumps({'Error':'Invalid parameters'}), content_type="application/json")
    data_for_resp = bbc_scrap(key_chapter, int(key_news))
    return HttpResponse(data_for_resp, content_type="application/json")

def test_redirect(request, *args, **kwargs):
    return redirect("/")
