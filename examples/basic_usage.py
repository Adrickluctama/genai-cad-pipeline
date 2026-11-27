#!/usr/bin/env python3
"""Basic usage example for genai_cad_pipeline."""

from genai_cad_pipeline import GenaiCadPipeline, GenaiCadPipelineOptions


def main() -> None:
    # Create with default options
    instance = GenaiCadPipeline()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = GenaiCadPipelineOptions(verbose=True)
    instance = GenaiCadPipeline(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
