import json
import requests
from assertpy import assert_that
from jsonschema import validate as validate_json_schema
import pytest
from setting.endpoint import API_PROVICE, API_CITY
from setting.general import api_key, max_latency
from jsonschemas.schema_city import *


def test():
    head = {
        "key": api_key
    }
    req = requests.get(API_CITY, headers=head)
    # VERIKASI
    status_code = req.status_code
    latency = req.elapsed.microseconds
    description = req.json().get("rajaongkir")["status"]["description"]
    results = req.json().get("rajaongkir")["results"]

    # ASSERT
    assert_that(status_code).is_equal_to(200)
    assert_that(latency).is_less_than(max_latency)
    assert_that(description).is_equal_to("OK")
    assert_that(results).is_type_of(list)
    assert_that(results).is_not_none()
    validate_json_schema(instance=req.json(), schema=schema_list_city_normal)
