from shared.util.util import spaceFormat
from plover.system import english_stenotype as e

try:
    from plover_python_dictionary_lib import get_context_from_system
except ImportError:
    from plover_python_dictionary_lib.plover_python_dictionary_lib import get_context_from_system

# ======== Boilerplate to set up objects.
context = get_context_from_system(e)
s = context.SingleDictionary
stroke = context.stroke
translation = context.translation


def getPrefixes(prefixes):
    return s(prefixes).map(spaceFormat)
