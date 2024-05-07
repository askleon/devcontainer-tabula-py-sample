import tabula

pdf = "sample.pdf"

dfs = tabula.read_pdf(pdf, pages='all')

for df in dfs:
    print(df)