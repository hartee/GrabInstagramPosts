import requests
import re

PERMALINK = """
https://graph.instagram.com/me/media?access_token=IGQVJWMGRIWHp0aXNRSDhxZAlFTdVhxNHVsN3VMT2FrUkIzVFdGNHgxaHExZAFU4aDctXzlJbVlpQVRUeXQzMEpUc2owSHFqWDNwWTlFVE5nNjJIWWc4Q080d2Y4SVA4SUplbHJ4TjFPdGdZAVHpsOE1SXwZDZD&fields=media_url,media_type,caption,permalink,timestamp
"""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_permalink(link):
    response = requests.get(link)
    return response.json()


def extract_title(caption):
    res = re.search("(?P<title>\[(.*)\])", caption)
    if res:
        return res.group(2)
    else:
        return None


def extract_caption(caption):
    res = re.search("(?P<caption>.+?(?=http))", caption.replace("\n", ""))
    if res:
        print (res.group(1))
        return res.group(1)
    else:
        print(caption)
        return caption


def extract_link(caption): 
    res = re.search("(?P<url>https?://[^\s]+)", caption)
    if res:
        return res.group("url")
    else:
        return None


def generate_pages(data):
    for post in data:
        # create new text file <id>.md
        # write out header...
        # ---
        # title: Coldplay - Viva la Vida
        # date: 2020-12-09
        # categories: [music]
        # tags: [music, culture]
        # language: en
        # ---
        #
        # <ims src=media_url>
        # <caption>
        # <a href="https://g.co/kgs/GBxFD2">video</a>
        #
        # f.close()

        print(post["id"])
        fname = post["id"] + ".md"
        f = open(fname, "w+")

        f.write("---  \r\n")

        title = extract_title(post['caption'])
        if title is not None:
            f.write("title:  " + extract_title(post['caption']) + "  \r\n")
        else:
            f.write("title: " + post["id"] + "  \r\n")

        f.write("date: " + post["timestamp"] + "  \r\n")
        f.write("categories: [music]  \r\n")
        f.write("tags: [music, culture]  \r\n")
        f.write("language: en  \r\n")
        f.write("---  \r\n")
        f.write("  \r\n")
        f.write('<img src="' + post["media_url"] + '">   \r\n')
        f.write("   \r\n")

        caption = extract_caption(post['caption'])
        link = extract_link(post['caption'])

        if caption is not None:
            f.write(caption + "  \r\n")
        f.write("   \r\n")
        f.write("   \r\n")


        if link is not None:
            f.write("[video](" + link + ")  \r\n")

        f.close()


if __name__ == '__main__':
    print_hi('PyCharm')
    data = get_permalink(PERMALINK)

    while True:
        next = data['paging'].get('next')
        if next == None:
            print('Finished processing feed')
            break
        else:
            print('Processing...')
            generate_pages(data['data'])
            data = get_permalink(next)
