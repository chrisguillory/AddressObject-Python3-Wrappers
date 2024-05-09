from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


import mdAddr_pythoncode
import mdGeo_pythoncode
from mdAddr_pythoncode import AutoCompletionMode, mdAddr
from mdGeo_pythoncode import mdGeo

DQS_DIR = os.environ['LD_LIBRARY_PATH'].split(':')[0].split('/')[2]
GEOCOM_DIR = os.environ['LD_LIBRARY_PATH'].split(':')[1].split('/')[2]
print(f'{DQS_DIR=} {GEOCOM_DIR=}')


def get_dqs_data_path() -> Path:
    return Path(f'/melissa_data/{DQS_DIR}/address/data')


def get_geocom_data_path() -> Path:
    return Path(f'/melissa_data/{GEOCOM_DIR}/data')


def initialize_addr() -> mdAddr_pythoncode.mdAddr:
    data_path = get_dqs_data_path()

    addr = mdAddr_pythoncode.mdAddr()
    # noinspection SpellCheckingInspection
    addr.SetLicenseString("fOdOUG53XSwmliJvd6fcr6**OL8VV4KZEXJouP_Ou1Hjc1**EU49FEZ3mcsGCpjy0uSiX-**")
    addr.SetPathToUSFiles(data_path.as_posix())
    addr.SetPathToCanadaFiles((data_path / 'mdCanada').as_posix())

    addr.SetPathToDPVDataFiles((data_path / 'DPV').as_posix())
    addr.SetPathToLACSLinkDataFiles(
        (data_path / 'mdLACS').as_posix())  # Needed for GetAutoCompletion. TODO: documented?
    addr.SetPathToSuiteLinkDataFiles((data_path / 'mdSteLink').as_posix())

    addr.SetPathToRBDIFiles((data_path / 'RBDI').as_posix())

    addr.SetPathToAddrKeyDataFiles((data_path / 'mdAddrKey').as_posix())
    program_status: mdAddr_pythoncode.ProgramStatus = addr.InitializeDataFiles()
    if program_status != mdAddr_pythoncode.ProgramStatus.ErrorNone:
        raise RuntimeError(f"Melissa Data address initialize error: {addr.GetInitializeErrorString()}")

    addr.SetUseUSPSPreferredCityNames(True)

    return addr


def initialize_melissa_geo() -> Any:
    data_path = get_geocom_data_path()

    # Create Geocoder Object
    geo = mdGeo_pythoncode.mdGeo()

    geo.SetLicenseString("fOdOUG53XSwmliJvd6fcr6**OL8VV4KZEXJouP_Ou1Hjc1**EU49FEZ3mcsGCpjy0uSiX-**")
    geo.SetPathToGeoCodeDataFiles(data_path.as_posix())
    # Geo Points Add-on
    geo.SetPathToGeoPointDataFiles(data_path.as_posix())

    program_status: mdGeo_pythoncode.ProgramStatus = geo.InitializeDataFiles()
    if program_status != mdGeo_pythoncode.ProgramStatus.ErrorNone:
        raise RuntimeError(f"Melissa Data geo initialize error: {geo.GetInitializeErrorString()}")

    return geo


def initialize_street() -> mdAddr_pythoncode.mdStreet:
    data_path = get_dqs_data_path()

    street_data = mdAddr_pythoncode.mdStreet()
    street_data.SetLicenseString("fOdOUG53XSwmliJvd6fcr6**OL8VV4KZEXJouP_Ou1Hjc1**EU49FEZ3mcsGCpjy0uSiX-**")

    program_status = street_data.Initialize(
        get_dqs_data_path().as_posix(),
        get_dqs_data_path().as_posix(),
        get_dqs_data_path().as_posix()
    )
    if program_status != ProgramStatus.ErrorNone:
        raise RuntimeError(f"Melissa Data street data initialize error: {street_data.GetInitializeErrorString()}")

    return street_data


"""
3420-545-0632-000-2
3420-545-0632-000-2
"""


