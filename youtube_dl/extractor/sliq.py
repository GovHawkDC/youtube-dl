 # coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
from ..utils import unescapeHTML


class SliqIE(InfoExtractor):
    _VALID_URL = r'https?:\/\/(?:www\.)?.*harmony\.sliq\.net\/.*'
    _TEST = {
        'url': 'https://sg001-harmony.sliq.net/00327/Harmony/en/PowerBrowser/PowerBrowserV2/20230317/-1/14357',
        'md5': '7cba6a8aa7ff3354abe1e8b30316db2f',
        'info_dict': {
            'id': '42',
            'ext': 'mp4',
            'title': 'House Health & Insurance [Mar 17, 2023 - Upon Adjournment]',
            'thumbnail': 'https://sg001-harmony.sliq.net/00327/Harmony/images/video.png',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        print(url)
        video_id = "42"
        webpage = self._download_webpage(url, video_id)
        # TODO more code goes here, for example ...
        title = self._search_regex(r'<span class="headerTitle".*>(.+?)</span>', webpage, 'title')
        title = unescapeHTML(title)
        print(title)
        url = self._search_regex(r'{"Name":\"Video\",\"Url\":\"(https:\/\/.*\.sliq\.net\/.*\.mp4)', webpage, 'url')
        print(url)
        thumbnail = self._search_regex(r"property=\"og\:image\"\s*content=\"(.*)\"", webpage, 'thumbnail')

        return {
            'id': video_id,
            'title': title,
            'url': url,
            'thumbnail': thumbnail,
        }

# python test/test_download.py TestDownload.test_Sliq