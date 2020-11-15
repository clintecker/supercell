# Third Party Code
from clint_utilities import assert_raises, RequestError
import responses

# Supercell Code
from supercell.breezometer.utils import (
    build_headers,
    build_query_string,
    build_uri,
    make_api_request,
)


def test_build_query_string():
    assert (
        "agency=EPA&features=one,two,three&hours=144&key=aaAAbbBBccCC&lat=-109.109109&lon=39.3939&metadata=true"
        == build_query_string(
            metadata=True,
            features=["one", "two", "three"],
            api_key="aaAAbbBBccCC",
            longitude=39.3939,
            latitude=-109.109109,
            hours=144,
            agency="EPA",
        )
    )

    assert (
        "agency=EPA&features=one,two,three&hours=144&key=aaAAbbBBccCC&lat=-109.109109&lon=39.3939&metadata=false"
        == build_query_string(
            metadata=False,
            features=["one", "two", "three"],
            api_key="aaAAbbBBccCC",
            longitude=39.3939,
            latitude=-109.109109,
            hours=144,
            agency="EPA",
        )
    )


def test_build_headers():
    assert {
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://breezometer.com/air-quality-map/search?lat=39.3939&lon=-109.109109",
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    } == build_headers(latitude=39.3939, longitude=-109.109109)


def test_build_uri():
    assert (
        "https://api.breezometer.com/v5/examples/10232?"
        "agency=BM&features=one,two,three&hours=144&"
        "key=aaAAbbBBccCC&lat=-109.109109&lon=39.3939&metadata=true"
    ) == build_uri(
        path="/v5/examples/10232",
        metadata=True,
        features=["one", "two", "three"],
        api_key="aaAAbbBBccCC",
        longitude=39.3939,
        latitude=-109.109109,
        hours=144,
        agency="BM",
    )


@responses.activate
def test_make_api_request_successful():
    responses.add(
        responses.GET,
        "https://api.breezometer.com/v5/examples/10232",
        json={"data": {}, "errors": None},
        status=200,
    )
    assert {"data": {}, "errors": None} == make_api_request(
        path="/v5/examples/10232",
        latitude=39.3939,
        longitude=-109.109109,
        features=["one", "two", "three"],
        api_key="aaAAbbBBccCC",
        metadata=True,
    )
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == (
        "https://api.breezometer.com/v5/examples/10232?"
        "features=one,two,three&key=aaAAbbBBccCC&lat=39.3939&lon=-109.109109&metadata=true"
    )


@responses.activate
def test_make_api_request_server_error():
    responses.add(
        responses.GET,
        "https://api.breezometer.com/v5/examples/10232",
        json=None,
        status=500,
    )
    assert_raises(
        fn=make_api_request,
        args=(),
        kwargs=dict(
            path="/v5/examples/10232",
            latitude=39.3939,
            longitude=-109.109109,
            features=["one", "two", "three"],
            api_key="aaAAbbBBccCC",
            metadata=True,
            num_attempts=3,
            delay=0,
        ),
        exc=RequestError,
    )
    assert len(responses.calls) == 3
    assert (
        responses.calls[2].request.url
        == responses.calls[1].request.url
        == responses.calls[0].request.url
        == (
            "https://api.breezometer.com/v5/examples/10232?"
            "features=one,two,three&key=aaAAbbBBccCC&lat=39.3939&lon=-109.109109&metadata=true"
        )
    )
