"""
Main Function
"""

from libraries.sage import sage
from libraries.wol import wol

def main():
    wol_toc_url          = "https://onlinelibrary.wiley.com/action/doSearch?Ppub=%5B20160315+TO+20210315%5D&SeriesKey=14706431&sortBy=Earliest&startPage=9&pageSize=1000"
    wol_save_excel       = "results/wol.xlsx"

    sage_database_url     = "https://journals.sagepub.com"
    sage_data_type        = "toc"
    sage_journal_names    = ["joca"]
    sage_journal_years    = range(15, 21)
    sage_journal_issues   = range(1,5)
    sage_save_excel       = "results/sage.xlsx"

    sage(database_url  = sage_database_url,
         data_type     = sage_data_type,
         journal_names = sage_journal_names,
         journal_years = sage_journal_years,
         journal_issues= sage_journal_issues,
         save_file     = sage_save_excel,
         save_mode     = 'o')
 
    wol(toc_url        = wol_toc_url,
        save_excel     = wol_save_excel,
        save_mode      = 'o',
        sheet_name     = 'wol_papers')

if __name__ == "__main__":
    main()
