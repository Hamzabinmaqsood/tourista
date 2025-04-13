#!/usr/bin/env python
import os
import sys
from pathlib import Path

def main():
    # Add project root to Python path
    BASE_DIR = Path(__file__).resolve().parent
    sys.path.append(str(BASE_DIR))
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError("Django not installed")
        
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()