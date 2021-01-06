# -*- coding: utf-8 -*-


from __future__ import absolute_import, division, unicode_literals


from collections import OrderedDict


__schema__ = {
    "feed": {
        "": {
            "label": 30014
        }
    },
    "top": {
        "": {
            "label": 30007
        }
    },
    "popular": {
        "": {
            "label": 30008
        }
    },
    "trending": {
        "": {
            "label": 30009
        },
        "music": {
            "label": 30010,
            "kwargs": {"type": "Music"}
        },
        "gaming": {
            "label": 30011,
            "kwargs": {"type": "Gaming"}
        },
        "news": {
            "label": 30012,
            "kwargs": {"type": "News"}
        },
        "movies": {
            "label": 30013,
            "kwargs": {"type": "Movies"}
        }
    },
    "autogenerated": {
        "popular": {
            "label": 30016,
            "action": "playlist",
            "kwargs": {"playlistId": "PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-"},
            #"kwargs": {"authorId": "UCF0pVplsI8R5kcAqgtoRqoA"}
        },
        "music": {
            "label": 30010,
            "kwargs": {"authorId": "UC-9-kyTW8ZkZNDHQJ6FgpwQ"}
        },
        "sports": {
            "label": 30017,
            "kwargs": {"authorId": "UCEgdi0XIXXZ-qJOFPf4JSKw"}
        },
        "gaming": {
            "label": 30011,
            "kwargs": {"authorId": "UCOpNcN46UbXVtpKMrmU4Abg"}
        },
        "news": {
            "label": 30012,
            "kwargs": {"authorId": "UCYfdidRxbB8Qhf0Nx7ioOYw"}
        },
        "live": {
            "label": 30006,
            "kwargs": {"authorId": "UC4R8DWoMoI7CAwX8_LjQHig"}
        },
        "fashion": {
            "label": 30015,
            "kwargs": {"authorId": "UCrpQ4p1Ql_hG8rKXIKM1MOQ"}
        },
        "learning": {
            "label": 30018,
            "kwargs": {"authorId": "UCtFRv9O2AHqOZjjynzrv-xg"}
        }
    },
    "search": {
        "": {
            "label": 30002,
            "art": {"poster": "DefaultAddonsSearch.png"}
        },
        "videos": {
            "label": 30003,
            "kwargs": {"type": "video"},
            "art": {"poster": "DefaultAddonVideo.png"}
        },
        "channels": {
            "label": 30004,
            "kwargs": {"type": "channel"},
            "art": {"poster": "DefaultArtist.png"}
        },
        "playlists": {
            "label": 30005,
            "kwargs": {"type": "playlist"},
            "art": {"poster": "DefaultPlaylist.png"}
        }
    }
}


__trending_types__ = {
    "Music": 30010,
    "Gaming": 30011,
    "News": 30012,
    "Movies": 30013
}


__query_types__ = {
    "video": 30003,
    "channel": 30004,
    "playlist": 30005
}


__sort_by__ = OrderedDict(
    (
        ("relevance", 30131),
        ("upload_date", 30132),
        ("view_count", 30133),
        ("rating", 30134)
    )
)

sortBy = __sort_by__.keys()


home = (
    {"type": "feed", "optional": True},
    {"type": "top", "optional": True},
    {"type": "popular", "optional": True},
    {"type": "trending", "optional": True},
    {"type": "autogenerated", "style": "popular", "optional": True},
    {"type": "autogenerated", "style": "music", "optional": True},
    {"type": "autogenerated", "style": "sports", "optional": True},
    #{"type": "autogenerated", "style": "gaming", "optional": True},
    {"type": "autogenerated", "style": "news", "optional": True},
    {"type": "autogenerated", "style": "live", "optional": True},
    #{"type": "autogenerated", "style": "fashion", "optional": True},
    {"type": "autogenerated", "style": "learning", "optional": True},
    {"type": "search"}
)


styles = {
    "trending": ("music", "gaming", "news", "movies"),
    "search": ("videos", "channels", "playlists")
}
