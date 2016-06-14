from mmtf.api import MMTFDecoder,parse,parse_gzip,fetch
COORD_DIVIDER = 1000.0
OCC_B_FACTOR_DIVIDER = 100.0
MAX_SHORT = 32767
MIN_SHORT = -32768
NULL_BYTE = '\x00'
CHAIN_LEN = 4
NUM_DICT = {1:'b',2:'>h',4:'>i'}
