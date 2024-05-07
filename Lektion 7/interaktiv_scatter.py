import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
  
def scatterplot(df, x_plot, y_plot, target):
    sns.scatterplot(data=df, x=x_plot, y=y_plot, hue=target)
    plt.xlabel(x_plot)
    plt.ylabel(y_plot)
    plt.title(f"{x_plot} vs {y_plot}")
    plt.legend(title="Species")
    plt.show()

def int_scatterplot(df, x_plot, y_plot, x_value, y_value, target):
    fig = px.scatter(df, x=x_plot, y=y_plot, color=target,
                     title=f"{x_plot} vs {y_plot}",
                     labels={x_plot: f"{x_plot} {x_value}", y_plot: f"{y_plot} {y_value}"},
                     hover_data={target: True},
                     opacity=0.7,
                     symbol=target)
    fig.show()

# Indlæser csv
df = pd.read_csv(r"Lektion 7\iris.csv")

# Finder punkter til at plot
df.info()

scatterplot(df, "sepal_length", "sepal_width", "species")
int_scatterplot(df, "sepal_length", "sepal_width", "(cm)", "(cm)", "species")
