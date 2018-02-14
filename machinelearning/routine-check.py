for pyLib in ['sys', 'numpy', 'matplotlib', 'pandas', 'sklearn']:
    print("Library: ",pyLib)
    map(__import__,{pyLib})
    if pyLib != "sys":
        print(pyLib)
    else:
        print('Module: {}'.format(pyLib.version))

