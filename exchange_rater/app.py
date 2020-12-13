# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""


import logging
import sys
from typing import NoReturn

from flask import Flask

from exchange_rater import commands
from exchange_rater.blueprints import user, raters
from exchange_rater.extensions import (
    db,
    migrate,
)


def create_app(config_object="exchange_rater.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    register_commands(app)
    configure_logger(app)
    return app


def register_extensions(app) -> NoReturn:
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app) -> NoReturn:
    """Register Flask blueprints."""
    app.register_blueprint(user.views.blueprint)


def register_shellcontext(app) -> NoReturn:
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db, "User": user.models.User}

    app.shell_context_processor(shell_context)


def register_commands(app) -> NoReturn:
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)


def configure_logger(app) -> NoReturn:
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
