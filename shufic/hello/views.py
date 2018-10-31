from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comments
from . import Form
from django.template.context_processors import csrf
import time
from django.contrib import auth

def hello(request):
    return HttpResponse("<H1>Hello World</H1>")


def helloT(request):
    names = ["Bogdan", "Alesha", "Bob", "Valera", "Tom"]
    return render(request, "index.html", {"name":"Bogdan", "lastname":"Kozlovsky", "names":names})


def ShowVideos(request):
    content = []

    for vid in Video.objects.all():
        oneVid = [vid]
        oneVid.append(Comments.objects.filter(Comments_Video_id=vid.id))
        content.append(oneVid)
    return render(request, "AllVideos.html", {"content":content,"usename": auth.get_user(request).usename})


def ShowOneVideo(request, video_id):
    comment_from = Form.CommentForm
    args = {}
    args.update(csrf(request))
    args["video"] = Video.objects.get(id=video_id)
    args["Comments"] = Comments.objects.filter(Comments_Video_id=video_id)
    args["Form"] = comment_from
    args["username"] = auth.get_user(request).usename
    return render(request, "OneVideo.html", args)


def AddLike(request, video_id):
    # print(request.path)
    video = Video.objects.get(id=video_id)
    response = redirect("/AllVideos/get/" + str(video_id) + "/")
    response.set_cookie(video_id, "true")
    if video_id in request.COOKIES:
        if request.COOKIES[video_id] == "false":
            video.Video_likos += 1
            response.set_cookie(video_id, "true")
        if request.COOKIES[video_id] == "true":
            video.Video_likos -= 1
            response.set_cookie(video_id, "false")
    else:
        video.Video_likos += 1
        response.set_cookie(video_id, "true")
    video.save()
    return response

def ajax(request):
    if request.GET:
        idvideo = request.GET['addlike']
        video = Video.objects.get(id=idvideo)
        video.Video_likos +=1
        video.save()
    return HttpResponse(video.Video_likos)

def AddCom(request,video_id):
    response = redirect("/AllVideos/get/" + str(video_id) + "/")
    if request.POST:
        if "Comment_Time" in request.COOKIES:
            if (time.time() - float(request.COOKIES["Comment_Time"])) < 20:
               print("Коментарии не возможно чаще 20 секунд")
            else:
                response.set_cookie("Comment_Time", time.time())
                forma = Form.CommentForm(request.POST)
                if forma.is_valid():
                    comment = forma.save(commit = False)
                    comment.Comments_Video = Video.objects.get(id = video_id)
                    forma.save()
        else:
            response.set_cookie("Comment_Time", time.time())
            forma = Form.CommentForm(request.POST)
            if forma.is_valid():
                comment = forma.save(commit=False)
                comment.Comments_Video = Video.objects.get(id=video_id)
                forma.save()
    return response


# Create your views here.
