import uuid

import pytest

from badlight.user.services import UserService


@pytest.fixture
def get_user_query():
    query = """
        query FetchUUIDQuery($uuid: String!) {
            user(uuid: $uuid){
                email
                name
            }
        }
    """
    return query


@pytest.fixture
def create_user_mutation():
    mutation = """
        mutation CreateUserQuery(
        $first_name: String!,
        $last_name: String!,
        $email: String!,
        $password: String!
        ) {
        createUser(
            firstName: $first_name,
            lastName: $last_name,
            email: $email,
            password: $password
        ){
            name
            email
            }
        }
    """
    return mutation


def test_get_user_query(graphql_client, get_user_query, snapshot):
    first_name, last_name, email, password = ("test",)*4
    user = UserService.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
    )

    snapshot.assert_match(
        graphql_client.execute(
            get_user_query,
            variables={"uuid": str(user.uuid)}
        )
    )


def test_get_user_query_bad_query(graphql_client, get_user_query, snapshot):
    snapshot.assert_match(
        graphql_client.execute(
            get_user_query,
            variables={"uuid": "does-not-exist"}
        )
    )


def test_get_user_query_user_not_found(graphql_client, get_user_query, snapshot):
    snapshot.assert_match(
        graphql_client.execute(
            get_user_query,
            variables={"uuid": str(uuid.uuid4())}
        )
    )

def test_create_user_mutation(graphql_client, create_user_mutation, snapshot):
    variables = {
        "first_name": "test",
        "last_name": "test",
        "email": "test.test@email.com",
        "password": "test",
    }

    snapshot.assert_match(
        graphql_client.execute(
            create_user_mutation,
            variables=variables,
        )
    )
