from horoscope import generated_prophecies
from datetime import datetime as dt



def generate_page(head, body):
    page = "<html>" + head + body + "</html>"
    return page

def generate_head(title):
    head = "<meta charset='utf-8'>" + "<title>" + title + "</title>"
    return "<head>" + head + "</head>"

def generate_body(header, paragraphs):
    body = "<h1>" + header + "</h1>"
    i = 0
    while i < len(paragraphs):
        body = body + "<p>" + paragraphs[i] + "</p>"
        i = i + 1
    return "<body>" + body + "</body>"
def save_page(title, header, paragraphs, output="index.html"):
    fp = open(output, "w", encoding="utf-8")
    today = dt.now().date()
    header += ' ' + str(today)
    page = generate_page(
        head=generate_head(title),
        body = generate_body(header = header, paragraphs = paragraphs)
    )   
    print(page, file = fp)
    fp.close()

today = dt.now().date()
save_page(title = "horoscope on today", header = "what the day prepare ", paragraphs = generated_prophecies())
