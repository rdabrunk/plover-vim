from plover_vim.shared.util import spaceFormat
import plover.system as e

from plover_python_dictionary_lib import get_context_from_system

# ======== Boilerplate to set up objects.
context = get_context_from_system(e)
s = context.SingleDictionary
stroke = context.stroke
translation = context.translation


def getPrefixes(prefixes):
    return s(prefixes).map(spaceFormat)
