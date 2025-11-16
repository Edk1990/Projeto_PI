#!/usr/bin/env python3
"""Script para verificar imports do app.py"""

import sys

print("=== Verificando imports do app.py ===")

try:
    with open('app.py', 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'import pandas' in content:
        print("❌ ERRO: app.py ainda contém 'import pandas'!")
        sys.exit(1)
    else:
        print("✅ OK: app.py NÃO contém pandas")
        
    if 'import csv' in content:
        print("✅ OK: app.py usa CSV nativo")
    else:
        print("❌ ERRO: app.py não usa CSV")
        sys.exit(1)
        
    print("\n✅ Verificação concluída com sucesso!")
    sys.exit(0)
    
except Exception as e:
    print(f"❌ Erro: {e}")
    sys.exit(1)
