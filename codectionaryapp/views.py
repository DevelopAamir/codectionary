from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import CreatorForm, UploadContentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone
import json
from django.http import JsonResponse
from .functions import *


def index(request):
    contents = getContents(request)
    subscription = getSubscriptions(request)
    creator = None
    if request.user.is_authenticated:
        user = Creator.objects.filter(user=request.user)
        if user:
            creator = user[0]
    search = ''
    if 'search' in request.GET:
        search = request.GET['search'];
    # if creator:
    #     user = creator[0];
    context = {'title': 'DeVideos - Explore Knowledge online',
               'contents': contents, 'creator_profile': creator, 'subscription': getSubscriptions(request), 'search' : search}
    
    return render(request, 'index.html', context)


def watchpage(request):
    contents = Content.objects.filter(id=request.GET['content'])
    suggession = getContents(request)
    content = None
    if contents:
        content = contents[0]
    creator = None
    context = {'title': 'Flutter Project Best', 'content': content, 'creator_profile': creator,
            'liked': False, 'followed': False, 'saved': False, 'followers': 0,'suggestion': suggession}
    if request.user.is_authenticated:
        user = Creator.objects.filter(user=request.user)
        if user:
            creator = user[0]
        context['creator_profile'] = creator
        if content:
             liked = Like.objects.filter(content=content, liker=request.user)
        if liked:
            context['liked'] = True

        followed = Follower.objects.filter(
            follow_to=content.creator, followed_by=request.user)
        if followed:
            context['followed'] = True

        saved = Saves.objects.filter(content=content, user=request.user)
        if saved:
            context['saved'] = True
  
    if content:
        if content.creator != creator:
            registerView = View(content=content)
            registerView.save()
        
        context['followers'] = len(
            Follower.objects.filter(follow_to=content.creator))
        return render(request, 'watchpage.html', context)
    else:
        return render(request, '404.html', context)


def profile(request, publisher):
    creator = None
    contents = None
    channel_owner = None
    if request.user.is_authenticated:
        user = Creator.objects.filter(user=request.user)
        if user:
            creator = user[0]
    context = {'title': 'Codectionary - Online Learning Channel',
               'creator_profile': creator, 'contents': contents, 'publisher': channel_owner, }

    creators = Creator.objects.filter(channel_name=publisher);
    if creators:
        view = 0
        likes = 0
        channel_owner = creators[0]
        contents = Content.objects.filter(creator=channel_owner).all()
        followers = Follower.objects.filter(follow_to=channel_owner).all()
        for cont in contents:
            li = Like.objects.filter(content= cont).all()
            vi = View.objects.filter(content= cont).all()
            view = view + len(vi)
            likes = likes + len(li)
        context = {'title': 'Codectionary - Online Learning Channel',
               'creator_profile': creator, 'contents': contents, 'publisher': channel_owner,'followers': len(followers), 'uploads': len(contents), 'views':view, 'likes': likes,}
        

        return render(request, 'profile.html', context)
    else:
        return render(request, '404.html',)


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    return render(request, 'login.html', {'title': 'Login - Devideos'})


@login_required(login_url='/login')
def studio(request):
    user = Creator.objects.filter(user=request.user)
  
    if not user:
        return redirect('/updateprofile')
    else:
        content = []
        contents = Content.objects.filter(
            creator=user[0]).all().order_by('id').reverse()
        for con in contents:
            cont = {}
            view = View.objects.filter(content=con)
            like = Like.objects.filter(content=con)
            cont['views'] = len(view)
            cont['like'] = len(like)
            cont['content'] = con
            content.append(cont)

        creators = user
        
        view = 0
        likes = 0
        channel_owner = creators[0]
        contents = Content.objects.filter(creator=channel_owner).all()
        followers = Follower.objects.filter(follow_to=channel_owner).all()
        for cont in contents:
            li = Like.objects.filter(content= cont).all()
            vi = View.objects.filter(content= cont).all()
            view = view + len(vi)
            likes = likes + len(li)
        
        context = {'title': 'Creator Studio - Devideos',
                   'creator_profile': user[0], 'contents_uploaded': content, 'views': view, 'likes': likes, 'followers': len(followers)}
        return render(request, 'studio.html', context)


