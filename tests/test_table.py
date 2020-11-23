import pandas as pd

with open("tests/index.html", "r") as f:
    table_content = f.read().replace("\n", "")

html_table_list = pd.read_html(table_content, attrs={"class": "tv-data-table"})

print(html_table_list)