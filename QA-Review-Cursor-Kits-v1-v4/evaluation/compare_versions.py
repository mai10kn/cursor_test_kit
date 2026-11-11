#!/usr/bin/env python3
"""Compare actual AI outputs from each kit against hidden synthetic QA Core labels.
Run from package root: python evaluation/compare_versions.py
This does not run Cursor. Missing predictions are reported as NOT_RUN.
"""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
TRUTH={(x['tc_id'],x['code']) for x in json.loads((BASE/'evaluation/ground-truth/qa-core-labels.json').read_text(encoding='utf-8'))['issues']}
VERSIONS=[('v1','v1-basic'),('v2','v2-viewpoint-risk'),('v3','v3-ba-qa-uat'),('v4','v4-workflow-first')]
print('VERSION | STATUS | TP | FP | FN | PRECISION | RECALL | F1')
for v,folder in VERSIONS:
    path=BASE/'kits'/folder/'output/findings.json'
    if not path.is_file():
        print(f'{v} | NOT_RUN | - | - | - | - | - | -')
        continue
    try:
        obj=json.loads(path.read_text(encoding='utf-8-sig'))
        if obj.get('input_scope','qa-core')!='qa-core':
            print(f'{v} | WRONG_SCOPE | - | - | - | - | - | -')
            continue
        issues=obj['issues']
        pred={(str(x['tc_id']).strip(),str(x['code']).strip().upper()) for x in issues}
        if len(pred)!=len(issues):
            print(f'Warning {v}: duplicate (tc_id,code) pairs collapsed for scoring.')
        tp=len(pred & TRUTH); fp=len(pred-TRUTH); fn=len(TRUTH-pred)
        p=tp/(tp+fp) if tp+fp else 0.0
        r=tp/(tp+fn) if tp+fn else 1.0
        f1=2*p*r/(p+r) if p+r else 0.0
        print(f'{v} | EVALUATED | {tp} | {fp} | {fn} | {p:.3f} | {r:.3f} | {f1:.3f}')
    except Exception as e:
        print(f'{v} | INVALID_OUTPUT ({type(e).__name__}: {e}) | - | - | - | - | - | -')