@login_required(login_url='/login')
def updateprofile(request):
    profile_comp = CreatorForm()
    if request.method == 'POST':

        current = Creator.objects.filter(user=request.user)

        if not current:
            profile_comp = CreatorForm(request.POST, request.FILES)
            if profile_comp.is_valid():
                profile_comp.save()
                return redirect('/studio')
            else:
                return render(request, 'update-profile.html', {'title': 'Update Profile - Devideos', 'userData': current, 'form': profile_comp, 'creator_profile': None})
        else:
            current = Creator.objects.get(user=request.user)
            profile_comp = CreatorForm(
                request.POST, request.FILES, instance=current)
            if profile_comp.is_valid():
                profile_comp.save()

                return redirect('/studio')
            else:
                return render(request, 'update-profile.html', {'title': 'Update Profile - Devideos', 'userData': current, 'form': profile_comp, 'creator_profile': current})
    else:
        users = Creator.objects.filter(user=request.user)
        user = None
        if users:
            user = users[0]
        return render(request, 'update-profile.html', {'title': 'Update Profile - Devideos', 'userData': user, 'form': profile_comp, 'creator_profile': user})


@login_required(login_url='/login')
def uploadContent(request):
    user = Creator.objects.filter(user=request.user)
   
    if not user:
        return redirect('/updateprofile')
    else:
        uploadForm = UploadContentForm()
        if request.method == 'POST':
            uploadForm = UploadContentForm(request.POST, request.FILES)
            if uploadForm.is_valid():
                uploadForm.save()
                messages = ['Successfully Uploaded Video']
                return render(request, 'uploadVideo.html', {'title': 'Upload Videos - Devideos', 'creator_profile': user[0], 'form': uploadForm, 'messages': messages})
            else:
                messages = None
                return render(request, 'uploadVideo.html', {'title': 'Upload Videos - Devideos', 'creator_profile': user[0], 'form': uploadForm, 'messages': messages})
        return render(request, 'uploadVideo.html', {'title': 'Upload Videos - Devideos', 'creator_profile': user[0], 'form': uploadForm})


@login_required(login_url='/login')
def videos(request):
    user = Creator.objects.filter(user=request.user)
    
    if not user:
        return redirect('/updateprofile')
    else:
        content = []
        contents = Content.objects.filter(
            creator=user[0]).all().order_by('id').reverse()
        for con in contents:
            cont = {}
            view = View.objects.filter(content=con)
            like = Like.objects.filter(content=con)
            cont['views'] = len(view)
            cont['like'] = len(like)
            cont['content'] = con
            content.append(cont)
        return render(request, 'videos.html', {'title': 'Upload Videos - Devideos', 'creator_profile': user[0], 'contents_uploaded': content})


@login_required(login_url='/login')
def updateVideo(request):
    user = Creator.objects.filter(user=request.user)
    uploadForm = UploadContentForm()
    
    if not user:
        return redirect('/updateprofile')
    else:
        if request.GET['content']:
            cont = Content.objects.get(id=request.GET['content'])
            uploadForm = UploadContentForm(instance=cont)

        if request.method == 'POST':
            
            if str(request.POST['creator']) == str(user[0].id):
                uploadForm = UploadContentForm(
                    request.POST, request.FILES, instance=cont)
                if uploadForm.is_valid():
                    uploadForm.save()
                    messages = ['Successfully Updated Video']

                    return render(request, 'uploadVideo.html', {'title': 'Upload Videos - Devideos', 'creator_profile': user[0], 'form': uploadForm, 'messages': messages})
                else:
                    messages = None
                    return render(request, 'uploadVideo.html', {'title': 'Upload Videos - Devideos', 'creator_profile': user[0], 'form': uploadForm, 'messages': messages})
            else:
                return HttpResponse('Permission Denied')

        return render(request, 'uploadVideo.html', {'title': 'Upload Videos - Devideos', 'creator_profile': user[0], 'form': uploadForm, 'update': True})


def like(request):
    contents = Content.objects.filter(id=request.GET['content'])
    content = None
    if contents:
        content = contents[0]
    if content:
        if request.method == 'POST':
            if request.user.is_authenticated:
                liked = Like.objects.filter(
                    content=content, liker=request.user)
                if not liked:
                    registerLike = Like(content=content, liker=request.user)
                    registerLike.save()
                    return HttpResponse('liked')
                else:
                    liked.delete()
                    return HttpResponse('removed')
            else:
                return HttpResponse('login')


