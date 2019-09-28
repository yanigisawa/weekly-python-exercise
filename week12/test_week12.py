import os
import json
from flask import request
from solution import app, scan, rescan

def make_files(directory, file_list):
    for i in file_list:
        with open(directory / f'file{i}', 'w') as f:
            f.write('abcd\n' * i)



def test_three_good_files(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    make_files(d, [1, 500, 1000])

    assert len(list(d.iterdir())) == 3


    with app.test_request_context('/scan', method='GET'):
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == '/scan'
        assert request.method == 'GET'
        fl = scan(d)
        assert len(fl) == 3
    assert type(fl) == list
    assert len(fl) == 3

    assert {'file1', 'file500', 'file1000'} == {os.path.basename(one_item['fileName'])
                                                for one_item in fl}


def test_non_existing_directory(tmp_path):
    with app.test_request_context('/scan', method='GET'):
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == '/scan'
        assert request.method == 'GET'
        fl = scan("foo")
        assert fl == "Directory 'foo' does not exist"


def test_add_files_for_rescan(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    make_files(d, [1, 500, 1000])
    assert len(list(d.iterdir())) == 3

    fl = scan(d)
    make_files(d, [4, 5])
    rs = rescan(d)
    expected = [{
        "fileName": "file4",
        "sha1": "caa6090a6bd4d02aad7af9b99cc563d64fd1a08d"
    }, {
        "fileName": "file5",
        "sha1": "9d291fb4ba82e098d6eff85dae0619d052535bb6"
    }]

    assert json.dumps(expected) == rs


def test_modify_sha1_for_rescan(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    make_files(d, [1, 500, 1000])
    assert len(list(d.iterdir())) == 3

    scan(d)
    with open(d / "file1", "a") as f:
        f.write("Append more content")
    rs = rescan(d)

    expected_json = [{
        "fileName": "file1",
        "sha1": "810f1d09cd2677f8227d5d68866bf5fe06b083ac"
    }]

    assert json.dumps(expected_json) == rs
