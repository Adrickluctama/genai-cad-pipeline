"""Tests for genai_cad_pipeline."""

from genai_cad_pipeline import GenaiCadPipeline, GenaiCadPipelineOptions


class TestGenaiCadPipeline:
    def test_create_instance_with_defaults(self) -> None:
        instance = GenaiCadPipeline()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = GenaiCadPipelineOptions(verbose=True)
        instance = GenaiCadPipeline(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = GenaiCadPipeline()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = GenaiCadPipeline()
        result = instance.run()
        assert result.error is None
