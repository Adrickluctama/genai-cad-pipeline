"""Type definitions for genai_cad_pipeline."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class GenaiCadPipelineOptions:
    """Configuration options for GenaiCadPipeline.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Text‑to‑CAD generation using OpenAI or Stable Diffusion models
        feature_2: Configuration for: Automatic conversion to STEP, STL, and OBJ formats
        feature_3: Configuration for: Azure Blob storage upload with SAS token handling
        feature_4: Configuration for: Schema validation of generated geometry
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None
    feature_4: Optional[dict[str, Any]] = None


@dataclass
class GenaiCadPipelineResult:
    """Result returned by GenaiCadPipeline operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
