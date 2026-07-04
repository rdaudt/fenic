# Fenic Operator Examples

This repository contains a small, runnable set of Fenic semantic DataFrame operator examples and their captured console output.

Fenic is a Python DataFrame library for semantic data processing. These examples show how common LLM and embedding workflows can be expressed as typed, inspectable DataFrame pipelines instead of ad hoc prompt scripts.

## Contents

- `fenic/scripts/operators/` - twelve focused operator examples plus shared session setup in `common.py`.
- `fenic/operator_outputs/` - captured console output from running each numbered operator script.
- `fenic-post.html` - a standalone enterprise engineering article that explains Fenic, evaluates enterprise readiness, and embeds each script with its output.

## Operator Scripts

| Script | Demonstrates |
| --- | --- |
| `01_extract.py` | Structured extraction from messy text with a Pydantic schema |
| `02_classify.py` | Semantic classification into predefined labels |
| `03_predicate.py` | Natural-language boolean filtering |
| `04_map.py` | Row-wise semantic transformation |
| `05_reduce.py` | Semantic aggregation across rows |
| `06_analyze_sentiment.py` | Built-in sentiment analysis |
| `07_summarize.py` | Text summarization |
| `08_embed.py` | Embedding generation |
| `09_parse_pdf.py` | PDF parsing into Markdown-style text |
| `10_semantic_join.py` | Natural-language DataFrame joins |
| `11_sim_join.py` | Embedding similarity joins |
| `12_with_cluster_labels.py` | Clustering over embeddings |

## Requirements

Use a Python environment with Fenic installed:

```bash
pip install fenic
```

The examples use OpenAI-backed language and embedding models configured in `fenic/scripts/operators/common.py`. Set an API key before running scripts that call models:

```bash
set OPENAI_API_KEY=your-key-here
```

On macOS or Linux:

```bash
export OPENAI_API_KEY=your-key-here
```

Running these scripts can incur API costs and may create local Fenic/DuckDB artifacts.

## Run Examples

Run one operator script:

```bash
python fenic/scripts/operators/01_extract.py
```

Run Fenic's static checker against a script:

```bash
fenic check fenic/scripts/operators/01_extract.py
```

Each captured output file under `fenic/operator_outputs/` corresponds to the matching numbered script.

## Article

Open `fenic-post.html` in a browser to read the standalone article. It includes:

- An executive summary of where Fenic fits.
- Practical enterprise use cases.
- Pros, cons, and operational risks.
- An enterprise-readiness matrix.
- Full source and captured output for all twelve operator examples.

## Notes

The outputs are representative captured runs from this project environment. LLM-backed results may vary between runs because model responses are probabilistic and provider behavior can change over time.
