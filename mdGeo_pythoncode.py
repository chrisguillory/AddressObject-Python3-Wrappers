from ctypes import *
from enum import Enum
import ctypes
import os
import sys

if (os.name == 'nt' and sys.version_info[:2] >= (3,8)):
    lib = ctypes.CDLL('mdGeo.dll', winmode=0)
elif (os.name == 'nt'):
    lib = ctypes.CDLL('mdGeo.dll')
else:
    lib = ctypes.CDLL('libmdGeo.so')

lib.mdGeoCreate.argtypes = []
lib.mdGeoCreate.restype = c_void_p
lib.mdGeoDestroy.argtypes = [c_void_p]
lib.mdGeoDestroy.restype = None
lib.mdGeoSetPathToGeoCodeDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdGeoSetPathToGeoCodeDataFiles.restype = None
lib.mdGeoSetPathToGeoPointDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdGeoSetPathToGeoPointDataFiles.restype = None
lib.mdGeoSetPathToGeoCanadaDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdGeoSetPathToGeoCanadaDataFiles.restype = None
lib.mdGeoSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdGeoSetLicenseString.restype = c_bool
lib.mdGeoInitialize.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdGeoInitialize.restype = c_int
lib.mdGeoInitializeDataFiles.argtypes = [c_void_p]
lib.mdGeoInitializeDataFiles.restype = c_int
lib.mdGeoGetInitializeErrorString.argtypes = [c_void_p]
lib.mdGeoGetInitializeErrorString.restype = c_char_p
lib.mdGeoGetBuildNumber.argtypes = [c_void_p]
lib.mdGeoGetBuildNumber.restype = c_char_p
lib.mdGeoGetDatabaseDate.argtypes = [c_void_p]
lib.mdGeoGetDatabaseDate.restype = c_char_p
lib.mdGeoGetExpirationDate.argtypes = [c_void_p]
lib.mdGeoGetExpirationDate.restype = c_char_p
lib.mdGeoGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdGeoGetLicenseExpirationDate.restype = c_char_p
lib.mdGeoSetLatitude.argtypes = [c_void_p, c_char_p]
lib.mdGeoSetLatitude.restype = None
lib.mdGeoSetLongitude.argtypes = [c_void_p, c_char_p]
lib.mdGeoSetLongitude.restype = None
lib.mdGeoWriteToLogFile.argtypes = [c_void_p, c_char_p]
lib.mdGeoWriteToLogFile.restype = c_bool
lib.mdGeoGeoCode.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdGeoGeoCode.restype = c_int
lib.mdGeoGeoPoint.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdGeoGeoPoint.restype = c_int
lib.mdGeoComputeDistance.argtypes = [c_void_p, c_double, c_double, c_double, c_double]
lib.mdGeoComputeDistance.restype = c_double
lib.mdGeoComputeBearing.argtypes = [c_void_p, c_double, c_double, c_double, c_double]
lib.mdGeoComputeBearing.restype = c_double
lib.mdGeoGetErrorCode.argtypes = [c_void_p]
lib.mdGeoGetErrorCode.restype = c_char_p
lib.mdGeoGetStatusCode.argtypes = [c_void_p]
lib.mdGeoGetStatusCode.restype = c_char_p
lib.mdGeoGetResults.argtypes = [c_void_p]
lib.mdGeoGetResults.restype = c_char_p
lib.mdGeoGetResultCodeDescription.argtypes = [c_void_p, c_char_p, c_int]
lib.mdGeoGetResultCodeDescription.restype = c_char_p
lib.mdGeoGetLatitude.argtypes = [c_void_p]
lib.mdGeoGetLatitude.restype = c_char_p
lib.mdGeoGetLongitude.argtypes = [c_void_p]
lib.mdGeoGetLongitude.restype = c_char_p
lib.mdGeoGetCensusTract.argtypes = [c_void_p]
lib.mdGeoGetCensusTract.restype = c_char_p
lib.mdGeoGetCensusBlock.argtypes = [c_void_p]
lib.mdGeoGetCensusBlock.restype = c_char_p
lib.mdGeoGetCountyFips.argtypes = [c_void_p]
lib.mdGeoGetCountyFips.restype = c_char_p
lib.mdGeoGetCountyName.argtypes = [c_void_p]
lib.mdGeoGetCountyName.restype = c_char_p
lib.mdGeoGetPlaceCode.argtypes = [c_void_p]
lib.mdGeoGetPlaceCode.restype = c_char_p
lib.mdGeoGetPlaceName.argtypes = [c_void_p]
lib.mdGeoGetPlaceName.restype = c_char_p
lib.mdGeoGetTimeZoneCode.argtypes = [c_void_p]
lib.mdGeoGetTimeZoneCode.restype = c_char_p
lib.mdGeoGetTimeZone.argtypes = [c_void_p]
lib.mdGeoGetTimeZone.restype = c_char_p
lib.mdGeoGetCBSACode.argtypes = [c_void_p]
lib.mdGeoGetCBSACode.restype = c_char_p
lib.mdGeoGetCBSATitle.argtypes = [c_void_p]
lib.mdGeoGetCBSATitle.restype = c_char_p
lib.mdGeoGetCBSALevel.argtypes = [c_void_p]
lib.mdGeoGetCBSALevel.restype = c_char_p
lib.mdGeoGetCBSADivisionCode.argtypes = [c_void_p]
lib.mdGeoGetCBSADivisionCode.restype = c_char_p
lib.mdGeoGetCBSADivisionTitle.argtypes = [c_void_p]
lib.mdGeoGetCBSADivisionTitle.restype = c_char_p
lib.mdGeoGetCBSADivisionLevel.argtypes = [c_void_p]
lib.mdGeoGetCBSADivisionLevel.restype = c_char_p
lib.mdGeoGetLastUsageLogMessage.argtypes = [c_void_p]
lib.mdGeoGetLastUsageLogMessage.restype = c_char_p
lib.mdGeoGetCensusKey.argtypes = [c_void_p]
lib.mdGeoGetCensusKey.restype = c_char_p
lib.mdGeoGetCountySubdivisionCode.argtypes = [c_void_p]
lib.mdGeoGetCountySubdivisionCode.restype = c_char_p
lib.mdGeoGetCountySubdivisionName.argtypes = [c_void_p]
lib.mdGeoGetCountySubdivisionName.restype = c_char_p
lib.mdGeoGetElementarySchoolDistrictCode.argtypes = [c_void_p]
lib.mdGeoGetElementarySchoolDistrictCode.restype = c_char_p
lib.mdGeoGetElementarySchoolDistrictName.argtypes = [c_void_p]
lib.mdGeoGetElementarySchoolDistrictName.restype = c_char_p
lib.mdGeoGetSecondarySchoolDistrictCode.argtypes = [c_void_p]
lib.mdGeoGetSecondarySchoolDistrictCode.restype = c_char_p
lib.mdGeoGetSecondarySchoolDistrictName.argtypes = [c_void_p]
lib.mdGeoGetSecondarySchoolDistrictName.restype = c_char_p
lib.mdGeoGetStateDistrictLower.argtypes = [c_void_p]
lib.mdGeoGetStateDistrictLower.restype = c_char_p
lib.mdGeoGetStateDistrictUpper.argtypes = [c_void_p]
lib.mdGeoGetStateDistrictUpper.restype = c_char_p
lib.mdGeoGetUnifiedSchoolDistrictCode.argtypes = [c_void_p]
lib.mdGeoGetUnifiedSchoolDistrictCode.restype = c_char_p
lib.mdGeoGetUnifiedSchoolDistrictName.argtypes = [c_void_p]
lib.mdGeoGetUnifiedSchoolDistrictName.restype = c_char_p
lib.mdGeoGetBlockSuffix.argtypes = [c_void_p]
lib.mdGeoGetBlockSuffix.restype = c_char_p
lib.mdGeoSetInputParameter.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdGeoSetInputParameter.restype = c_bool
lib.mdGeoFindGeo.argtypes = [c_void_p]
lib.mdGeoFindGeo.restype = None
lib.mdGeoGetOutputParameter.argtypes = [c_void_p, c_char_p]
lib.mdGeoGetOutputParameter.restype = c_char_p

