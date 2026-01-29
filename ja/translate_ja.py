#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import sys

def translate_html_to_japanese(input_file, output_file, article_title_ja):
    """将HTML文件翻译为日文 - 翻译导航、页脚和基本元素"""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 基本替换
    replacements = [
        (r'lang="en"', 'lang="ja"'),
        ('<li><a href="/index.html">Home</a></li>', '<li><a href="/index.html">ホーム</a></li>'),
        ('<li><a href="#article-content">Article</a></li>', '<li><a href="#article-content">記事</a></li>'),
        ('<li><a href="#footer">About</a></li>', '<li><a href="#footer">について</a></li>'),
        ('<li><a href="/index.html#footer">About</a></li>', '<li><a href="/index.html#footer">について</a></li>'),
        ('<h4>Topics</h4>', '<h4>トピック</h4>'),
        ('<h4>Company</h4>', '<h4>会社</h4>'),
        ('<h4>Legal</h4>', '<h4>法的情報</h4>'),
        ('<a href="/index.html#topics">Artificial Intelligence</a>', '<a href="/index.html#topics">人工知能</a>'),
        ('<a href="/index.html#topics">Development Tools</a>', '<a href="/index.html#topics">開発ツール</a>'),
        ('<a href="/index.html#topics">Cloud Infrastructure</a>', '<a href="/index.html#topics">クラウドインフラ</a>'),
        ('<a href="/index.html#topics">Open Source</a>', '<a href="/index.html#topics">オープンソース</a>'),
        ('<a href="/index.html#topics">Development</a>', '<a href="/index.html#topics">開発</a>'),
        ('<a href="/index.html#topics">Infrastructure</a>', '<a href="/index.html#topics">インフラ</a>'),
        ('<a href="/index.html#topics">Security</a>', '<a href="/index.html#topics">セキュリティ</a>'),
        ('<a href="/index.html#footer">About Us</a>', '<a href="/index.html#footer">私たちについて</a>'),
        ('<a href="/index.html#footer">Editorial Team</a>', '<a href="/index.html#footer">編集チーム</a>'),
        ('<a href="/index.html#footer">Contact</a>', '<a href="/index.html#footer">お問い合わせ</a>'),
        ('<a href="/index.html#footer">Careers</a>', '<a href="/index.html#footer">採用情報</a>'),
        ('<a href="/index.html#footer">Advertise</a>', '<a href="/index.html#footer">広告</a>'),
        ('<a href="/index.html#footer">Privacy Policy</a>', '<a href="/index.html#footer">プライバシーポリシー</a>'),
        ('<a href="/index.html#footer">Terms of Service</a>', '<a href="/index.html#footer">利用規約</a>'),
        ('<a href="/index.html#footer">Cookie Policy</a>', '<a href="/index.html#footer">Cookieポリシー</a>'),
        ('<a href="/index.html#footer">Editorial Guidelines</a>', '<a href="/index.html#footer">編集ガイドライン</a>'),
        ('In-depth analysis on artificial intelligence, software development, and emerging technology trends shaping tomorrow\'s digital landscape.',
         '人工知能、ソフトウェア開発、明日のデジタル風景を形作る新興技術トレンドについての詳細な分析。'),
        ('Delivering thoughtful analysis on technology trends, developer tools, and the future of software.',
         'テクノロジートレンド、開発ツール、ソフトウェアの未来についての思慮深い分析を提供します。'),
        ('Empowering informed decisions in technology.',
         'テクノロジーでの情報に基づいた決定を支援します。'),
        ('· Empowering informed decisions in technology.', '· テクノロジーでの情報に基づいた決定を支援します。'),
    ]

    # 执行替换
    for old, new in replacements:
        content = content.replace(old, new)

    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python translate_ja.py <input_file> <output_file> <article_title_ja>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    article_title_ja = sys.argv[3]

    translate_html_to_japanese(input_file, output_file, article_title_ja)
    print(f"Translated {input_file} -> {output_file}")
