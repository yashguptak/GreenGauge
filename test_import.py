import importlib, sys
try:
    m = importlib.import_module("utils.emissions")
    importlib.reload(m)
    print("MODULE FILE:", getattr(m, "__file__", "NO __file__"))
    print("EXPORTS:", [n for n in dir(m) if not n.startswith("_")])
    print("Has calculate_footprint?", hasattr(m, "calculate_footprint"))
    print("Has lifestyle_footprint?", hasattr(m, "lifestyle_footprint"))
except Exception as e:
    print("IMPORT ERROR:", e)
    sys.exit(1)
