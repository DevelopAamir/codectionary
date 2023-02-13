from .models import *
def getContents(request):
    posts = Content.objects.all().order_by('id').reverse()
    results = []
    query = None;
    if 'search' in request.GET:
        if request.GET['search'] != '':
            query = request.GET['search'];
    if query != None:
        query = query.split()
        for post in posts:
            for ask in query:
                if ask.lower() in post.title.lower() or ask.lower() in post.content or ask.lower() in post.desciption or ask.lower() in post.creator.channel_name.lower() or ask.lower() in post.tags:
                    results.append(post)
                    break
    else:
        results =posts
    print(results)
    return results

def getSubscriptions(request):
    subscription = []
    if request.user.is_authenticated:
        subs = Follower.objects.filter(followed_by = request.user).all()
        for sub in subs:
            subscription.append(sub.follow_to)
    return subscription
