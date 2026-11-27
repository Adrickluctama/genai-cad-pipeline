# genai_cad_pipeline

Generate CAD models from text prompts and store them in Azure with validation

## Installation

```bash
pip install genai_cad_pipeline
```

## Quick Start

```python
from genai_cad_pipeline import GenaiCadPipeline

instance = GenaiCadPipeline()
result = instance.run()
print(result)
```

## Features

- Text‑to‑CAD generation using OpenAI or Stable Diffusion models
- Automatic conversion to STEP, STL, and OBJ formats
- Azure Blob storage upload with SAS token handling
- Schema validation of generated geometry

## API Reference

### `GenaiCadPipeline`

#### Constructor

```python
GenaiCadPipeline(options: GenaiCadPipelineOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `GenaiCadPipelineResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/genai_cad_pipeline/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
