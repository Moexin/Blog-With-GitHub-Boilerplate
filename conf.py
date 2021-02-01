# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 5
archives_page_size = 15
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Moexin/Moexin.Github.io@gh-pages"
}

# 站点设置
site_name = "Moexin's Blog"
site_logo = "${static_prefix}Moexin.jpg"
site_build_date = "2016-01-22T16:51+08:00"
author = "Moexin"
email = "i@dqb.pw"
author_homepage = "https://dqb.pw"
description = "心若浮沉💗浅笑安然"
key_words = ['Moexin', 'Blog', "Moexin's Blog", '萌新']
language = 'zh-CN'
external_links = [
    {
        "name": "TCat云服务",
        "url": "https://tcat.pw",
        "brief": "可能是最走心的云服务商"
    },
    {
        "name": "Moexin's NetDisk",
        "url": "https://pan.dqb.pw",
        "brief": "基于OneDrive的个人网盘"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/Moexin",
        "icon": "gi gi-github"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "AWXSLU0r8WkSTtSRhS9QKy0F-gzGzoHsz",
    "appKey": "vKfe5G9sioi4aMcpqtxXmixq",
    "visitor": True,
    "recordIP": True
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
