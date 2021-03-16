"""
TOC on  https://journals.sagepub.com/
"""

from toc.toc import TOC
from webtools.driver import Driver

class SageTOC(TOC):
    def __init__(self, url='', base_url="https://journals.sagepub.com") -> None:
        super().__init__(url=url)

        self.base_url = base_url
        self.driver   = Driver()
        self.driver.init_dirver()
        self.driver.get_html_source(self.url)

        self.__init_site_tags()

    def __init_site_tags(self):
        self.journal_name_meta_property = "og:title"
        self.papers_title_class = "ref nowrap"

    def save_toc_html(self, file_name="toc_sage.html"):
        self.driver.save_html(html_file = file_name)

    def get_journal_name(self):
        self.journal_name = self.driver.find_by_meta_property(meta_property=self.journal_name_meta_property)

    def get_papers(self):
        self.papers = self.driver.find_all_href_by_class_name(class_name=self.papers_title_class, base_url=self.base_url)

    def get_all(self):
        self.get_journal_name()
        self.get_papers()

def main():
    url  = "https://journals.sagepub.com/toc/joca/20/1"
    toc0 = SageTOC(url=url)
    toc0.save_toc_html()
    toc0.get_all()

    print(toc0.journal_name)
    print(toc0.papers)

if __name__ == "__main__":
    main()