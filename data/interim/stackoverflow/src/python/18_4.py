from tensorflow.python.framework.type_spec import register_type_spec_from_value_converter
from keras.engine.keras_tensor import KerasTensor

def _get_type_spec(v:KerasTensor) -> tf.TypeSpec:
    return v.type_spec

register_type_spec_from_value_converter(KerasTensor, _get_type_spec)