def follow(request):
    contents = Content.objects.filter(id=request.GET['content'])
    content = None
    if contents:
        content = contents[0]
    if content:
        if request.method == 'POST':
            if request.user.is_authenticated:
                followed = Follower.objects.filter(
                    follow_to=content.creator, followed_by=request.user)
                if not followed:
                    registerLike = Follower(
                        follow_to=content.creator, followed_by=request.user)
                    registerLike.save()
                    return HttpResponse('followed')
                else:
                    followed.delete()
                    return HttpResponse('removed')
            else:
                return HttpResponse('login')

def unfollow(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            followed = Follower.objects.filter(
                follow_to=request.GET['creator'], followed_by=request.user)
            followed.delete()
            return HttpResponse('removed')
        else:
            return HttpResponse('login')


def comment(request):
    contents = Content.objects.filter(id=request.GET['content'])
    content = None
    if contents:
        content = contents[0]
    if content:
        if request.method == 'POST':
            if request.user.is_authenticated:
                comment = Comments(commentor=request.user,
                                   content=content, text=request.GET['msg'])
                comment.save()
                return HttpResponse('commented')
            else:
                return HttpResponse('login')
        else:
            comment = Comments.objects.filter(
                content=content).all().order_by('id').reverse()

            comments_dict = []
            for com in comment.all():
                element = {}
                element['commentor'] = {
                    'id': com.commentor.id,
                    'name': com.commentor.first_name + ' ' + com.commentor.last_name,
                }
                element['text'] = com.text
                element['time'] = com.time.strftime("%Y-%m-%d")
                comments_dict.append(element)

            return HttpResponse(json.dumps(comments_dict), headers={'content-type': 'application/json'})


def save(request):
    contents = Content.objects.filter(id=request.GET['content'])
    content = None
    if contents:
        content = contents[0]
    if content:
        if request.method == 'POST':
            if request.user.is_authenticated:
                saved = Saves.objects.filter(
                    content=content, user=request.user)
                if not saved:
                    registerLike = Saves(content=content, user=request.user)
                    registerLike.save()
                    return HttpResponse('saved')
                else:
                    saved.delete()
                    return HttpResponse('removed')
            else:
                return HttpResponse('login')



@login_required(login_url='/login')
def saved(request):
    contents = []
    creator = None
    if request.user.is_authenticated:
        user = Creator.objects.filter(user=request.user)
        if user:
            creator = user[0]
    saved = Saves.objects.filter(user=request.user).all()
    for save in saved:
        contents.append(save.content)

    context = {'title': 'DeVideos - Explore Knowledge online',
               'contents': contents, 'creator_profile': creator}
    
    return render(request, 'savedVideos.html', context)

@login_required(login_url='/login')
def subscriptions(request):
    creator = None
    subscription = getSubscriptions(request)
    if request.user.is_authenticated:
        user = Creator.objects.filter(user=request.user)
        if user:
            creator = user[0]
    context = {'title': 'DeVideos - Explore Knowledge online',
               'subscriptions': subscription, 'creator_profile': creator}
    return render(request, 'subscriptions.html', context)


@login_required(login_url='/login')
def deleteVideo(request):
    creator = None
    if request.user.is_authenticated:
        user = Creator.objects.filter(user=request.user)
        if user:
            creator = user[0]
    if creator:
        vid = Content.objects.filter(id = request.POST['content'], creator= creator)
        if vid:
            vid.delete()
            return redirect('/videos')
        else:
            return HttpResponse('Un Authorized')

@login_required(login_url='/login')
def earning(request):
    user = Creator.objects.filter(user=request.user)
    
    if not user:
        return redirect('/updateprofile')
    else:
        content = []
        contents = Content.objects.filter(
            creator=user[0]).all()
        followers = Follower.objects.filter(follow_to=user[0]).all()
        # for con in contents:
        #     cont = {}
        #     view = View.objects.filter(content=con)
        #     like = Like.objects.filter(content=con)
        #     cont['views'] = len(view)
        #     cont['like'] = len(like)
        #     cont['content'] = con
        #     content.append(cont)
        return render(request, 'earning.html', {'title': 'Upload Videos - Devideos', 'creator_profile': user[0],'no_of_contents':len(contents),'followers': len(followers)})