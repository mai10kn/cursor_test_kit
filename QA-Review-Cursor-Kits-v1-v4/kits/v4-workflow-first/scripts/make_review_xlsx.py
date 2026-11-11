#!/usr/bin/env python3
"""Turn output/review-sheet.csv into formatted .xlsx with functional dropdown.
Usage: python scripts/make_review_xlsx.py [input.csv] [output.xlsx]
Dependency: artifact_tool. Original TC columns are retained as strings; choose source CSV created by Cursor.
"""
from pathlib import Path
import csv, sys
from artifact_tool import Workbook, SpreadsheetFile
root=Path(__file__).resolve().parents[1]
src=Path(sys.argv[1]) if len(sys.argv)>1 else root/'output/review-sheet.csv'
dst=Path(sys.argv[2]) if len(sys.argv)>2 else root/'output/review-sheet.xlsx'
with src.open('r',encoding='utf-8-sig',newline='') as f:
    rows=list(csv.reader(f))
if not rows: raise ValueError('Empty source CSV')
if len(set(rows[0]))!=len(rows[0]): raise ValueError('Duplicate headers')
required=['AI Issue','Suggested Fix','Review Decision']
missing=[x for x in required if x not in rows[0]]
if missing: raise ValueError(f'Missing required columns: {missing}')
col_count=len(rows[0]); row_count=len(rows)
for i,row in enumerate(rows,1):
    if len(row)!=col_count: raise ValueError(f'Row {i} contains {len(row)} columns; expected {col_count}')
wb=Workbook.create(); sh=wb.worksheets.add('Review Sheet')
sh.get_range_by_indexes(0,0,row_count,col_count).values=rows
sh.get_range_by_indexes(0,0,1,col_count).format={
    'fill':'#17365D','font':{'bold':True,'color':'#FFFFFF'},
    'vertical_alignment':'center','wrap_text':True,'row_height':32}
sh.freeze_panes.freeze_rows(1)
for ci,h in enumerate(rows[0]):
    col=sh.get_range_by_indexes(0,ci,row_count,1)
    col.format.column_width=36 if h in ['Steps','Test Steps','Expected Result','AI Issue','Suggested Fix'] else (23 if h=='Review Decision' else 20)
    if ci<len(rows[0])-3: col.set_number_format('@')
sh.get_range_by_indexes(1,0,max(row_count-1,1),col_count).format.wrap_text=True
if row_count>1:
    c=rows[0].index('Review Decision')
    r=sh.get_range_by_indexes(1,c,row_count-1,1)
    r.data_validation={'rule':{'type':'list','values':['Pending','Keep','Modify','Split','Merge','Remove','Clarify','Reject AI Finding']}}
    r.format.fill='#FFF6DB'
    c2=rows[0].index('AI Issue')
    sh.get_range_by_indexes(1,c2,row_count-1,1).format.fill='#EFF6FF'
dst.parent.mkdir(parents=True,exist_ok=True)
SpreadsheetFile.export_xlsx(wb).save(str(dst))
print(f'Created {dst} | {row_count-1} testcases | {col_count} columns')
