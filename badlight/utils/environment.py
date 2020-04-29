from dotenv import load_dotenv


def initialize_environment(*, environment, env_path=None):
    if environment.lower() == "production":
        return None

    if env_path is None:
        return load_dotenv()

    return load_dotenv(dotenv_path=env_path)
