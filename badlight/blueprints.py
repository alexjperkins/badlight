def register_blueprints(app, root):
    from .internal.controller import internal_blueprint

    app.register_blueprint(internal_blueprint, url_prefix=f"/{root}/__internal__")
