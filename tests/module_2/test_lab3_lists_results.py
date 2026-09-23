import importlib

from module_2 import lab3_lists_results


def test_should_print_results_list_after_each_mutation(capsys):
    # This module has no main() -- it's a top-level script that mutates and
    # prints `results` as it goes, so reload it to observe a fresh run
    # (the module-level `results = [...]` line resets state each time).
    capsys.readouterr()
    importlib.reload(lab3_lists_results)
    captured = capsys.readouterr()
    assert captured.out.splitlines() == [
        "['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad']",
        "['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Bowser', 'Donkey Kong Jr.']",
        "['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Donkey Kong Jr.']",
        "['Bowser', 'Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Donkey Kong Jr.']",
        '1',
        "['Donkey Kong Jr.', 'Toad', 'Koopa Troopa', 'Yoshi', 'Princess', 'Luigi', 'Mario', 'Bowser']",
    ]
    assert lab3_lists_results.results == [
        "Donkey Kong Jr.", "Toad", "Koopa Troopa", "Yoshi", "Princess", "Luigi", "Mario", "Bowser",
    ]
