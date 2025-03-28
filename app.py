from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import numpy as np
import json
import plotly
import os
print("Templates folder path:", os.path.abspath("templates"))



app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    df = pd.read_csv("coffee_exports.csv")

    # Create Plotly figure
    fig = px.bar(
        df,
        x="Country",
        y="Export_Tons",
        color="Region",
        title="Coffee Exports by Country (in Tons)"
    )

    # Match dark theme layout
    fig.update_layout(
        plot_bgcolor='#1a1c23',
        paper_bgcolor='#1a1c23',
        font_color='#ffffff',
        autosize=True,
        margin=dict(t=50, l=50, r=50, b=50),
        height=600
    )
    fig.update_xaxes(showgrid=False, color='#cccccc')
    fig.update_yaxes(showgrid=False, color='#cccccc')

    # Convert to JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(debug=True)