def query_mak_data(addr: mdAddr, geo: mdGeo, mak: str | None, json: dict[str, str]) -> dict[str, Any]:
    if 'unparsed_address' in json:
        assert 'address' not in json, "Cannot have both 'unparsed_address' and 'address' in the same request"
        assert 'last_line' not in json, "Cannot have both 'unparsed_address' and 'last_line' in the same request"
        address, last_line = json['unparsed_address'].split(',', maxsplit=1)
        json |= {
            "address": address,
            "last_line": last_line,
        }
        json.pop('unparsed_address')

    json_to_setter = (
        ("address", addr.SetAddress),
        ("city", addr.SetCity),
        ("last_line", addr.SetLastLine),
        ("plus4", addr.SetPlus4),
        ("state", addr.SetState),
        ("suite", addr.SetSuite),
        ("zip", addr.SetZip),
        ("country_code", addr.SetCountryCode),
    )
    extra_keys = set(json.keys()) - {name for name, _ in json_to_setter}
    assert not extra_keys, f"Unexpected keys in request: {extra_keys}"
    # noinspection DuplicatedCode
    addr.ClearProperties()
    for name, setter in json_to_setter:
        value = json.get(name)
        if value is not None:
            if not isinstance(value, str):
                raise RuntimeError(f"Request field {name} must be string")
            setter(value)
    addr.VerifyAddress()

    address_result = {
        "mak": addr.GetMelissaAddressKey(),
        "base_mak": addr.GetMelissaAddressKeyBase(),
        'address_key': addr.GetAddressKey(),
        "results": sorted(addr.GetResults().split(',')),
        "dpv_footnotes": addr.GetDPVFootnotes(),
        "ews_flag": addr.GetEWSFlag(),
        "lacs_status": addr.GetLACS(),
        "lacs_link_indicator": addr.GetLACSLinkIndicator(),
        "lacs_link_return_code": addr.GetLACSLinkReturnCode(),
        "rdbi": addr.GetRBDI(),
        "suite_link_return_code": addr.GetSuiteLinkReturnCode(),
        "address": addr.GetAddress(),
        "city": addr.GetCity(),
        "country_code": addr.GetCountryCode(),
        "plus4": addr.GetPlus4(),
        "state": addr.GetState(),
        "suite": addr.GetSuite(),
        "urbanization": addr.GetUrbanization(),
        "zip": addr.GetZip(),
        "parsed_address_range": addr.GetParsedAddressRange(),
        "parsed_garbage": addr.GetParsedGarbage(),
        "parsed_lockbox": addr.GetParsedLockBox(),
        "parsed_post_direction": addr.GetParsedPostDirection(),
        "parsed_pre_direction": addr.GetParsedPreDirection(),
        "parsed_private_mailbox_name": addr.GetParsedPrivateMailboxName(),
        "parsed_private_mailbox_number": addr.GetParsedPrivateMailboxNumber(),
        "parsed_route_service": addr.GetParsedRouteService(),
        "parsed_street_name": addr.GetParsedStreetName(),
        "parsed_suffix": addr.GetParsedSuffix(),
        "parsed_suite_name": addr.GetParsedSuiteName(),
        "parsed_suite_range": addr.GetParsedSuiteRange(),
        "address_type_code": addr.GetAddressTypeCode(),
        "address_type_string": addr.GetAddressTypeString(),
        "city_abbreviation": addr.GetCityAbbreviation(),
        "is_cmra": addr.GetCMRA(),
        "congressional_district": addr.GetCongressionalDistrict(),
        "county_fips": addr.GetCountyFips(),
        "county_name": addr.GetCountyName(),
        "private_mailbox": addr.GetPrivateMailbox(),
        "time_zone": addr.GetTimeZone(),
        "time_zone_code": addr.GetTimeZoneCode(),
        "zip_type": addr.GetZipType(),
        "carrier_route": addr.GetCarrierRoute(),
        "delivery_point_check_digit": addr.GetDeliveryPointCheckDigit(),
        "delivery_point_code": addr.GetDeliveryPointCode(),
        "elot_number": addr.GetELotNumber(),
        "elot_order": addr.GetELotOrder(),

    }

    if mak:
        print(f'Expected MAK {mak}, got {address_result["mak"]}')
        assert address_result["mak"] == mak, f"Expected MAK {mak}, got {address_result['mak']}"

    return {
        "address_result": address_result,
        "geocoder_result": query_geocoder_data(
            geo=geo,
            mak=address_result["mak"],
            address_key=address_result["address_key"]
        ),
    }


def query_geocoder_data(geo: mdGeo, mak: str, address_key: str) -> dict[str, Any]:
    geo.SetInputParameter("MAK", mak)
    geo.SetInputParameter("AddressKey", address_key)
    geo.FindGeo()

    geocoder_result = {
        "block_suffix": geo.GetOutputParameter("BlockSuffix"),
        "cbsa_code": geo.GetOutputParameter("CBSACode"),
        "cbsa_title": geo.GetOutputParameter("CBSATitle"),
        "cbsa_level": geo.GetOutputParameter("CBSALevel"),
        "cbsa_division_code": geo.GetOutputParameter("CBSADivisionCode"),
        "cbsa_division_title": geo.GetOutputParameter("CBSADivisionTitle"),
        "cbsa_division_level": geo.GetOutputParameter("CBSADivisionLevel"),
        "census_block": geo.GetOutputParameter("CensusBlock"),
        "census_key": geo.GetOutputParameter("CensusKey"),
        "census_key_decennial": geo.GetOutputParameter("CensusKeyDecennial"),
        "census_tract": geo.GetOutputParameter("CensusTract"),
        "county_fips": geo.GetOutputParameter("CountyFIPS"),
        "county_name": geo.GetOutputParameter("CountyName"),
        "county_subdivision_code": geo.GetOutputParameter("CountySubdivisionCode"),
        "county_subdivision_name": geo.GetOutputParameter("CountySubdivisionName"),
        "elementary_school_district_code": geo.GetOutputParameter(
            "ElementarySchoolDistrictCode"
        ),
        "elementary_school_district_name": geo.GetOutputParameter(
            "ElementarySchoolDistrictName"
        ),
        "latitude": geo.GetOutputParameter("Latitude"),
        "longitude": geo.GetOutputParameter("Longitude"),
        "lsad": geo.GetOutputParameter("LSAD"),
        "place_code": geo.GetOutputParameter("PlaceCode"),
        "place_name": geo.GetOutputParameter("PlaceName"),
        "results": geo.GetOutputParameter("Results"),
        "secondary_school_district_code": geo.GetOutputParameter(
            "SecondarySchoolDistrictCode"
        ),
        "secondary_school_district_name": geo.GetOutputParameter(
            "SecondarySchoolDistrictName"
        ),
        "state_district_lower": geo.GetOutputParameter("StateDistrictLower"),
        "state_district_upper": geo.GetOutputParameter("StateDistrictUpper"),
        "time_zone": geo.GetOutputParameter("TimeZone"),
        "time_zone_code": geo.GetOutputParameter("TimeZoneCode"),
        "unified_school_district_code": geo.GetOutputParameter("UnifiedSchoolDistrictCode"),
        "unified_school_district_name": geo.GetOutputParameter("UnifiedSchoolDistrictName"),
    }

    return geocoder_result


