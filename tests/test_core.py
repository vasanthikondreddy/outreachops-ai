from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def auth(user='admin'): return {'Authorization':f'Bearer {user}'}

def test_login():
    r=client.get('/api/me',headers=auth()); assert r.status_code==200; assert r.json()['username']=='admin'

def test_tenant_isolation():
    a=client.get('/api/patients',headers=auth('admin')).json()
    b=client.get('/api/patients',headers=auth('hospital2')).json()
    assert a and b
    assert all(x['hospital_id']!=2 for x in a)
    assert all(x['hospital_id']==2 for x in b)

def test_safety_eval():
    r=client.post('/api/evaluation/run',headers=auth()); assert r.status_code==200; assert 'false_negative_rate' in r.json()
