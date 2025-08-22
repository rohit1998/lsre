import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _(hello):
    hello
    return


@app.cell
def _():
    hello = "Hello World!"
    return (hello,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
