
import chrome_bookmarks
import webbrowser
import sys

def main():
    for url in chrome_bookmarks.urls:
        print(url.url)
        if (url.url == 'https://valiantny.sharepoint.com/sites/CMChangeManagement' or url.url == 'https://developers.google.com/api-client-library/python/'):
            continue
        webbrowser.open_new_tab(url.url)
    sys.exit("0")

main()