from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.l"""
    with open(RSS_FEED) as rss_file:
        tags = TAG_HTML.findall(rss_file.read())
    return [tag.replace('-', ' ').lower() for tag in tags]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    
    similar_tags = []
    for t1, t2 in product(tags, tags):
        if t1 == t2 or t1[0] != t2[0]:
            continue
        if SequenceMatcher(None, t1, t2).ratio() > SIMILAR:
            similar_tags.append(sorted((t1, t2)))

    return similar_tags
    


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
    # xd = get_tags()
    # fg = get_top_tags(xd)
    # gh = get_similarities(xd)
    # print(gh)
