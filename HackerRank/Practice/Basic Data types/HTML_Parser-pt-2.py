from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Comment :", data)

    def handle_data(self, data) -> None:
        print("Data :", data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
print('-----')
# parser.close()
# parser.feed(html)
print(parser.feed(html))
parser.close()
