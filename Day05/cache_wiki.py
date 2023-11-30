import wikipedia
import warnings
import argparse
import json
import logging

def find_pages(all_pages: dict, cur_page: str, links: set, curr_depth: int, max_depth: int) -> None:
    logging.basicConfig(level=logging.INFO)
    logging.info(all_pages)
    all_pages[cur_page] = set()
    for l in links:
        if len(all_pages) >= 1000:
            return
        if curr_depth >= max_depth:
            break
        try:
            page = wikipedia.page(l, auto_suggest=False)
        except (Exception, Warning) as error:
            continue
        if l not in all_pages:
            find_pages(all_pages, l, page.links, curr_depth + 1, max_depth)
        all_pages[cur_page].add(l)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", dest="cur_page", default="Ubisoft")
    parser.add_argument("-d", dest="max_depth", default=3, type=int)
    args = parser.parse_args()

    try:
        page = wikipedia.page(args.cur_page, auto_suggest=False)
    except wikipedia.PageError as error:
        logging.error(' No such page')
        exit()

    links: set = page.links

    all_pages: dict = dict()

    logging.basicConfig(level=logging.INFO)
    find_pages(all_pages, args.cur_page, links, 0, args.max_depth)

    if len(all_pages) >= 20:
        all_pages = {key: list(val) for key, val in all_pages.items()}
        with open('result.json', 'w') as fp:
            json.dump(all_pages, fp)
    else:
        print('Count of links is less than 20. Please change initial page')


if __name__ == '__main__':
    main()

# python3 cache_wiki.py -p 'Erdős number'
