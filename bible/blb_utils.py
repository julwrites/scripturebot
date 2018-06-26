# coding=utf-8

# Python modules
import re
from bs4 import BeautifulSoup

# Local modules
from common import debug, html_utils, constants, text_utils, web_utils
from common.telegram import telegram_utils

from bible import blb_classes

# This URL will return search results
BLB_SEARCH_URL = "https://www.blueletterbible.org/search/preSearch.cfm?Criteria={}&t={}{}"

BLB_VERSIONS = ["NIV", "ESV", "KJV", "NASB", "RSV", "NKJV"]

BLB_VERSE_CLASS = "columns tablet-8 small-10 tablet-order-3 small-order-2"


def format_blb_url(query, version, modifier=""):
    return BLB_SEARCH_URL.format(query, version, modifier)


def fetch_blb(query, version="NASB", modifier=""):
    debug.log("Querying for {}", [query])

    query = query.lower().strip()

    if query is None:
        return None

    formatUrl = format_blb_url(query, version, modifier)

    url, html = html_utils.fetch_html(formatUrl)

    if html is None:
        return None

    soup = html_utils.html_to_soup(html, "nocrumbs")

    if soup is None:
        return None

    return url, html, soup


def get_search_raw(soup, version="NASB"):
    debug.log("Parsing search results")

    # We will need a BLBSearchResult for this
    return None


def get_search(query, version="NASB"):
    debug.log("Word search: {}", [query])

    url, html, soup = fetch_blb(query, version)

    if soup is None:
        return None

    header = "\n".join([tag.text for tag in soup.select("h1")])

    if header == "Search Results":
        results = get_search_raw(soup)

        if results is None:
            return None

        return telegram_utils.join(results.get_results(), "\n\n")

    return None


def get_lexicon(query, version="NASB"):
    debug.log("Fetching Lexicon: {}", [query])

    url, html, soup = fetch_blb(query, version)

    if soup is none:
        return none

    header = "\n".join([tag.text for tag in soup.select("h1")])

    if header.find("Lexicon") != -1:
        return telegram_utils.link(header, url)
    else:
        url, html, soup = fetch_blb(query, version)

        if soup is none:
            return none

        header = "\n".join(
            [tag.text for tag in soup.findAll("p", attrs={id: "lexlist"})])

        return telegram_utils.link(
            header, format_blb_url(query, version, "#s=s_lexiconc"))


def get_versions():
    return BLB_VERSIONS
