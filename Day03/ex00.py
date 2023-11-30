from bs4 import BeautifulSoup as BS

if __name__ == '__main__':
    with open('../materials/evilcorp.html') as file, open('script') as file2:
        html_doc = file.read()
        script = file2.read()

    from_html = BS(html_doc, features='lxml')

    from_html.title.string = "Evil Corp - Stealing your money every day"

    hack_str = f'{from_html.find_all("span")[0].text}, \
    you are hacked!'

    new_tag = from_html.new_tag("h1")
    from_html.body.insert(0, new_tag)
    from_html.body.h1.string = hack_str

    read_script = BS(script, 'lxml')
    script_tag = from_html.new_tag('script')
    from_html.body.insert(0, script_tag)
    from_html.body.script.string = read_script.script.text

    from_html.a['href'] = 'https://mrrobot.fandom.com/wiki/Fsociety'
    from_html.a.string = 'Fsociety'
    print(from_html.prettify())

    with open('../materials/evilcorp_hacked.html', 'w') as file:
        file.write(from_html.prettify())
