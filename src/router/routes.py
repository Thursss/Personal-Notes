import src.pages.index as index_pages
import src.pages.not_found as not_found_pages

routes = {
    index_pages.path: index_pages.view,
    not_found_pages.path: not_found_pages.view,
}

if __name__ == "__main__":
    print(routes)
