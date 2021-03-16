"""
TOC on Wiley online Library (https://onlinelibrary.wiley.com/)
"""

from toc.toc import TOC
from webtools.driver import Driver

class WOLTOC(TOC):
    def __init__(self, url='', base_url="https://onlinelibrary.wiley.com") -> None:
        super().__init__(url=url)

        self.base_url = base_url
        self.driver   = Driver()
        self.driver.init_dirver()
        self.driver.get_html_source(self.url)

        self.__init_site_tags()

    def __init_site_tags(self):
        self.journal_name_class = "result__suffix"
        self.papers_title_class = "publication_title visitable"

    def save_toc_html(self, file_name="toc.html"):
        self.driver.save_html(html_file = file_name)

    def get_journal_name(self):
        self.journal_name = self.driver.find_by_class_name(class_name=self.journal_name_class).replace('"', '')

    def get_papers(self):
        self.papers = self.driver.find_all_href_by_class_name(class_name=self.papers_title_class, base_url=self.base_url)

    def get_all(self):
        self.get_journal_name()
        self.get_papers()

def main():
    url  = "https://onlinelibrary.wiley.com/action/doSearch?Ppub=%5B20160315+TO+20210315%5D&SeriesKey=14706431&sortBy=Earliest&startPage=9&pageSize=1000"
    toc0 = WOLTOC(url=url)
    toc0.save_toc_html()
    toc0.get_all()

    print(toc0.papers)

if __name__ == "__main__":
    main()