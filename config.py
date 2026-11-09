# config.py - change things here, not inside the panels
START_DATE = "2015-01-01"
BENCHMARK = "SPY"

TICKER_UNIVERSE = {
    "AAPL": "Apple", "MSFT": "Microsoft", "NVDA": "Nvidia",
    "AMZN": "Amazon", "GOOGL": "Alphabet", "META": "Meta",
    "TSLA": "Tesla", "JPM": "JPMorgan", "JNJ": "Johnson & Johnson",
    "XOM": "ExxonMobil", "KO": "Coca-Cola", "ASML": "ASML (US listing)",
    "CRH": "CRH", "RYAAY": "Ryanair (US listing)",
}
DEFAULT_TICKERS = ["AAPL", "MSFT", "NVDA", "JNJ"]
MAX_TICKERS = 6
START_AMOUNT = 10_000          # euro invested in the panel 2 backtest

COLOURS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#6250d6"]
GOAL_COLOUR = "#e34948"
BENCHMARK_COLOUR = "#888780"
