"""
For the Win students should pass the tests for this file.
"""
import pytest
import file_clerk.clerk as clerk
from webcode_tk import html_tools as html

project_dir = "project/"

min_required_elements = [
    ("p", 10),
    ("ul or ol or dl", 3),
    ("li", 10),]

has_dl = [
    ("dl", 1),
    ("dt", 4),
    ("dd", 4),
]


def get_dl_data(dl_test_data: list) -> list:
    has_definition_list = False
    dl_data = []
    only_dl = html.get_num_elements_in_folder(
        "dl", project_dir
    )
    has_definition_list = bool(only_dl)
    if has_definition_list:
        dts = html.get_num_elements_in_folder("dt", project_dir)
        dds = html.get_num_elements_in_folder("dd", project_dir)
        # Process output list
        multiplier = only_dl
        for item in has_dl:
            element, min = item
            min *= multiplier
            match element:
                case "dl":
                    expected = "pass: project has enough DLs."
                    if only_dl >= min:
                        result = expected
                    else:
                        msg = f"fail: project needs at least one "
                        msg += "definition list."
                case "dt":
                    expected = "pass: project has enough DT elements."
                    if dts >= min:
                        msg = expected
                    else:
                        needed = min - dts
                        msg = f"fail: project needs {needed} more DT "
                        msg += "element/s."
                    dl_data.append((msg, expected))
                case "dd":
                    expected = "pass: project has enough DD elements."
                    if dds >= min:
                        msg = expected
                    else:
                        needed = min - dds
                        msg = f"fail: project needs {needed} more DD "
                        msg += "element/s."
                    dl_data.append((msg, expected))
    else:
        result = "fail: there are no definition lists."
        expected = "pass: you have enough definition lists."
        dl_data.append((result, expected))
    return dl_data


min_number_of_elements = html.get_number_of_elements_per_file(
    project_dir, min_required_elements
)

definition_list_test = get_dl_data(has_dl)


@pytest.fixture
def html_files():
    html_files = html.get_all_html_files(project_dir)
    return html_files


@pytest.mark.parametrize("file,element,num", min_number_of_elements)
def test_for_html_exceeds_number_of_elements(file, element, num):
    if not html_files:
        assert False
    if "or" in element.lower():
        elements = element.split()
        actual = 0
        for el in elements:
            el = el.strip()
            actual += html.get_num_elements_in_file(el, file)
    else:
        actual = html.get_num_elements_in_file(element, file)
    assert actual >= num


@pytest.mark.parametrize("result,expected", definition_list_test)
def test_for_definition_lists(result, expected):
    assert result == expected
