"""
 General Paper Class
"""

class Paper:
    def __init__(self, url="") -> None:
        self.url              = url
        self.title            = ""
        self.authors          = []
        self.corr_author_info = ""
        self.journal_info     = ""
        self.keywords         = []
        self.abstract         = ""
        self.publish_date     = ""

    # def get_title(self, class_name="art_title"):
    #     try:
    #         title_node = self.bs_form.find(class_=class_name)
    #         self.title = title_node.get_text()

    #     except:
    #         print("[-] Warning: Get Title failed!")
    
    # def get_authors(self, meta_property="article:author"):
    #     try:
    #         # <meta property="article:author" content="Thomas Raymen, Oliver Smith" />
    #         authors      = self.bs_form.find(attrs={"property":meta_property})["content"]
    #         self.authors = authors.split(",")

    #     except:
    #         print("[-] Warning: Get Authors failed!")

    # def get_corr_author_info(self, class_name = "artice-notes"):
    #     try:
    #         self.corr_author_info = self.bs_form.find(class_=class_name).get_text()

    #     except:
    #         print("[-] Warning: Get Corresponding Author Info failed!")

    # def get_journal_info(self, meta_name="citation_journal_title"):
    #     try:
    #         # <meta name="citation_journal_title" content="Journal of Consumer Culture" />
    #         self.journal_info = self.bs_form.find(attrs={"name":meta_name})["content"]

    #     except:
    #         print("[-] Warning: Get Journal info failed!")

    # def get_abstract(self, class_name = "abstractSection abstractInFull"):
    #     try:
    #         self.abstract = self.bs_form.find(class_=class_name).get_text()

    #     except:
    #         print("[-] Warning: Get Abstract failed!")

    # def get_keywords(self, class_name = "hlFld-KeywordText"):
    #     try:
    #         self.keywords = self.bs_form.find(class_=class_name).get_text().replace('Keywords ','').split(', ')

    #     except:
    #         print("[-] Warning: Get Keywords failed!")

    # def get_publish_date(self, meta_property="article:published_time - datetime"):
    #     try:
    #         # <meta property="article:published_time - datetime" content="October 16, 2017" />
    #         self.publish_date      = self.bs_form.find(attrs={"property":meta_property})["content"]

    #     except:
    #         print("[-] Warning: Get Authors failed!")

    def authors_to_string(self):
        authors = ""
        for author in self.authors:
            authors += author
            authors += ','
        return authors

    def keywords_to_string(self):
        keywords = ""
        for keyword in self.keywords:
            keywords += keyword
            keywords += ','
        return keywords
