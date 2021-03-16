"""
Main Function for wol(wiley online library, https://onlinelibrary.wiley.com/)
"""

from toc.toc_wol import WOLTOC
from paper.paper_wol import WOLPaper
from excel.excel import Excel
from openpyxl.styles import Font

def wol(toc_url, 
        base_url   = "https://onlinelibrary.wiley.com", 
        save_excel = "results/wol.xlsx", 
        save_mode  = 'o', 
        sheet_name = "wol_papers"):

    excel_title      = ["题目","作者","发表日期","发表刊物","全文链接","关键词","摘要"]
    excel_col_width  = {'A': 50, 'B':20, 'C':20, 'D':30, 'E':50, 'F':50, 'G':100}

    excel_inst       = Excel(save_excel)

    toc_inst         = WOLTOC(url=toc_url, base_url=base_url)
    toc_inst.get_all()

    excel_inst.write(sheet_name=sheet_name, data_array=excel_title, write_mode=save_mode)

    papers_dict = toc_inst.papers

    for key in papers_dict.keys():
        print("[+] Info: Paper: {}".format(papers_dict[key]))
        paper = WOLPaper(url=papers_dict[key])
        paper.get_all()
        data_term = [paper.title, paper.authors_to_string(), paper.publish_date, paper.journal_info, paper.url, paper.keywords_to_string(), paper.abstract]
        excel_inst.write(sheet_name=sheet_name, data_array=data_term)

    excel_inst.set_col_width(sheet_name=sheet_name, cols_width=excel_col_width)
    excel_inst.set_row_auto_wraptext_center(sheet_name=sheet_name, all=True)
    excel_inst.set_font(sheet_name=sheet_name, font_style=Font(name='Times New Roman'), all=True)

if __name__ == "__main__":
    wol()
