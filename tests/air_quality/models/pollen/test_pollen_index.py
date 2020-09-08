# Supercell Code
from supercell.air_quality.models.pollen.pollen_index import PollenIndex


def test_model():
    assert '{"value": 42, "category": "High Risk", "color": "#FF0000"}' == str(
        PollenIndex(value=42, category="High Risk", color="#FF0000",)
    )


def test_initialize_with_dictionary():
    assert '{"value": 42, "category": "High Risk", "color": "#FF0000"}' == str(
        PollenIndex.initialize_from_dictionary(
            response_dictionary={
                "value": 42,
                "category": "High Risk",
                "color": "#FF0000",
            }
        )
    )
