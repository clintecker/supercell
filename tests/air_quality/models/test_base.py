# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.air_quality.models.base import AirQualityBaseModel, AirQualityModel


def test_air_quality_base_model():
    class Other(AirQualityBaseModel):
        pass

    assert "AirQualityBaseModel" == str(AirQualityBaseModel())
    assert "Other" == str(Other())

    assert "AirQualityBaseModel" == AirQualityBaseModel().to_str()
    assert "Other" == Other().to_str()

    assert "AirQualityBaseModel" == AirQualityBaseModel().as_string
    assert "Other" == Other().as_string

    assert "AirQualityBaseModel" == repr(AirQualityBaseModel())
    assert "Other" == repr(Other())


def test_air_quality_model():
    o = AirQualityModel(
        timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc())
    )
    assert datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()) == o.timestamp
