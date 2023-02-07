from environs import Env


env = Env()

AUTH0_DOMAIN = env.str("AUTH0_DOMAIN")
AUTH0_NAMESPACE = f'https://{AUTH0_DOMAIN}'
API_AUDIENCE = env.str("API_AUDIENCE")
MANAGEMENT_TOKEN = env.str("MANAGEMENT_TOKEN")
ALGORITHMS = ["RS256"]



auth0_rule_namespace: str = env.str('AUTH0_RULE_NAMESPACE', 'https://github.com/dorinclisu/fastapi-auth0')
