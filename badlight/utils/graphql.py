from flask_graphql import GraphQLView


def initialize_graphql(*, app, schema):
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True,),
    )
    return app
