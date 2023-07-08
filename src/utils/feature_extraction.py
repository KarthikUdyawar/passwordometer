"""
Module for password strength calculation.

This module provides a function for calculating the strength of a password
based on certain criteria.
"""
from typing import Any, Optional

import numpy as np
import pandas as pd
from password_strength import PasswordStats
from sklearn.base import BaseEstimator, TransformerMixin


def calculate_strength(text: str) -> float:
    """
    Calculate the strength of a password.

    Args:
        text (str): The password for which the strength will be calculated.

    Returns:
        float: The strength value of the password.
    """
    return float(PasswordStats(text).strength())


class LenTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the length of the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "LenTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the length of each password.
        """
        X["len"] = X["password"].apply(self._lenTransform)
        transformed_X = X["len"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _lenTransform(self, text: str) -> int:
        """Calculate the length of the input text.

        Args:
            text (str): Input text (password).

        Returns:
            int: Length of the input text (password).
        """
        return len(text)


class AlphaUCTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of uppercase alphabetic characters
    in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "AlphaUCTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of uppercase alphabetic characters in each password.
        """
        X["alphaUC"] = X["password"].apply(self._alphaUCTransform)
        transformed_X = X["alphaUC"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _alphaUCTransform(self, text: str) -> int:
        """Calculate the count of uppercase alphabetic characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of uppercase alphabetic characters in the input text.
        """
        return sum(bool(a.isupper()) for a in text)


class AlphaLCTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of lowercase alphabetic
    characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "AlphaLCTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of lowercase alphabetic characters in each password.
        """
        X["alphaLC"] = X["password"].apply(self._alphaLCTransform)
        transformed_X = X["alphaLC"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _alphaLCTransform(self, text: str) -> int:
        """Calculate the count of lowercase alphabetic characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of lowercase alphabetic characters in the input text.
        """
        return sum(bool(a.islower()) for a in text)


class NumberTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of numeric characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "NumberTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of numeric characters in each password.
        """
        X["number"] = X["password"].apply(self._numberTransform)
        transformed_X = X["number"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _numberTransform(self, text: str) -> int:
        """Calculate the count of numeric characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of numeric characters in the input text.
        """
        return sum(bool(a.isdecimal()) for a in text)


class SymbolTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of special symbol characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "SymbolTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of special symbol characters in each password.
        """
        X["symbol"] = X["password"].apply(self._symbolTransform)
        transformed_X = X["symbol"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _symbolTransform(self, text: str) -> int:
        """Calculate the count of special symbol characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of special symbol characters in the input text.
        """
        return sum(a in set("!@#$%^&*") for a in text)


class MidCharTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of special symbol or
    numeric characters in the middle of the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "MidCharTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of special symbol or numeric characters
            in the middle of each password.
        """
        X["midChar"] = X["password"].apply(self._midCharTransform)
        transformed_X = X["midChar"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _midCharTransform(self, text: str) -> int:
        """Calculate the count of special symbol or numeric
        characters in the middle of the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of special symbol or numeric characters in the middle of the input text.
        """
        return sum(
            bool(a.isdecimal() or (a in set("!@#$%^&*"))) for a in text[1:-1]
        )
        # R1716: Simplify chained comparison between the operands (chained-comparison)


class RepCharTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of repeated characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "RepCharTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of repeated characters in each password.
        """
        X["repChar"] = X["password"].apply(self._repCharTransform)
        transformed_X = X["repChar"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _repCharTransform(self, text: str) -> int:
        """Calculate the count of repeated characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of repeated characters in the input text.
        """
        return len(text) - len(list(set(text)))


class UniqueCharTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of unique characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "UniqueCharTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of unique characters in each password.
        """
        X["uniqueChar"] = X["password"].apply(self._uniqueCharTransform)
        transformed_X = X["uniqueChar"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _uniqueCharTransform(self, text: str) -> int:
        """Calculate the count of unique characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of unique characters in the input text.
        """
        return len(list(set(text)))


class ConsecAlphaUCTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of consecutive uppercase
    alphabetic characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "ConsecAlphaUCTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of consecutive uppercase alphabetic characters in each password.
        """
        X["consecAlphaUC"] = X["password"].apply(self._consecAlphaUCTransform)
        transformed_X = X["consecAlphaUC"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _consecAlphaUCTransform(self, text: str) -> int:
        """Calculate the count of consecutive uppercase alphabetic characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of consecutive uppercase alphabetic characters in the input text.
        """
        temp = ""
        nConsecAlphaUC = 0
        for a in text:
            if a.isupper():
                if temp and temp[-1] == a:
                    nConsecAlphaUC += 1
                temp = a
        return nConsecAlphaUC


class ConsecAlphaLCTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of consecutive lowercase
    alphabetic characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "ConsecAlphaLCTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of consecutive lowercase alphabetic characters in each password.
        """
        X["consecAlphaLC"] = X["password"].apply(self._consecAlphaLCTransform)
        transformed_X = X["consecAlphaLC"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _consecAlphaLCTransform(self, text: str) -> int:
        """Calculate the count of consecutive lowercase alphabetic characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of consecutive lowercase alphabetic characters in the input text.
        """
        temp = ""
        nConsecAlphaLC = 0
        for a in text:
            if a.islower():
                if temp and temp[-1] == a:
                    nConsecAlphaLC += 1
                temp = a
        return nConsecAlphaLC


class ConsecNumberTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of consecutive numeric characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "ConsecNumberTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of consecutive numeric characters in each password.
        """
        X["consecNumber"] = X["password"].apply(self._consecNumberTransform)
        transformed_X = X["consecNumber"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _consecNumberTransform(self, text: str) -> int:
        """Calculate the count of consecutive numeric characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of consecutive numeric characters in the input text.
        """
        temp = ""
        nConsecNumber = 0
        for a in text:
            if a.isdecimal():
                if temp and temp[-1] == a:
                    nConsecNumber += 1
                temp = a
        return nConsecNumber


class ConsecSymbolTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of consecutive special symbol
    characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "ConsecSymbolTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of consecutive special symbol characters in each password.
        """
        X["consecSymbol"] = X["password"].apply(self._consecSymbolTransform)
        transformed_X = X["consecSymbol"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _consecSymbolTransform(self, text: str) -> int:
        """Calculate the count of consecutive special symbol characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of consecutive special symbol characters in the input text.
        """
        temp = ""
        nConsecSymbol = 0
        for a in text:
            if a in set("!@#$%^&*"):
                if temp and temp[-1] == a:
                    nConsecSymbol += 1
                temp = a
        return nConsecSymbol


class SeqAlphaTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of sequential alphabetic
    characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "SeqAlphaTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of sequential alphabetic characters in each password.
        """
        X["seqAlpha"] = X["password"].apply(self._seqAlphaTransform)
        transformed_X = X["seqAlpha"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _seqAlphaTransform(self, text: str) -> int:
        """Calculate the count of sequential alphabetic characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of sequential alphabetic characters in the input text.
        """
        sAlphas = "abcdefghijklmnopqrstuvwxyz"
        nSeqAlpha = 0
        for s in range(len(sAlphas) - 2):
            sFwd = sAlphas[s : s + 3]
            sRev = sFwd[::-1]
            if sFwd in text.lower() or sRev in text.lower():
                nSeqAlpha += 1
        return nSeqAlpha


class SeqNumberTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of sequential numeric characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "SeqNumberTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of sequential numeric characters in each password.
        """
        X["seqNumber"] = X["password"].apply(self._seqNumberTransform)
        transformed_X = X["seqNumber"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _seqNumberTransform(self, text: str) -> int:
        """Calculate the count of sequential numeric characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of sequential numeric characters in the input text.
        """
        sNumerics = "01234567890"
        nSeqNumber = 0
        for s in range(len(sNumerics) - 2):
            sFwd = sNumerics[s : s + 3]
            sRev = sFwd[::-1]
            if sFwd in text.lower() or sRev in text.lower():
                nSeqNumber += 1
        return nSeqNumber


class SeqKeyboardTransform(BaseEstimator, TransformerMixin):  # type: ignore
    """Transformer that calculates the count of sequential keyboard characters in the input text."""

    def fit(
        self, X: pd.DataFrame, y: Optional[np.ndarray[np.int64, Any]] = None
    ) -> "SeqKeyboardTransform":
        """Fit the transformer to the data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.
            y (np.ndarray, optional): Target values. Defaults to None.

        Returns:
            self: Returns an instance of self.
        """
        return self

    def transform(self, X: pd.DataFrame) -> np.ndarray[np.int64, Any]:
        """Transform the input data.

        Args:
            X (pd.DataFrame): Input data containing a "password" column.

        Returns:
            np.ndarray: Transformed data as a 2D NumPy array with one column
            representing the count of sequential keyboard characters in each password.
        """
        X["seqKeyboard"] = X["password"].apply(self._seqKeyboardTransform)
        transformed_X = X["seqKeyboard"].to_numpy()
        return np.array(transformed_X).reshape(-1, 1)

    def _seqKeyboardTransform(self, text: str) -> int:
        """Calculate the count of sequential keyboard characters in the input text.

        Args:
            text (str): Input text.

        Returns:
            int: Count of sequential keyboard characters in the input text.
        """
        sTopRow = "qwertyuiop"
        sHomeRow = "asdfghjkl"
        sBottomRow = "zxcvbnm"
        nKeyboard = 0
        sRows = [sTopRow, sHomeRow, sBottomRow]

        for sRow in sRows:
            for s in range(len(sRow) - 2):
                sFwd = sRow[s : s + 3]
                sRev = sFwd[::-1]
                if sFwd in text.lower() or sRev in text.lower():
                    nKeyboard += 1

        return nKeyboard
