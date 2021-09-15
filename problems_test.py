from problems import convert_json, separate_sonnets, two_columns_to_one
import shutil
import json
import os


def test_convert_json():
    if os.path.isfile("sample_text\\string_lengths_map.json"):
        os.remove("sample_text\\string_lengths_map.json")

    convert_json()

    with open("sample_text\\string_lengths_map.json", "r") as f:
        provided = json.load(f)
    with open("testing_text\\string_lengths.json", "r") as f:
        expected = json.load(f)

    if os.path.isfile("sample_text\\string_lengths_map.json"):
        os.remove("sample_text\\string_lengths_map.json")  # cleaning up after ourselves

    assert provided == expected


def test_separate_sonnets():
    if os.path.isdir("sonnets"):
        shutil.rmtree("sonnets")  # removing any preexisting files
    separate_sonnets()

    for file_path in os.listdir("testing_text\\sonnets"):
        with open(f"sonnets\\{file_path}", "r") as provided, open(f"testing_text\\sonnets\\{file_path}") as expected:
            assert provided.read() == expected.read()

    if os.path.isdir("sonnets"):
        shutil.rmtree("sonnets")  # cleaning up


def test_two_to_one_columns():
    if os.path.isfile("sample_text\\iso_8859-1_two_columns.txt"):
        os.remove("sample_text\\iso_8859-1_two_columns.txt")

    two_columns_to_one()

    with open("sample_text\\iso_8859-1_two_columns.txt", "r") as provided, \
            open("testing_text\\iso_8859-1_two_columns.txt") as expected:
        for provided_line, expected_line in zip(provided, expected):
            assert provided_line.strip() == expected_line.strip()

    if os.path.isfile("sample_text\\iso_8859-1_two_columns.txt"):
        os.remove("sample_text\\iso_8859-1_two_columns.txt")
