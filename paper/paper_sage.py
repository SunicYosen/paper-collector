"""
Papers on Sagepub (https://journals.sagepub.com)
"""

from paper.paper import Paper
from webtools.driver import Driver

class SagePaper(Paper):
    def __init__(self, url) -> None:
        super().__init__(url=url)

        self.driver = Driver()
        self.driver.init_dirver()
        self.driver.get_html_source(self.url)

        self.__init_site_tags()

    def __init_site_tags(self):
        self.title_class_name             = "art_title"
        self.authors_meta_property        = "article:author"
        self.corr_author_info_class_name  = "artice-notes"
        self.journal_info_meta_name       = "citation_journal_title"
        self.keywords_class_name          = "hlFld-KeywordText"
        self.abstract_class_name          = "abstractSection abstractInFull"
        self.publish_date_meta_property   = "article:published_time - datetime"

    def save_paper_html(self, file_name="paper.html"):
        self.driver.save_html(html_file=file_name)

    def get_title(self):
        self.title = self.driver.find_by_class_name(class_name=self.title_class_name)

    def get_authors(self):
        self.authors = self.driver.find_all_by_meta_property(meta_property=self.authors_meta_property)

    def get_corr_author_info(self):
        self.corr_author_info = self.driver.find_by_class_name(class_name=self.corr_author_info_class_name)

    def get_journal_info(self):
        self.journal_info = self.driver.find_by_meta_name(meta_name=self.journal_info_meta_name)

    def get_keywords(self):
        self.keywords = self.driver.find_all_by_class_name(class_name=self.keywords_class_name)

    def get_abstract(self):
        self.abstract = self.driver.find_by_class_name(class_name=self.abstract_class_name)

    def get_publish_date(self):
        self.publish_date = self.driver.find_by_meta_property(meta_property=self.publish_date_meta_property)

    def get_all(self):
        self.get_title()
        self.get_authors()
        self.get_corr_author_info()
        self.get_journal_info()
        self.get_keywords()
        self.get_abstract()
        self.get_publish_date()

def main():
    url    = "https://onlinelibrary.wiley.com/doi/abs/10.1111/ijcs.12660"
    paper0 = SagePaper(url=url)
    paper0.get_all()
    print(paper0.publish_date)

if __name__ == "__main__":
    main()