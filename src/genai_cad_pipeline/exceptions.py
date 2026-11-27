"""Custom exceptions for genai_cad_pipeline."""

from __future__ import annotations


class GenaiCadPipelineError(Exception):
    """Base exception for all GenaiCadPipeline errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(GenaiCadPipelineError):
    """Raised when the SDK is misconfigured."""


class ValidationError(GenaiCadPipelineError):
    """Raised when input validation fails."""


class TimeoutError(GenaiCadPipelineError):
    """Raised when an operation exceeds its time limit."""
