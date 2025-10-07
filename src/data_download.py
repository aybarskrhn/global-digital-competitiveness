"""Utilities for downloading World Bank indicators with offline fallbacks."""
from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Dict, Iterable, Optional

import pandas as pd

try:
    import wbdata  # type: ignore
except ImportError:  # pragma: no cover - wbdata is optional for offline workflows
    wbdata = None  # type: ignore


DEFAULT_DATA_DIR = Path(__file__).resolve().parents[1] / "data"
RAW_DIR = DEFAULT_DATA_DIR / "raw"


class DataDownloadError(RuntimeError):
    """Raised when an indicator cannot be downloaded and no fallback data exists."""


def _resolve_output_path(indicator_id: str, output_path: Optional[Path]) -> Path:
    if output_path is None:
        output_path = RAW_DIR / f"{indicator_id.lower()}_wbdata.csv"
    return output_path


def fetch_indicator(
    indicators: Dict[str, str],
    data_date: tuple[dt.datetime, dt.datetime],
    countries: Optional[Iterable[str]] = None,
    convert_date: bool = True,
    output_path: Optional[Path] = None,
    fallback_file: Optional[Path] = None,
) -> pd.DataFrame:
    """Fetch a World Bank indicator with an optional offline fallback.

    Parameters
    ----------
    indicators:
        Mapping of indicator codes to column names (as expected by ``wbdata``).
    data_date:
        Tuple of start and end dates for the data.
    countries:
        Iterable of country ISO codes to filter. ``None`` downloads all countries.
    convert_date:
        Whether to convert the date column to pandas ``datetime`` objects.
    output_path:
        Optional path to save the downloaded data for reuse.
    fallback_file:
        Optional CSV file to use when the download fails.

    Returns
    -------
    ``pd.DataFrame``
        The indicator data with column names defined by ``indicators``.

    Raises
    ------
    DataDownloadError
        If the indicator cannot be downloaded and no fallback data is provided.
    """

    indicator_id = next(iter(indicators))
    output_path = _resolve_output_path(indicator_id, output_path)

    if wbdata is None:
        return _load_fallback(fallback_file, indicator_id)

    try:
        df = wbdata.get_dataframe(
            indicators,
            data_date=data_date,
            country=countries,
            convert_date=convert_date,
        )
    except Exception as exc:  # pragma: no cover - network-dependent
        df = _handle_download_failure(exc, fallback_file, indicator_id)
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path)

    return df.reset_index()


def _handle_download_failure(
    error: Exception, fallback_file: Optional[Path], indicator_id: str
) -> pd.DataFrame:
    """Handle download failure by loading the fallback file if available."""

    if fallback_file is not None:
        return _load_fallback(fallback_file, indicator_id)

    raise DataDownloadError(
        "World Bank download failed and no fallback data was provided."
    ) from error


def _load_fallback(fallback_file: Optional[Path], indicator_id: str) -> pd.DataFrame:
    """Load fallback data from disk or raise an informative error."""

    if fallback_file is None:
        fallback_file = RAW_DIR / f"{indicator_id.lower()}_fallback.csv"

    if not fallback_file.exists():
        raise DataDownloadError(
            f"Fallback data file not found at '{fallback_file}'."
        )

    return pd.read_csv(fallback_file)


__all__ = ["DataDownloadError", "fetch_indicator"]
