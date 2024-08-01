import lief
import sys

if len(sys.argv) < 3:
    print("Required arguments: input path, output path")
    exit(1)


lib_symbols = lief.parse(sys.argv[1])
if lib_symbols is None:
    print("Error opening given BDS file, aborting")
    exit(1)

for s in lib_symbols.static_symbols:
    #only modify local symbols to minimize scope
    s.visibility = lief.ELF.SYMBOL_VISIBILITY.DEFAULT
    if s.binding == lief.ELF.SYMBOL_BINDINGS.LOCAL:
        s.binding = lief.ELF.SYMBOL_BINDINGS.GLOBAL
    lib_symbols.add_dynamic_symbol(s)
lib_symbols.write(sys.argv[2])
