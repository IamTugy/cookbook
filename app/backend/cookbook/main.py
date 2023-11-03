import uvicorn
from environs import Env

from cookbook.bindings import get_bindings
from cookbook.ports.bindings_schema import Bindings
from cookbook.ports.fastapi_app import create_app

env = Env()

environment = env.str("ENV", 'dev')

bindings: Bindings = get_bindings(environment)

app = create_app(bindings)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3001)
