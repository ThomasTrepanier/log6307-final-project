@site.register()
def List(url):
    total_videos = 0
    video_list = []
    next_url = url

    while total_videos < 30 and next_url:
        try:
            listhtml = utils.getHtml(next_url, '')
        except:
            return None

        match = re.compile(r'bg-black"><a href="([^"]+).+?<img\s*src="([^"]+).+?<div class="videoDur">([:\d]+).+?<div class="videoTtl" title="([^"]+).*?redirect-link">([^<]+)', re.DOTALL | re.IGNORECASE).findall(listhtml)
        for videopage, img, duration, name, nice in match:
            # Check video duration and continue if less than 15 min
            dur_min = sum(x * int(t) for x, t in zip([60, 1, 1/60], duration.split(":")))
            if dur_min < 15:
                continue
            
            nice = " [COLOR lime][" + nice + "][/COLOR]"
            name = utils.cleantext(name).title()

            contexturl = (utils.addon_sys + "?mode=custom_eroprofile_by_Cumination.Lookupinfo&list_mode=custom_eroprofile_by_Cumination.List&url=" + urllib_parse.quote_plus(BASE_URL + videopage))
            contextmenu = [
                (
                    '[COLOR deeppink]Lookup info[/COLOR]',
                    'RunPlugin(' + contexturl + ')',
                )
            ]
            # Add to temporary list
            video_list.append((name + nice, BASE_URL + videopage, 'Playvid', img, name + nice, duration, contextmenu))
            total_videos += 1

        nextp = re.compile('([^\"]+)\"\D*21_73').search(listhtml)
        next_url = BASE_URL + nextp[1].replace('&amp;', '&') if nextp else None

    # Add video links to Kodi
    for video in video_list:
        site.add_download_link(*video)
        
    if next_url:
        np = int(re.compile('(\d+)\"\D*21_73').search(listhtml)[1])
        cp = np - 1
        lp = re.compile(r'(\d+)\"\D+21_75').search(listhtml)[1]
        nplptxt = 'Next Page (' + str(cp) + ' / ' + str(lp) + ')'

        cm_page = (utils.addon_sys + "?mode=custom_eroprofile_by_Cumination.GotoPage&list_mode=custom_eroprofile_by_Cumination.List&url=" + urllib_parse.quote_plus(next_url) + "&np=" + str(np) + "&lp=" + str(lp))
        cm = [('[COLOR violet]Goto Page #[/COLOR]', 'RunPlugin(' + cm_page + ')')]
        site.add_dir(nplptxt, next_url, 'List', site.img_next, contextm=cm)

    utils.eod()
