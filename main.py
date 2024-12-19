from flet import Page, app, WEB_BROWSER
from src.router.index import on_route_change, on_view_pop


def main(page: Page):
    page.title = "Personal Notes"

    page.on_route_change = lambda e: on_route_change(page, e)
    page.on_view_pop = lambda e: on_view_pop(page, e)
    page.go(page.route)


if __name__ == "__main__":
    app(main, view=WEB_BROWSER)
