from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodPost
from .forms import FoodPostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages

def index(request):
    recent_posts = FoodPost.objects.all().order_by('-id')[:3]  # latest 3 posts
    return render(request, 'foodshare/index.html', {'recent_posts': recent_posts})



from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    if None in [lat1, lon1, lat2, lon2]:
        return float('inf')
    R = 6371
    lat1, lon1, lat2, lon2 = map(float, [lat1, lon1, lat2, lon2])
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    return 2 * R * asin(sqrt(a))

def listings(request):
    posts = FoodPost.objects.filter(picked_up=False) 
    posts = FoodPost.objects.all()
    category = request.GET.get('category')
    dietary = request.GET.get('dietary')
    distance = request.GET.get('distance')
    user_lat = request.GET.get('latitude')
    user_lon = request.GET.get('longitude')

    if category:
        posts = posts.filter(category=category)
    if dietary:
        posts = posts.filter(dietary=dietary)

    if distance and user_lat and user_lon:
        user_lat = float(user_lat)
        user_lon = float(user_lon)
        max_km = float(distance)

        filtered_posts = []
        for post in posts:
            if post.latitude and post.longitude:
                km = haversine(user_lat, user_lon, post.latitude, post.longitude)
                if km <= max_km:
                    post.distance_km = round(km, 1)
                    filtered_posts.append(post)
        posts = filtered_posts

    return render(request, 'foodshare/listings.html', {'posts': posts})

@never_cache
@login_required
def pickup_view(request, pk):
    post = get_object_or_404(FoodPost, pk=pk)

    if request.method == 'POST':
        post.picked_up = True
        post.picked_up_by = request.user
        post.save()
        # Redirect to listings or success page
        return redirect('listings')

    return render(request, 'foodshare/pickup.html', {'post': post})

@never_cache
@login_required
def post_food(request):
    user = request.user
    
    if request.method == 'POST':
        form = FoodPostForm(request.POST, request.FILES)
        if form.is_valid():
            food_post = form.save(commit=False)
            food_post.user = user

            # Get latitude and longitude from POST
            lat = request.POST.get('latitude')
            lng = request.POST.get('longitude')

            # Convert empty strings to None, else convert to float
            food_post.latitude = float(lat) if lat else None
            food_post.longitude = float(lng) if lng else None

            food_post.save()
            return redirect('listings')
    else:
        form = FoodPostForm()

    user_posts = FoodPost.objects.filter(user=user).order_by('-id')
    return render(request, 'foodshare/post.html', {'form': form, 'user_posts': user_posts})




@never_cache
@login_required
def edit_post(request, pk):
    post = get_object_or_404(FoodPost, pk=pk, user=request.user)
    if request.method == 'POST':
        form = FoodPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_food')
    else:
        form = FoodPostForm(instance=post)
    return render(request, 'foodshare/edit_post.html', {'form': form})

@never_cache
@login_required
def delete_post(request, pk):
    post = get_object_or_404(FoodPost, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_food')
    return render(request, 'foodshare/confirm_delete.html', {'post': post})



