#!/usr/bin/env python3
"""Self-tests for static skill utilities, never for a real API or app."""
import csv,json,sys,tempfile,unittest
from pathlib import Path
from copy import deepcopy
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from dry_run_workflow import validate
from audit_acceptance_gates import audit as audit_gates
from audit_requirement_coverage import audit as audit_coverage
from audit_visual_baselines import audit as audit_visual
from audit_workflow_run import audit as audit_run

def data(n):return json.loads((ROOT/'assets/templates'/n).read_text(encoding='utf-8'))
def save_csv(path,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)

class Graph(unittest.TestCase):
    def setUp(self):
        self.g=data('workflow-dry-run-example.json')
        self.r=data('workflow-node-registry-example.json')
    def test_mock_blocked(self):
        x=validate(self.g,self.r)
        self.assertTrue(any('model not verified' in a for a in x['errors']))
        self.assertFalse(x['live_execution'])
    def test_mock_only_fixture(self):
        x=validate(self.g,self.r,allow_mock=True,max_budget=0.15)
        self.assertEqual(x['errors'],[])
        self.assertEqual(len(x['order']),4)
        self.assertEqual(x['estimatedCostUsd'],0.1)
    def test_budget(self):self.assertTrue(any('exceeds budget' in e for e in validate(self.g,self.r,True,0.01)['errors']))
    def test_cycle(self):
        self.g['edges'].append({'id':'cycle','source':'gallery-1','sourcePort':'selectedImage','target':'generate-1','targetPort':'referenceImage'})
        self.assertTrue(any('Cycle detected' in e for e in validate(self.g,self.r,True)['errors']))
    def test_wrong_port(self):
        self.g['edges'][1]['targetPort']='referenceImage'
        self.assertTrue(any('incompatible' in e for e in validate(self.g,self.r,True)['errors']))
    def test_missing_required_port(self):
        self.g['edges']=self.g['edges'][1:]
        self.assertTrue(any('unconnected required' in e for e in validate(self.g,self.r,True)['errors']))
    def test_duplicate_id(self):
        self.g['nodes'].append(deepcopy(self.g['nodes'][0]))
        self.assertTrue(any('Duplicate node id' in e for e in validate(self.g,self.r,True)['errors']))

class Evidence(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        for folder in ('docs','evidence','src'):(self.root/folder).mkdir()
        (self.root/'evidence/test.txt').write_text('actual log fixture')
        (self.root/'src/main.py').write_text('print(123)')
    def tearDown(self):self.temp.cleanup()
    def test_acceptance_pass_and_missing(self):
        fields=['Gate_ID','Requirement_ID','Priority','Description','Status','Evidence_Path','Validation_Command','Verified_At','Owner_Approval','Waiver_ID','Notes']
        row=dict(zip(fields,['G1','REQ-001','P0','spec','PASS','evidence/test.txt','test-command','2026-11-09','YES','','']))
        p=self.root/'docs/ACCEPTANCE_GATES.csv'
        save_csv(p,[row]);self.assertEqual(audit_gates(self.root,True)['errors'],[])
        row['Evidence_Path']='evidence/missing.txt';save_csv(p,[row]);self.assertTrue(audit_gates(self.root,True)['errors'])
    def test_coverage_pass_and_not_run(self):
        fields=['Requirement_ID','Priority','Approved','Feature_ID','UI_Control_ID','Implementation_File','Test_ID','Test_Status','Test_Evidence','Deviation_ID','Notes']
        row=dict(zip(fields,['REQ-001','P0','YES','FEAT-001','CTRL-001','src/main.py','TEST-001','PASS','evidence/test.txt','','']))
        p=self.root/'docs/REQUIREMENT_COVERAGE.csv';save_csv(p,[row]);self.assertEqual(audit_coverage(self.root,True)['errors'],[])
        row['Test_Status']='NOT_RUN';save_csv(p,[row]);self.assertTrue(audit_coverage(self.root,True)['errors'])
    def test_visual_missing_actual(self):
        fields=['Screen_ID','Viewport','Zoom','Platform','Priority','Owner_Approval','Waiver_ID','Baseline_Path','Actual_Path','Review_Status','Reviewer','Diff_Evidence','Notes']
        row=dict(zip(fields,['SCR-001','1280x800','100','web','P0','PENDING','','evidence/test.txt','missing.png','PASS','reviewer','evidence/test.txt','']))
        save_csv(self.root/'docs/VISUAL_BASELINES.csv',[row]);self.assertTrue(audit_visual(self.root,True)['errors'])
    def test_mock_run_cannot_pass(self):
        p=self.root/'docs/run.json';p.write_text(json.dumps(data('workflow-run-snapshot-example.json')))
        self.assertTrue(any('mock or dry' in e for e in audit_run(p,self.root)['errors']))

if __name__=='__main__':unittest.main()
