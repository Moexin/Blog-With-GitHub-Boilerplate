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
<link rel="shortcut icon" href="${site_prefix}Favicon/favicon.ico">
<link rel="icon" sizes="16x16 32x32 64x64" href="${site_prefix}Favicon/favicon.ico">
<link rel="icon" type="image/png" sizes="196x196" href="${site_prefix}Favicon/favicon-192.png">
<link rel="icon" type="image/png" sizes="160x160" href="${site_prefix}Favicon/favicon-160.png">
<link rel="icon" type="image/png" sizes="96x96" href="${site_prefix}Favicon/favicon-96.png">
<link rel="icon" type="image/png" sizes="64x64" href="${site_prefix}Favicon/favicon-64.png">
<link rel="icon" type="image/png" sizes="32x32" href="${site_prefix}Favicon/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="${site_prefix}Favicon/favicon-16.png">
<link rel="apple-touch-icon" href="${site_prefix}Favicon/favicon-57.png">
<link rel="apple-touch-icon" sizes="114x114" href="${site_prefix}Favicon/favicon-114.png">
<link rel="apple-touch-icon" sizes="72x72" href="${site_prefix}Favicon/favicon-72.png">
<link rel="apple-touch-icon" sizes="144x144" href="${site_prefix}Favicon/favicon-144.png">
<link rel="apple-touch-icon" sizes="60x60" href="${site_prefix}Favicon/favicon-60.png">
<link rel="apple-touch-icon" sizes="120x120" href="${site_prefix}Favicon/favicon-120.png">
<link rel="apple-touch-icon" sizes="76x76" href="${site_prefix}Favicon/favicon-76.png">
<link rel="apple-touch-icon" sizes="152x152" href="${site_prefix}Favicon/favicon-152.png">
<link rel="apple-touch-icon" sizes="180x180" href="${site_prefix}Favicon/favicon-180.png">
<meta name="msapplication-TileColor" content="#FFFFFF">
<meta name="msapplication-TileImage" content="${site_prefix}Favicon/favicon-144.png">
<meta name="msapplication-config" content="${site_prefix}Favicon/browserconfig.xml">
'''

footer_addon = ''

body_addon = ''
