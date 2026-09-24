from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Post, Comment, Like, Follow


def home(request):
    posts = Post.objects.all().order_by("-created_at")

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect("login")

        # FOLLOW / UNFOLLOW
        follow_user_id = request.POST.get("follow_user_id")

        if follow_user_id:
            user_to_follow = User.objects.get(id=follow_user_id)

            if user_to_follow != request.user:
                follow = Follow.objects.filter(
                    follower=request.user,
                    following=user_to_follow
                ).first()

                if follow:
                    follow.delete()
                else:
                    Follow.objects.create(
                        follower=request.user,
                        following=user_to_follow
                    )

            return redirect("home")

        # LIKE / UNLIKE
        like_post_id = request.POST.get("like_post_id")

        if like_post_id:
            post = Post.objects.get(id=like_post_id)

            like = Like.objects.filter(
                post=post,
                user=request.user
            ).first()

            if like:
                like.delete()
            else:
                Like.objects.create(
                    post=post,
                    user=request.user
                )

            return redirect("home")

        # ADD COMMENT
        post_id = request.POST.get("post_id")

        if post_id:
            comment_text = request.POST.get("comment")

            if comment_text:
                Comment.objects.create(
                    post_id=post_id,
                    author=request.user,
                    content=comment_text
                )

            return redirect("home")

        # CREATE POST
        content = request.POST.get("content")

        if content:
            Post.objects.create(
                author=request.user,
                content=content
            )

            return redirect("home")

    following_ids = []

    if request.user.is_authenticated:
        following_ids = list(
            Follow.objects.filter(
                follower=request.user
            ).values_list("following_id", flat=True)
        )

    return render(
        request,
        "social/home.html",
        {
            "posts": posts,
            "following_ids": following_ids
        }
    )


def login_view(request):

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        error = "Invalid username or password."

    return render(
        request,
        "social/login.html",
        {"error": error}
    )


def logout_view(request):

    logout(request)

    return redirect("home")


def register(request):

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            error = "Username and password are required."

        elif User.objects.filter(username=username).exists():
            error = "Username already exists."

        else:
            User.objects.create_user(
                username=username,
                password=password
            )

            return redirect("login")

    return render(
        request,
        "social/register.html",
        {"error": error}
    )
def profile(request, username):
    user = User.objects.get(username=username)

    posts = Post.objects.filter(
        author=user
    ).order_by("-created_at")

    followers_count = Follow.objects.filter(
        following=user
    ).count()

    following_count = Follow.objects.filter(
        follower=user
    ).count()

    return render(
        request,
        "social/profile.html",
        {
            "profile_user": user,
            "posts": posts,
            "followers_count": followers_count,
            "following_count": following_count,
        }
    )