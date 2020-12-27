
import os
from pathlib import Path

from environs import Env

from exchange_rater.app import create_app


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))
    current_path = Path(current_path)
    root_path = current_path.parent
    env_path = os.path.join(root_path, '.env')
    env = Env()
    if os.path.exists(env_path):
        env.read_env(env_path)

    app = create_app()
    FLASK_APP_LOCAL_PORT = env.int('FLASK_APP_LOCAL_PORT', default=8000)
    app.run(host='0.0.0.0', port=FLASK_APP_LOCAL_PORT)

