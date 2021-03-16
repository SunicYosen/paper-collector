"""
Main Function
"""

from toc.toc_sage import SageTOC
from paper.paper_sage import SagePaper
from excel.excel import Excel
from openpyxl.styles import Font

def sage(database_url  = "https://journals.sagepub.com", 
         data_type     = "toc",
         journal_names = ["joca"],
         journal_years = [],
         journal_issues= [],
         save_file     = "result/sage.xlsx",
         save_mode     = 'o'):

    excel_title      = ["题目","作者","发表日期","发表刊物","全文链接","关键词","摘要"]
    excel_col_width  = {'A': 50, 'B':20, 'C':20, 'D':30, 'E':50,'F':50, 'G':100}

    excel_inst       = Excel(save_file)

    for journal_name in journal_names:
        excel_inst.write(sheet_name=journal_name, data_array=excel_title, write_mode=save_mode)

        for year in journal_years:
            for issue in journal_issues:
                toc_url  = database_url + '/' + data_type + '/' + journal_name + '/' + str(year) + '/' + str(issue)
                print("[+] Info: TOC: {}".format(toc_url))

                toc_inst = SageTOC(toc_url)
                toc_inst.get_journal_name()
                toc_inst.get_papers()

                excel_inst.write(sheet_name=journal_name, data_array=[toc_inst.journal_name + '-' + toc_inst.journal_subinfo])

                papers_dict = toc_inst.papers
                for key in papers_dict.keys():
                    print("[+] Info: Paper: {}".format(papers_dict[key]))
                    paper = SagePaper(url=papers_dict[key])
                    paper.get_all()
                    data_term = [paper.title, paper.authors_to_string(), paper.publish_date, paper.journal_info, paper.url, paper.keywords_to_string(), paper.abstract]
                    excel_inst.write(sheet_name=journal_name, data_array=data_term)

        excel_inst.set_col_width(sheet_name=journal_name, cols_width=excel_col_width)
        excel_inst.set_row_auto_wraptext_center(sheet_name=journal_name, all=True)
        excel_inst.set_font(sheet_name=journal_name, font_style=Font(name='Times New Roman'), all=True)

if __name__ == "__main__":
    sage()