# mdGeo Enumerations
class ProgramStatus(Enum):
    ErrorNone = 0
    ErrorOther = 1
    ErrorOutOfMemory = 2
    ErrorRequiredFileNotFound = 3
    ErrorFoundOldFile = 4
    ErrorDatabaseExpired = 5
    ErrorLicenseExpired = 6

class AccessType(Enum):
    Local = 0
    Remote = 1

class DiacriticsMode(Enum):
    Auto = 0
    On = 1
    Off = 2

class StandardizeMode(Enum):
    ShortFormat = 0
    LongFormat = 1
    AutoFormat = 2

class SuiteParseMode(Enum):
    ParseSuite = 0
    CombineSuite = 1

class AliasPreserveMode(Enum):
    ConvertAlias = 0
    PreserveAlias = 1

class AutoCompletionMode(Enum):
    AutoCompleteSingleSuite = 0
    AutoCompleteRangedSuite = 1
    AutoCompletePlaceHolderSuite = 2
    AutoCompleteNoSuite = 3

class ResultCdDescOpt(Enum):
    ResultCodeDescriptionLong = 0
    ResultCodeDescriptionShort = 1

class MailboxLookupMode(Enum):
    MailboxNone = 0
    MailboxExpress = 1
    MailboxPremium = 2

class mdGeo(object):
    def __init__(self):
        self.I = lib.mdGeoCreate()

    def __del__(self):
        lib.mdGeoDestroy(self.I)

    def SetPathToGeoCodeDataFiles(self, p1):
        lib.mdGeoSetPathToGeoCodeDataFiles(self.I, p1.encode('utf-8'))

    def SetPathToGeoPointDataFiles(self, p1):
        lib.mdGeoSetPathToGeoPointDataFiles(self.I, p1.encode('utf-8'))

    def SetPathToGeoCanadaDataFiles(self, p1):
        lib.mdGeoSetPathToGeoCanadaDataFiles(self.I, p1.encode('utf-8'))

    def SetLicenseString(self, License):
        return lib.mdGeoSetLicenseString(self.I, License.encode('utf-8'))

    def Initialize(self, DataPath, IndexPath):
        return ProgramStatus(lib.mdGeoInitialize(self.I, DataPath.encode('utf-8'), IndexPath.encode('utf-8')))

    def InitializeDataFiles(self):
        return ProgramStatus(lib.mdGeoInitializeDataFiles(self.I))

    def GetInitializeErrorString(self):
        return lib.mdGeoGetInitializeErrorString(self.I).decode('utf-8')

    def GetBuildNumber(self):
        return lib.mdGeoGetBuildNumber(self.I).decode('utf-8')

    def GetDatabaseDate(self):
        return lib.mdGeoGetDatabaseDate(self.I).decode('utf-8')

    def GetExpirationDate(self):
        return lib.mdGeoGetExpirationDate(self.I).decode('utf-8')

    def GetLicenseExpirationDate(self):
        return lib.mdGeoGetLicenseExpirationDate(self.I).decode('utf-8')

    def SetLatitude(self, latitude):
        lib.mdGeoSetLatitude(self.I, latitude.encode('utf-8'))

    def SetLongitude(self, longitude):
        lib.mdGeoSetLongitude(self.I, longitude.encode('utf-8'))

    def WriteToLogFile(self, logFile):
        return lib.mdGeoWriteToLogFile(self.I, logFile.encode('utf-8'))

    def GeoCode(self, Zip, Plus4=""):
        return lib.mdGeoGeoCode(self.I, Zip.encode('utf-8'), Plus4.encode('utf-8'))

    def GeoPoint(self, Zip, Plus4, DeliveryPointCode):
        return lib.mdGeoGeoPoint(self.I, Zip.encode('utf-8'), Plus4.encode('utf-8'), DeliveryPointCode.encode('utf-8'))

    def ComputeDistance(self, Latitude1, Longitude1, Latitude2, Longitude2):
        return lib.mdGeoComputeDistance(self.I)

    def ComputeBearing(self, Latitude1, Longitude1, Latitude2, Longitude2):
        return lib.mdGeoComputeBearing(self.I)

    def GetErrorCode(self):
        return lib.mdGeoGetErrorCode(self.I).decode('utf-8')

    def GetStatusCode(self):
        return lib.mdGeoGetStatusCode(self.I).decode('utf-8')

    def GetResults(self):
        return lib.mdGeoGetResults(self.I).decode('utf-8')

    def GetResultCodeDescription(self, resultCode, opt=0):
        return lib.mdGeoGetResultCodeDescription(self.I, resultCode.encode('utf-8'), ResultCdDescOpt(opt).value).decode('utf-8')

    def GetLatitude(self):
        return lib.mdGeoGetLatitude(self.I).decode('utf-8')

    def GetLongitude(self):
        return lib.mdGeoGetLongitude(self.I).decode('utf-8')

    def GetCensusTract(self):
        return lib.mdGeoGetCensusTract(self.I).decode('utf-8')

    def GetCensusBlock(self):
        return lib.mdGeoGetCensusBlock(self.I).decode('utf-8')

    def GetCountyFips(self):
        return lib.mdGeoGetCountyFips(self.I).decode('utf-8')

    def GetCountyName(self):
        return lib.mdGeoGetCountyName(self.I).decode('utf-8')

    def GetPlaceCode(self):
        return lib.mdGeoGetPlaceCode(self.I).decode('utf-8')

    def GetPlaceName(self):
        return lib.mdGeoGetPlaceName(self.I).decode('utf-8')

    def GetTimeZoneCode(self):
        return lib.mdGeoGetTimeZoneCode(self.I).decode('utf-8')

    def GetTimeZone(self):
        return lib.mdGeoGetTimeZone(self.I).decode('utf-8')

    def GetCBSACode(self):
        return lib.mdGeoGetCBSACode(self.I).decode('utf-8')

    def GetCBSATitle(self):
        return lib.mdGeoGetCBSATitle(self.I).decode('utf-8')

    def GetCBSALevel(self):
        return lib.mdGeoGetCBSALevel(self.I).decode('utf-8')

    def GetCBSADivisionCode(self):
        return lib.mdGeoGetCBSADivisionCode(self.I).decode('utf-8')

    def GetCBSADivisionTitle(self):
        return lib.mdGeoGetCBSADivisionTitle(self.I).decode('utf-8')

    def GetCBSADivisionLevel(self):
        return lib.mdGeoGetCBSADivisionLevel(self.I).decode('utf-8')

    def GetLastUsageLogMessage(self):
        return lib.mdGeoGetLastUsageLogMessage(self.I).decode('utf-8')

    def GetCensusKey(self):
        return lib.mdGeoGetCensusKey(self.I).decode('utf-8')

    def GetCountySubdivisionCode(self):
        return lib.mdGeoGetCountySubdivisionCode(self.I).decode('utf-8')

    def GetCountySubdivisionName(self):
        return lib.mdGeoGetCountySubdivisionName(self.I).decode('utf-8')

    def GetElementarySchoolDistrictCode(self):
        return lib.mdGeoGetElementarySchoolDistrictCode(self.I).decode('utf-8')

    def GetElementarySchoolDistrictName(self):
        return lib.mdGeoGetElementarySchoolDistrictName(self.I).decode('utf-8')

    def GetSecondarySchoolDistrictCode(self):
        return lib.mdGeoGetSecondarySchoolDistrictCode(self.I).decode('utf-8')

    def GetSecondarySchoolDistrictName(self):
        return lib.mdGeoGetSecondarySchoolDistrictName(self.I).decode('utf-8')

    def GetStateDistrictLower(self):
        return lib.mdGeoGetStateDistrictLower(self.I).decode('utf-8')

    def GetStateDistrictUpper(self):
        return lib.mdGeoGetStateDistrictUpper(self.I).decode('utf-8')

    def GetUnifiedSchoolDistrictCode(self):
        return lib.mdGeoGetUnifiedSchoolDistrictCode(self.I).decode('utf-8')

    def GetUnifiedSchoolDistrictName(self):
        return lib.mdGeoGetUnifiedSchoolDistrictName(self.I).decode('utf-8')

    def GetBlockSuffix(self):
        return lib.mdGeoGetBlockSuffix(self.I).decode('utf-8')

    def SetInputParameter(self, key, val):
        return lib.mdGeoSetInputParameter(self.I, key.encode('utf-8'), val.encode('utf-8'))

    def FindGeo(self):
        lib.mdGeoFindGeo(self.I)

    def GetOutputParameter(self, key):
        return lib.mdGeoGetOutputParameter(self.I, key.encode('utf-8')).decode('utf-8')