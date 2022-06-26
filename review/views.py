""" import render, redirect, reverse, login """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ReviewForm, CommentForm


def review(request):
    """ View Review """
    review = review.objects.all()
    template = 'products/product_detail.html'
    context = {
        'review': review
        }
    return render(request, template, context)


@login_required
def add_review(request):
    """ Add a review """
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to create a review")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save()
                review.product = product
                review.author = request.user
                review.save()

                messages.success(request, "Successfully added your review")
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request, "Failed to add review, please ensure the \
                        form is valid")
        else:
            form = ReviewForm()

        template = 'review/add_review.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


@login_required
def edit_review(request):
    """ Edit a review """
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to edit a review")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save()
                review.product = product
                review.author = request.user
                review.save()

                messages.success(request, "Successfully edited your review")
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request, "Failed to edit review, please ensure the \
                        form is valid")
        else:
            form = ReviewForm()

        template = 'review/edit_review.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


@login_required
def delete_review(request):
    """ Delete own review """
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to delete a review")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:

        review.delete()
        messages.success(request, 'Your review has been deleted')
        return redirect(reverse('products'))

    else:
        messages.error(request, "You are not allowed to do that.")

    return redirect(reverse('products'))


def comment(request):
    """ View Review """
    comment = comments.objects.all()
    template = 'products/product_detail.html'
    context = {
        'comment': review
        }
    return render(request, template, context)


@login_required
def add_comment(request):
    """ Add a comment """
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to add a comment")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                comment = form.save()
                comment.product = product
                comment.author = request.user
                review.save()

                messages.success(request, "Successfully added your comment")
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request, "Failed to add comment, please ensure the \
                        form is valid")
        else:
            form = CommentForm()

        template = 'review/add_comment.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


@login_required
def edit_comment(request):
    """ Edit a comment """
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to edit a comment")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                comment = form.save()
                comment.product = product
                comment.author = request.user
                comment.save()

                messages.success(request, "Successfully edited your comment")
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request, "Failed to edit comment, please ensure the \
                        form is valid")
        else:
            form = CommentForm()

        template = 'review/edit_comment.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


@login_required
def delete_comment(request):
    """ Delete own comment """
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to delete a commment")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:

        comment.delete()
        messages.success(request, 'Your comment has been deleted')
        return redirect(reverse('products'))

    else:
        messages.error(request, "You are not allowed to do that.")

    return redirect(reverse('products'))
