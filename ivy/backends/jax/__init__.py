import sys
import ivy
import jax as _jax
# noinspection PyPackageRequirements
import jaxlib
import jax.numpy as jnp
from jaxlib.xla_extension import Buffer

# make ivy.Container compatible with jax pytree traversal
from jax.tree_util import register_pytree_node
from jax.tree_util import tree_flatten, tree_unflatten

register_pytree_node(
    ivy.Container,
    lambda c: tree_flatten(c.to_dict()),
    lambda a, c: ivy.Container(tree_unflatten(a, c))
)

# local
from .core import *
from . import nn
from .nn import *

# noinspection PyUnresolvedReferences
use = ivy.framework_handler.ContextManager(sys.modules[__name__])

# noinspection PyUnresolvedReferences,PyProtectedMember
NativeArray = (_jax.interpreters.xla._DeviceArray, jaxlib.xla_extension.DeviceArray, Buffer)
# noinspection PyUnresolvedReferences,PyProtectedMember
NativeVariable = _jax.interpreters.xla._DeviceArray
# noinspection PyUnresolvedReferences
Device = jaxlib.xla_extension.Device
Dtype = jnp.dtype

# data types
int8 = jnp.int8
int16 = jnp.int16
int32 = jnp.int32
int64 = jnp.int64
uint8 = jnp.uint8
uint16 = jnp.uint16
uint32 = jnp.uint32
uint64 = jnp.uint64
bfloat16 = jnp.bfloat16
float16 = jnp.float16
float32 = jnp.float32
float64 = jnp.float64
# noinspection PyShadowingBuiltins
bool = jnp.bool_

backend = 'jax'
