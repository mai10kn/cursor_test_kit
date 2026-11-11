#!/usr/bin/env python3
"""Score a model's golden-set findings by (tc_id, code) against annotated labels.
Usage: python scripts/score_golden.py internal/golden-set/labels.json output/golden-predictions.json
Predictions JSON: {"issues":[{"tc_id":"TC-002","code":"INCORRECT_EXPECTED"}, ...]}
"""
import json
import sys
from pathlib import Path

def load_pairs(p):
    doc = json.loads(Path(p).read_text(encoding='utf-8'))
    return {(str(x['tc_id']), str(x['code'])) for x in doc.get('issues', [])}

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python score_golden.py <labels.json> <predictions.json>')
    truth, predicted = map(load_pairs, sys.argv[1:])
    tp = truth & predicted
    fp = predicted - truth
    fn = truth - predicted
    precision = len(tp) / len(predicted) if predicted else 0.0
    recall = len(tp) / len(truth) if truth else 1.0
    print(json.dumps({
        'true_positive':len(tp),'false_positive':len(fp),'false_negative':len(fn),
        'precision':round(precision,4),'recall':round(recall,4),
        'false_positive_pairs':sorted(fp),'missed_pairs':sorted(fn)
    }, ensure_ascii=False, indent=2))
