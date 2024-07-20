from hkckan import list_packages, show_package, group_list, group_show

def test_packages():
    pkgs = list_packages()
    assert pkgs is not None

    pkg = show_package(pkgs[0])
    assert pkg is not None

def test_groups():
    grps = group_list()
    assert grps is not None

    grp = group_show(grps[0])
    assert grp is not None