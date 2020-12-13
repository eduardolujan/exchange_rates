import os
import sys
from pathlib import Path

current_path = os.path.dirname(os.path.abspath(__file__))
project_root = Path(current_path).parent
app_path = os.path.join(project_root, 'exchange_rater')
tests_path = os.path.join(project_root, 'tests')


if project_root not in sys.path and os.path.exists(app_path):
    sys.path.append(project_root)


if tests_path not in sys.path and os.path.exists(tests_path):
    sys.path.append(tests_path)
