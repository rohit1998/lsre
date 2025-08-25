import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""# Tutorial on lsre""")
    return


@app.cell
def _():
    import lsre

    import yaml
    import pandas as pd
    from pathlib import Path
    return Path, lsre, pd, yaml


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Basic Usage

    ```python
    lsre.is_ipv4('192.168.0.1')
    ```
    """
    )
    return


@app.cell
def _(lsre):
    lsre.is_ipv4('192.168.0.1')
    return


@app.cell
def _(mo):
    mo.md(r"""## List of all functions""")
    return


@app.cell
def _(lsre):
    function_name_list = [attr for attr in dir(lsre) if attr.startswith('is_')]
    function_name_list
    return (function_name_list,)


@app.cell
def _(mo):
    mo.md(r"""## Sample data""")
    return


@app.cell
def _(Path, yaml):
    input_path = Path('configs/config.yaml')

    with input_path.open("r", encoding="utf-8") as f:
        text_list = yaml.safe_load(f)['text_list']
    text_list
    return (text_list,)


@app.cell
def _(mo):
    mo.md(r"""## Result on sample data""")
    return


@app.cell
def _(function_name_list, lsre, pd, text_list):
    results = []

    for text in text_list:
        results.append([])
        for function_name in function_name_list:
            function = getattr(lsre, function_name)
            results[-1].append(function(text))

    results_df = pd.DataFrame(
        results,
        columns=function_name_list,
        index=text_list,
    )
    results_df
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
