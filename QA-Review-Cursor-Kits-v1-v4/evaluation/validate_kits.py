#!/usr/bin/env python3
"""Validate kit structure and shared fixture integrity; not an AI quality test."""
from pathlib import Path
import csv, hashlib, zipfile, json
ROOT=Path(__file__).resolve().parents[1]
folders=['v1-basic','v2-viewpoint-risk','v3-ba-qa-uat','v4-workflow-first']
errors=[]
for folder in folders:
    kit=ROOT/'kits'/folder
    expected=['README.md','WORKFLOW.md','EVALUATION_SCHEMA.md','VERSION.json','.cursor/skills/qa-review/SKILL.md','input/requirements.md','input/testcases.csv']
    for file in expected:
        if not (kit/file).is_file(): errors.append(f'{folder} missing {file}')
    for filename in ['requirements.md','testcases.csv']:
        a=kit/'input'/filename;b=ROOT/'fixtures/qa-core'/filename
        if a.is_file() and a.read_bytes()!=b.read_bytes():errors.append(f'{folder} input mismatch: {filename}')
    if (kit/'.cursor/skills/qa-review/SKILL.md').is_file():
        txt=(kit/'.cursor/skills/qa-review/SKILL.md').read_text()
        if not txt.startswith('---\n') or '\ndescription:' not in txt: errors.append(f'{folder}: bad skill frontmatter')
    print(folder, 'OK' if not any(folder in err for err in errors) else 'ERROR')
# XLSX genuine dropdown
p=ROOT/'kits/v4-workflow-first/templates/review-sheet-demo.xlsx'
if not p.is_file(): errors.append('v4 missing Excel demo')
else:
    with zipfile.ZipFile(p) as z:
        if not any(b'dataValidation' in z.read(n) for n in z.namelist() if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')):
            errors.append('v4 Excel missing functional data validation')
print('QA Core TC count:',sum(1 for _ in csv.DictReader((ROOT/'fixtures/qa-core/testcases.csv').open())))
print('Problems:',len(errors))
for e in errors:print(' -',e)
raise SystemExit(1 if errors else 0)
