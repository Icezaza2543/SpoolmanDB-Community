import csv
import importlib
import json
from pathlib import Path
import subprocess

import pytest

ROOT=Path(__file__).resolve().parents[1]

@pytest.fixture
def pending_catalog(tmp_path):
    (tmp_path/'filaments').mkdir(); (tmp_path/'contracts').mkdir()
    definition={'name':'PETG {color_name}','material':'PETG','density':1.27,'weights':[{'weight':1000,'spool_type':'plastic'}],'diameters':[1.75],'colors':[{'name':'Black','hex':'000000'}]}
    (tmp_path/'filaments/acme.json').write_text(json.dumps({'manufacturer':'Acme','filaments':[definition,{**definition,'name':'Acme PETG {color_name}'}]}))
    for name in ('not_duplicates','owner_pending_duplicates'):
        (tmp_path/f'contracts/{name}.json').write_text(json.dumps({'version':1,'groups':{}}))
    def git(*args):
        return subprocess.check_output(['git',*args],cwd=tmp_path,text=True).strip()
    git('init'); git('config','user.name','Fixture'); git('config','user.email','fixture@example.invalid');git('add','.');git('commit','-m','existing duplicate fixture')
    return tmp_path,git('rev-parse','HEAD')

def check(root,base=None):
    return importlib.import_module('scripts.duplicate_guard').check_duplicate_candidates(root,base)

def pending(root):
    catalog=importlib.import_module('scripts.duplicate_catalog')
    gid,rows=next(iter(catalog.candidate_groups(catalog.catalog_records(root)).items()))
    ids=[r['record']['id'] for r in rows]
    entry={'ids':ids,'reason':'Owner decision required','ref':'docs/audits/backlog-decisions.csv','source':'a'*40}
    (root/'contracts/owner_pending_duplicates.json').write_text(json.dumps({'version':1,'groups':{gid:entry}}))
    path=root/'docs/audits/backlog-decisions.csv';path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='',encoding='utf-8') as h:
        writer=csv.DictWriter(h,fieldnames=['group_id','side_a_id','side_b_id']);writer.writeheader();writer.writerow({'group_id':gid,'side_a_id':ids[0],'side_b_id':';'.join(ids[1:])})
    return gid,ids

def test_existing_candidate_fails_full_enforcement(pending_catalog):
    root,base=pending_catalog
    errors,warnings=check(root,base)
    assert len(errors)==1 and warnings==[]

def test_head_only_candidate_fails_full_enforcement(pending_catalog):
    root,_=pending_catalog
    assert len(check(root)[0])==1

def test_exact_owner_pending_membership_passes(pending_catalog):
    root,base=pending_catalog;pending(root)
    assert check(root,base)==([],[])

@pytest.mark.parametrize('damage',['missing','wrong_id','duplicate_row','extra_row','short_row'])
def test_pending_sheet_mismatch_fails_closed(pending_catalog,damage):
    root,base=pending_catalog;gid,ids=pending(root);path=root/'docs/audits/backlog-decisions.csv'
    if damage=='missing':path.unlink()
    elif damage=='wrong_id':path.write_text(path.read_text().replace(ids[0],'unrelated_id'))
    elif damage=='duplicate_row':path.write_text(path.read_text()+path.read_text().splitlines()[1]+'\n')
    elif damage=='short_row':path.write_text('group_id,side_a_id,side_b_id\n'+gid+'\n')
    else:path.write_text(path.read_text()+'unrelated,other_a,other_b\n')
    assert check(root,base)[0]

def test_pending_membership_does_not_exempt_new_member(pending_catalog):
    root,base=pending_catalog;pending(root)
    path=root/'filaments/acme.json';data=json.loads(path.read_text());data['filaments'].append({**data['filaments'][0],'name':'PETG ({color_name})'});path.write_text(json.dumps(data))
    assert check(root,base)[0]

def test_stale_pending_entry_fails(pending_catalog):
    root,base=pending_catalog;pending(root)
    path=root/'filaments/acme.json';data=json.loads(path.read_text());data['filaments'].pop();path.write_text(json.dumps(data))
    assert check(root,base)[0]

def test_pending_and_nonduplicate_overlap_fails(pending_catalog):
    root,base=pending_catalog;pending(root)
    (root/'contracts/not_duplicates.json').write_text((root/'contracts/owner_pending_duplicates.json').read_text())
    assert check(root,base)[0]

def test_pending_requires_exact_fields_and_membership(pending_catalog):
    root,base=pending_catalog
    (root/'contracts/owner_pending_duplicates.json').write_text(json.dumps({'version':1,'groups':{'all':{'manufacturer':'Acme'}}}))
    assert check(root,base)[0]

def test_full_audit_cli_reports_unresolved_then_pending(pending_catalog):
    root,_=pending_catalog
    cmd=['python',str(ROOT/'scripts/audit_duplicates.py'),'--all','--root',str(root)]
    result=subprocess.run(cmd,capture_output=True,text=True)
    assert result.returncode==1
    assert json.loads(result.stdout)['summary']['unresolved']==1
    pending(root)
    result=subprocess.run(cmd,capture_output=True,text=True)
    assert result.returncode==0
    report=json.loads(result.stdout)
    assert report['summary']=={'sources':1,'records':2,'candidates':1,'not_duplicates':0,'owner_pending':1,'unresolved':0}

def test_full_audit_enumerates_other_source_files(pending_catalog):
    root,_=pending_catalog;pending(root)
    path=root/'filaments/acme.json';data=json.loads(path.read_text());data['manufacturer']='Beta';data['filaments'][1]['name']='Beta PETG {color_name}';(root/'filaments/beta.json').write_text(json.dumps(data))
    result=subprocess.run(['python',str(ROOT/'scripts/audit_duplicates.py'),'--all','--root',str(root)],capture_output=True,text=True)
    assert result.returncode==1
    report=json.loads(result.stdout)
    assert report['summary']['sources']==2 and report['summary']['unresolved']==1
