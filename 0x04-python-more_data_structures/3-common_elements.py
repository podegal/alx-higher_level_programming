#!/usr/bin/python3
def common_elements(set_1, set_2):
    _commonElements = []
    for a in set_1:
        for b in set_2:
            if a == b:
                _commonElements.append(a)

    return _commonElements
