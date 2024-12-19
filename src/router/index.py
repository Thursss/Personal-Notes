from flet import RouteChangeEvent, Page
from src.router.routes import routes


def on_route_change(page: Page, e: RouteChangeEvent):
    page.views.clear()
    page.views.append(routes["/"])

    try:
        # 路由切换
        current_view = routes[e.route]
        page.views.append(current_view)
    except KeyError: 
        page.views.append(routes["/404"])

    page.update()


def on_view_pop(page: Page, e: RouteChangeEvent):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)
