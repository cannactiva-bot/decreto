"""Pipe-test final de los hooks reales."""
import subprocess, json, os

mock_match = json.dumps({"tool_name":"Bash","tool_input":{"command":"python C:/Users/micro/Desktop/cnmc/_apply_TEST.py"}})
mock_no = json.dumps({"tool_name":"Bash","tool_input":{"command":"git status"}})

print('=== HOOK 1 (backup_v4.sh) con MATCH ===')
r = subprocess.run(['bash', '/c/Users/micro/Desktop/cnmc/.claude/hooks/backup_v4.sh'],
                   input=mock_match, capture_output=True, text=True, timeout=10)
print(f'  exit={r.returncode}  stdout={r.stdout!r}  stderr={r.stderr!r}')

backups = sorted(os.listdir(r'C:\Users\micro\Desktop\cnmc\_backups'))
print(f'  Backups creados: {len(backups)}')
for b in backups[-3:]:
    print(f'    {b}')

print()
print('=== HOOK 1 (backup_v4.sh) con NO match ==')
n_before = len(os.listdir(r'C:\Users\micro\Desktop\cnmc\_backups'))
r = subprocess.run(['bash', '/c/Users/micro/Desktop/cnmc/.claude/hooks/backup_v4.sh'],
                   input=mock_no, capture_output=True, text=True, timeout=10)
n_after = len(os.listdir(r'C:\Users\micro\Desktop\cnmc\_backups'))
print(f'  exit={r.returncode}  backups antes={n_before} despues={n_after} (debe ser igual)')

print()
print('=== HOOK 2 (post_apply.sh) con NO match (rapido) ==')
r = subprocess.run(['bash', '/c/Users/micro/Desktop/cnmc/.claude/hooks/post_apply.sh'],
                   input=mock_no, capture_output=True, text=True, timeout=10)
print(f'  exit={r.returncode}  stdout={r.stdout!r}')

print()
print('=== Settings JSON listo ===')
with open(r'C:\Users\micro\Desktop\cnmc\.claude\settings.json', encoding='utf-8') as f:
    print(f.read())
