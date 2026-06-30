# new_pipeline_test — finish deployment in Databricks

SDP Builder staged a **Declarative Automation Bundle** project. Databricks recognizes a folder as a bundle when
`databricks.yml` is at the project root (see [bundle configuration reference](https://docs.databricks.com/aws/en/dev-tools/bundles/reference)).

Staged copy in workspace: `/Workspace/Users/laurel.kremer@databricks.com/sdp-bundles/new_pipeline_test`


## 1. Push this project to GitHub

Remote URL: `https://github.com/kremerlal/deploy-test-3`

From your laptop (in a folder containing these bundle files):

```bash
git init
git add .
git commit -m "Add SDP Builder bundle new_pipeline_test"
git branch -M main
git remote add origin https://github.com/kremerlal/deploy-test-3
git push -u origin main
```


## 2. Open the bundle in a Git folder

In the Databricks workspace:

1. **Workspace** → **Create** → **Git folder** (or clone into `/Repos/laurel.kremer@databricks.com/new_pipeline_test`).
2. Paste your GitHub repository URL and clone.
3. Open **`databricks.yml`** in the bundle editor.

Databricks should show the **Deployments** icon (rocket) in the left sidebar.

## 3. Deploy with the bundle UI

1. Click the **Deployments** icon.
2. Select target **`dev`**.
3. Click **Deploy** and confirm.

Deployed resources appear under **Bundle resources**. Run the pipeline with the play icon, or:

```bash
databricks bundle run new_pipeline_test_etl --target dev
```

Optional job resource key: `new_pipeline_test_job`.


## 4. Promote to production (after dev deploy succeeds)

1. Open **`databricks.yml`** in your Git folder (Deployments icon visible).
2. In the **Deployments** pane, change the target dropdown from **dev** to **prod**.
3. Click **Deploy** and confirm.

Or from CLI: `databricks bundle deploy --target prod`

Docs: [Deploy bundles from the workspace](https://docs.databricks.com/aws/en/dev-tools/bundles/workspace-deploy)
