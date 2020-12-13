import os
import sys
from pathlib import Path

current_path = os.path.dirname(os.path.abspath(__file__))
project_root = Path(current_path).parent
app_path = os.path.join(project_root, 'exchange_rater')
print(app_path)
if project_root not in sys.path:
    sys.path.append(project_root)
