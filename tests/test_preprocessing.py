import pandas as pd
import pytest

from src.bayan.preprocessing.core import mask_pii, normalize, preprocess


@pytest.mark.parametrize("raw,expected", [
    ("مـشكلة", "مشكلة"),
    ("هلووو", "هلوو"),
    ("ممتااااز", "ممتااز"),
    ("  نص   فيه   مسافات  ", "نص فيه مسافات"),
    ("hello    world", "hello world"),
    ("الخدمة 😡", "الخدمة 😡"),
    ("GOOD!!!", "GOOD!!"),
    ("تممم", "تمم"),
])
def test_normalize_contract(raw, expected):
    assert normalize(raw) == expected


@pytest.mark.parametrize("raw,expected", [
    ("اتصل 0551234567", "اتصل <PHONE>"),
    ("Call +966551234567", "Call <PHONE>"),
    ("رقم الهوية 1023456789", "رقم الهوية <NATIONAL_ID>"),
    ("ID 2123456789", "ID <NATIONAL_ID>"),
    ("لا توجد بيانات شخصية", "لا توجد بيانات شخصية"),
])
def test_mask_pii_examples(raw, expected):
    assert mask_pii(raw) == expected


def test_preprocess_masks_before_normalising():
    assert preprocess("  0551234567   😡  ") == "<PHONE> 😡"


def test_pii_fixture_recall():
    df = pd.read_csv("data/eval/pii_test_set.csv")
    actual = [mask_pii(x) for x in df["text"]]
    assert actual == df["expected_masked"].tolist()
