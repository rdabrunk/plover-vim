from plover_vim.Josiah_modifier.defaults import shifted_symbols_aus, symbols, spelling

numbers = {
        "": ""
        }

middles = {
        "": ""
        }

defaults = {
        "disable_defaults": False,  # can be spelling, symbols etc ...
        # any dictionary entry overiddes the defaults
        "command_suffix": "{^^}",
        "spelling": spelling,
        "symbols": symbols,
        "shifted": shifted_symbols_aus,
        "numbers": numbers,
        "middles": middles,
        "escape": "escape",
        "systems": []
            }
