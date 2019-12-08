from part2 import run_program


def test_run_program(monkeypatch, capsys):

    def _parse_test_input(x):
        return [int(x) for x in x.strip().split(',')]

    def _test(test_program, test_input, expected_output):
        monkeypatch.setattr("builtins.input", lambda _: str(test_input))
        run_program(_parse_test_input(test_program))
        captured = capsys.readouterr()
        assert captured.out == f"{expected_output}\n"

    test1 = "3,9,8,9,10,9,4,9,99,-1,8"
    _test(test1, 1, 0)
    _test(test1, 8, 1)

    test2 = "3,9,7,9,10,9,4,9,99,-1,8"
    _test(test2, 1, 1)
    _test(test2, 8, 0)

    test3 = "3,3,1108,-1,8,3,4,3,99"
    _test(test3, 8, 1)
    _test(test3, 1, 0)

    test4 = "3,3,1107,-1,8,3,4,3,99"
    _test(test4, 1, 1)
    _test(test4, 8, 0)

    test5 = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    _test(test5, 0, 0)
    _test(test5, 1, 1)

    test6 = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
    _test(test6, 0, 0)
    _test(test6, 1, 1)

    test7 = ("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,"
             "1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"
             "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
    _test(test7, 7, 999)
    _test(test7, 8, 1000)
    _test(test7, 9, 1001)
