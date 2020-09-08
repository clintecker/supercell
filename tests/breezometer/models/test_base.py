# Standard Library
import datetime

# Third Party Code
from dateutil.tz import tzutc

# Supercell Code
from supercell.breezometer.models.base import BreezoMeterBaseModel, BreezoMeterModel


def test_air_quality_base_model():
    class Other(BreezoMeterBaseModel):
        pass

    assert "BreezoMeterBaseModel" == str(BreezoMeterBaseModel())
    assert "Other" == str(Other())

    assert "BreezoMeterBaseModel" == BreezoMeterBaseModel().to_str()
    assert "Other" == Other().to_str()

    assert "BreezoMeterBaseModel" == BreezoMeterBaseModel().as_string
    assert "Other" == Other().as_string

    assert "BreezoMeterBaseModel" == repr(BreezoMeterBaseModel())
    assert "Other" == repr(Other())


def test_air_quality_model():
    o = BreezoMeterModel(
        timestamp=datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc())
    )
    assert datetime.datetime(2020, 1, 1, 1, 1, 1, tzinfo=tzutc()) == o.timestamp
