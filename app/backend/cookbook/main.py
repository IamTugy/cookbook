import uvicorn
from environs import Env

from cookbook.bindings import DevBindings, LocalHostBindings
from cookbook.ports.bindings_schema import Bindings
from cookbook.ports.fastapi_app import create_app

env = Env()

environment = env.str("ENV", 'dev')

bindings: Bindings = {
    'dev': DevBindings,
    'local': LocalHostBindings,
}.get(environment)

app = create_app(bindings)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8443)
