from bs4 import BeautifulSoup

def extract_rules(html):
    soup = BeautifulSoup(html, "html.parser")
    paras = soup.find_all("p")
    rules = []
    for p in paras:
        text = p.get_text().strip()
        if len(text) > 80:
            rules.append({
                "text": text,
                "source": "public_real_case.html",
                "doctrines": ["Doctrine 224", "TAG-001"]
            })
    return rules
