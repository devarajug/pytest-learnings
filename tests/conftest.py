import pytest
import sys

def pytest_addoption(parser):
    parser.addoption(
        "--tag",
        action="store",
        metavar="name",
        help="only run tests matching the tag name.",
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "tag: Tag for the individual tests")

def pytest_collection_modifyitems(config, items):    
    tag = config.getvalue("tag")
    for item in items:
        for mark in item.iter_markers(name="tag"):
            if tag in mark.args:
                items.remove(item)
