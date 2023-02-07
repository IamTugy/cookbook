from environs import Env

from src.ports.bindings.bindings_schema import Bindings
from src.ports.bindings.dev.core import DevBindings
from src.ports.bindings.localhost.core import LocalBindings

env = Env()

ENVIRONMENT = env.str("ENV", 'dev')

bindings: Bindings = {
    'dev': DevBindings,
    'local': LocalBindings,
}.get(ENVIRONMENT)()
