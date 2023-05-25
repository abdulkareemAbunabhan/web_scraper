import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    """this function used to count how many citation needed in the site"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_tags = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
    return len(citation_tags)


def get_citations_needed_report(url):
    """this function return a report contains all the paragraphs that need citation"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_tags = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
    report = ""
    for tag in citation_tags:
        parent = tag.find_parent("p")
        text = parent.get_text(strip=True)
        report += f"- {text}\n"
    return report


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    count = get_citations_needed_count(url)
    report = get_citations_needed_report(url)

    print(f"Number of citations needed: {count}")
    print("Citations needed report:")
    print(report)