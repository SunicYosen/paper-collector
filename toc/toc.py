"""
General Table of Content Class
"""

class TOC:
    def __init__(self, url="") -> None:
        self.url             = url
        self.base_url        = ""
        self.journal_name    = ""
        self.journal_subinfo = ""
        self.papers          = {}

#         self.get_html_bs()

#     def get_html_bs(self):
#         try:    
#             self.html = get_html_source(self.url)

#             with open("toc.html", 'w') as html_file:
#                 html_file.write(self.html)

#             self.bs_form = BeautifulSoup(self.html, 'lxml')

#         except:
#             print("[-] Error: Cannot get html from toc url: {}".format(self.url))
#             exit()

#     def get_journal_info(self, meta_property="og:title"):
#         try:
#             # <meta property="og:title" content="Journal of Consumer Culture - Volume 20, Number 1, Feb 01, 2020" />
#             journal_info      = self.bs_form.find(attrs={"property":meta_property})["content"]
#             self.journal_name = journal_info.split(" - ")[0]
#             self.journal_subinfo = journal_info.split(" - ")[1]

#         except:
#             print("[-] Warning: Get Journal Info failed!")

#     def get_papers(self, class_name = "art_title linkable", base_url="https://journals.sagepub.com"):
#         try:
#             for paper in self.bs_form.find_all('div', class_ = class_name):
#                 paper_name = paper.get_text()
#                 paper_url  = base_url + paper.select('a')[0].get("href")
#                 self.papers.update({paper_name:paper_url})
#         except:
#             print("[-] Warning: Get Papers failed!")

# def main():
#     url  = "https://journals.sagepub.com/toc/joca/20/1"
#     toc0 = TOC(url=url)
#     toc0.get_journal_info()
#     toc0.get_papers()
    
#     print(toc0.papers)

# if __name__ == "__main__":
#     main()