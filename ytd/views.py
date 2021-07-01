#import modules

from django.shortcuts import render
from django.http import FileResponse
from pytube import YouTube
import re
import os
import pafy

#homepage

def home(request):
	return render(request, 'index.html')

# get youtube links, showing embed, showing filze size etc...

def download(request):
	global url
	url=request.GET.get('url')
	yt=pafy.new(url)
	video=[]
	video=yt.streams.filter(progressive=True).all()
	embed_link=url.replace( "watch?v=", "embed/")
	if embed_link.startswith('https://m.'):
		embed_link = re.sub(r'https://m.', 'https://www.', embed_link)
	title=yt.title
	context={'video':video, 'embed':embed_link, 'title':title}
	return render(request, 'download.html', context)
	
#downloading start

def downloaded(request, resolution):
	global url
	if request.method=="POST":
		homedir = os.path.expanduser("~")
		dirs = homedir + '/storage/downloads'
		download = YouTube(url).streams.get_by_resolution(resolution).download(dirs)
	return render(request, 'done.html')