# noinspection SpellCheckingInspection
def main() -> None:
    addr = initialize_addr()
    geo = initialize_melissa_geo()
    parser = mdAddr_pythoncode.mdParse()

    print(
        json.dumps(
            query_mak_data(
                addr=addr,
                geo=geo,
                mak='',
                json={'address': '408A Laurel Ct # B', 'city': 'Laredo', 'state': 'TX', 'zip': '78041'}
            ),
            indent=2,
        )
    )
    return

    # street_data = initialize_street()
    # while True:
    #     result = street_data.GetAutoCompletion(
    #         'W223N4537', '53072', AutoCompletionMode.AutoCompleteSingleSuite, True)
    #     if not result:
    #         break
    #     print(f'{result=}')

    # result = parser.Parse('644 Bartram Court')
    # print(f'{result=}')
    # print(f'{parser.GetStreetName()=}')
    # print(f'{parser.GetSuffix()=}')
    #

    # addr.SetAddress('555 N Broad St Apt B607')
    # addr.SetLastLine('Doylestown, PA 18901')
    # result = addr.VerifyAddress()
    # print(f"VerifyAddress result: {result}")
    # print(f'{addr.GetMelissaAddressKey()=}')
    # print(f'{addr.GetAddressKey()=}')
    # print(f'{addr.GetAddress()} {addr.GetSuite()}'.strip())
    # print(f'{addr.GetCity()}, {addr.GetState()} {addr.GetZip()}')
    # print(f'{addr.GetResults()=}')
    #
    # print()

    unpased_address = "13701 Ronald Reagan Bld #62, Cedar Park, TX 78613"
    address, last_line = unpased_address.split(',', 1)
    addr.ClearProperties()
    # addr.SetAddress(address.strip())
    # addr.SetLastLine(last_line.strip())
    addr.SetAddress('17854 Rapids Rd')
    addr.SetLastLine('Hiram, OH')
    result = addr.VerifyAddress()
    print(f"VerifyAddress result: {result}")
    print(f'{addr.GetMelissaAddressKey()=}')
    print(f'{addr.GetMelissaAddressKeyBase()=}')
    print(f'{addr.GetAddressKey()=}')
    print(f'{addr.GetAddress()} {addr.GetSuite()}'.strip())
    print(f'{addr.GetCity()}, {addr.GetState()} {addr.GetZip()}')
    print(f'{addr.GetParsedGarbage()=}')
    # County and FIPS code
    print(f'{addr.GetCountyName()=}')
    print(f'{addr.GetCountyFips()=}')
    print(f'{addr.Su()=}')
    print(f'{addr.GetResults()=}')

    # Keep the suite
    # suite = '62'  # We might have to figure out how to parse the suite
    #
    # print(f'{addr.FindSuggestion()=}')
    # print(f'{addr.GetMelissaAddressKey()=}')
    # print(f'{addr.GetMelissaAddressKeyBase()=}')
    # print(f'{addr.GetAddressKey()=}')
    # print(f'{addr.GetAddress()} {addr.GetSuite()}'.strip())
    # print(f'{addr.GetCity()}, {addr.GetState()} {addr.GetZip()}')
    # print(f'{addr.GetParsedGarbage()=}')
    # print(f'{addr.GetResults()=}')
    #
    # # Restore the suite
    # addr.SetSuite(suite)
    # addr.VerifyAddress()
    # print(f'{addr.GetMelissaAddressKey()=}')
    # print(f'{addr.GetMelissaAddressKeyBase()=}')
    # print(f'{addr.GetAddressKey()=}')
    # print(f'{addr.GetAddress()} {addr.GetSuite()}'.strip())
    # print(f'{addr.GetCity()}, {addr.GetState()} {addr.GetZip()}')


if __name__ == '__main__':
    """
    % ./run_docker.sh
    % LD_LIBRARY_PATH=/melissa_data/dqs.202404/address/linux/gcc48_64bit python -m main
    """
    main()
