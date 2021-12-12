def url_analysis(url=None):
    import re
    where_manga = re.compile(r'(?:https|http)://(?:www\.|)(.*?)\.com')
    mangasite = re.findall(where_manga, url)

    if mangasite[0] == 'dogemanga':
        from manga_site.dogemanga import dogemanga_main
        dogemanga_main(url)
    else:
        pass