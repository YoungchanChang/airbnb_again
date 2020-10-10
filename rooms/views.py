from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models

def all_rooms(request):
    current_page = request.GET.get("page", 1)
    # 초기 페이지 설정 부분
    current_page = int(current_page or 1)

    page_size = 5
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, page_size, orphans=2)
    try:
        rooms = paginator.page(int(current_page))
        # Navigator 설정부분
        block_size = 5
        current_block = ceil(current_page / block_size)

        block_limit = current_block * block_size
        block_offset = block_limit - block_size + 1

        # 마지막 페이지 설정 부분
        # max_page = ceil(models.Room.objects.count() / page_size)
        max_page = paginator.num_pages
        block_end = current_block * block_size
        if (max_page <= block_end):
            block_end = max_page

        return render(
            request,
            "rooms/home.html",
            {
                "rooms": rooms,
                "page": current_page,
                "max_page": max_page,
                "block_end": block_end,
                "page_range": range(block_offset, block_end + 1),
            },
        )
    except EmptyPage:
        return redirect("/")

