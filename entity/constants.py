
TIME_FMT = "%Y-%m-%dT%H:%M:%S%z"
TIME_FMT_SEC = "%Y-%m-%d %H:%M:%S"
TIME_FMT_MIN = "%Y-%m-%d %H:%M"

DATASOURCE_ALPACA = 'alpaca'
DATASOURCE_POLYGON = 'polygon'
DATASOURCE_BINANCE = 'binance'
DATASOURCE_BITMEX = 'bitmex'
DATASOURCE_CACHE = 'cache'
DATATYPE_TICKER = "ticker"
DATATYPE_ORDERBOOK = "orderbook"
DATATYPE_UNIVERSE = "universe"
FREQ_DAY = 'day'
FREQ_MINUTE = 'minute'

TRADING_ALPACA = 'alpaca'
TRADING_BINANCE = 'binance'
TRADING_BACKTEST = 'backtest'

TRADING_PLATFORM_DATASOURCE = {
    TRADING_ALPACA: DATASOURCE_ALPACA,
    TRADING_BINANCE: DATASOURCE_BINANCE,
}

VALID_DATASOURCE = [DATASOURCE_POLYGON, DATASOURCE_ALPACA, DATASOURCE_BINANCE, DATASOURCE_CACHE, DATASOURCE_BITMEX]
VALID_FREQ = [FREQ_DAY, FREQ_MINUTE]

DATA_FILE_FMT = "/type={type}/freq={freq}/dt={dt}/"
UNIVERSE_DATA_FILE_FMT = "/type={type}/"

DATA_KEY_DF = "df"
DATA_KEY_PATH = "path"

DATA_DATETIME = "Date Time"  # index
DATA_SYMBOL = 'Symbol'
DATA_OPEN = "Open"
DATA_HIGH = "High"
DATA_LOW = "Low"
DATA_CLOSE = "Close"
DATA_VOLUME = "Volume"
DATA_ADJCLOSE = "Adj Close"
DATA_HISTORICAL_COLS = [
    DATA_SYMBOL,
    DATA_OPEN,
    DATA_HIGH,
    DATA_LOW,
    DATA_CLOSE,
    DATA_VOLUME,
    DATA_ADJCLOSE]

DATA_ASK = "ask"
DATA_BID = "bid"
DATA_SELL_PCT = "sell{bin_idx}"
DATA_BUY_PCT = "buy{bin_idx}"

DATA_ORDERBOOK_COLS = [
    DATA_SYMBOL,
    DATA_ASK,
    DATA_BID,
]


ORDER_TYPE_MARKET = "market"
ORDER_TYPE_LIMIT = "limit"
ORDER_BUY = "buy"
ORDER_SELL = "sell"

ORDER_TIME_IN_FORCE_GTC = "GTC"  # Good till cancelled

# BINANCE
KLINES_DATA_COLS = [DATA_DATETIME, DATA_OPEN, DATA_HIGH, DATA_LOW, DATA_CLOSE, DATA_VOLUME, "CloseTime",
                    "QuoteVolume", "Trades", "TakerBuyBaseAssetVolume", "TakerBuyQuoteAssetVolume",
                    "ignore"]

# Polygon get_historical_data, /v2/aggs/ticker/
POLYGON_VOLUME = 'v'
POLYGON_OPEN = 'o'
POLYGON_CLOSE = 'c'
POLYGON_HIGH = 'h'
POLYGON_LOW = 'l'
POLYGON_TS = 't'
POLYGON_AGG_WINDOW = 'n'
POLYGON_SYMBOL = 'T'

POLYGON_DATA_COLS = []

ALPACA_VOLUME = 'volume'
ALPACA_OPEN = 'open'
ALPACA_CLOSE = 'close'
ALPACA_HIGH = 'high'
ALPACA_LOW = 'low'

# test
ENV_TEST_LEVEL = "TEST_LEVEL"
TEST_LEVEL_UNIT = "unit"
TEST_LEVEL_INTEGRATION = "integration"

# logger
LOGGER_GOQUANT = "goquant"