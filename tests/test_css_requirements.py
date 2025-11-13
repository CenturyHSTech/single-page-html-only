"""
Test CSS Requirements.
"""
from bs4 import BeautifulSoup
import pytest
import file_clerk.clerk as clerk
from webcode_tk import css_tools as css
from webcode_tk import html_tools as html
from webcode_tk import contrast_tools as contrast

project_path = "project/"
html_files = html.get_all_html_files(project_path)
styles_by_html_files = css.get_styles_by_html_files(project_path)

color_contrast_results = contrast.generate_contrast_report(project_path)
no_style_attribute_tests = []

def set_style_attribute_tests(path):
    results = []
    for file in html_files:
        filename = clerk.get_file_name(file)
        html = clerk.file_to_string(file)
        soup = BeautifulSoup(html, "html.parser")
        tags_with_style = soup.find_all(lambda tag: tag.has_attr('style'))
        number = len(tags_with_style)
        result = ""
        expected = f"pass: in {filename}, there are no tags with a style attribute."
        if number > 0:
            result = f"fail: in {filename}, there are {number} tags with a style attribute applied."
        else:
            result = expected
        results.append((result, expected))
    return results


def get_unique_font_families(project_folder):
    font_rules = css.get_unique_font_rules(project_folder)
    font_families_tests = []
    for file in font_rules:
        # apply the file, unique rules, unique selectors, and unique values
        filename = file.get("file")
        unique_rules = file.get("rules")
        passes_rules = len(unique_rules) >= 2
        passes_selectors = passes_rules
        unique_values = []
        for rule in unique_rules:
            value = rule.get("family")
            if value not in unique_values:
                unique_values.append(value)
        passes_values = len(unique_values) == 2
        font_families_tests.append((filename, passes_rules, passes_selectors,
                                    passes_values))
    return font_families_tests


def get_font_rules_data(font_tests):
    rules_data = []
    for test in font_tests:
        rules_data.append(test[:2])
    return rules_data


def get_font_selector_data(font_tests):
    rules_data = []
    for test in font_tests:
        rules_data.append((test[0], test[2]))
    return rules_data


def get_font_family_data(font_tests):
    rules_data = []
    for test in font_tests:
        rules_data.append((test[0], test[3]))
    return rules_data


def get_required_properties(required_properties, has_required_properties,
                            dec_block):
    for declaration in dec_block.declarations:
        prop = declaration.property
        if prop in required_properties:
            has_required_properties[prop] = True
        elif "background" in prop:
            # using shorthand?
            split_values = declaration.value.split()
            for value in split_values:
                if css.color_tools.is_hex(value):
                    has_required_properties["background-color"] = True


def applies_css(styles_by_html_files: list) -> list:
    results = []
    for item in styles_by_html_files:
        path = item.get("file")
        filename = clerk.get_file_name(path)
        expected = f"pass: {filename} applies CSS."
        sheets = item.get("stylesheets")
        applies_styles = False
        if sheets:
            for sheet in sheets:
                if sheet.text:
                    applies_styles = True
        if applies_styles:
            result = expected
        else:
            result = f"fail: {filename} does not apply CSS"
        results.append((result, expected))
    return results

font_families_tests = get_unique_font_families(project_path)
font_rules_results = get_font_rules_data(font_families_tests)
font_selector_results = get_font_selector_data(font_families_tests)
font_family_results = get_font_family_data(font_families_tests)
style_attributes_data = set_style_attribute_tests(html_files)
stylesheets = css.get_all_project_stylesheets(project_path)

applies_styles = applies_css(styles_by_html_files)

try:
    link_colors = css.get_link_color_data(project_path)
except TypeError:
    link_colors = []
    

@pytest.fixture
def project_folder():
    return project_path


@pytest.fixture
def html_styles():
    return styles_by_html_files


@pytest.fixture
def html_docs():
    return html_files


@pytest.fixture
def link_color_details():
    return link_colors


@pytest.mark.parametrize("result,expected", applies_styles)
def test_for_any_css_tag_or_stylesheet(result, expected):
    assert result == expected


@pytest.mark.parametrize("result,expected", style_attributes_data)
def test_files_for_style_attribute_data(result, expected):
    assert result == expected


@pytest.mark.parametrize("result", color_contrast_results)
def test_files_for__color_contrast(result):
    assert "pass:" in result[:5]


@pytest.mark.parametrize("file,passes_font_families", font_selector_results)
def test_files_for_2_font_families_max(file, passes_font_families):
    assert passes_font_families


def test_link_color_details_for_links_targeted(link_color_details):
    assert link_color_details
