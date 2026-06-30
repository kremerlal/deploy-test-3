# new_pipeline_test

SDP Builder bundle for pipeline `dbbbc400-2573-4238-82ff-c6ce8259a1a6`.

| File | Purpose |
|------|---------|
| `databricks.yml` | Bundle root — open this in a **Git folder** to enable the Deployments UI |
| `resources/new_pipeline_test_etl.pipeline.yml` | Lakeflow pipeline resource |
| `resources/new_pipeline_test_job.job.yml` | Optional job to refresh the pipeline |
| `src/new_pipeline_test.py` | PySpark `pipelines as dp` source |
| `GIT_SETUP.md` | GitHub + workspace deploy steps |

See **GIT_SETUP.md** for the full workflow (push to GitHub → clone Git folder → Deploy).
