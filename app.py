import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load CSV
def load_csv(file):
    data = pd.read_csv(file.name)

    cols_to_keep = [
        'Book_ID', 'Department', 'Issue_Date', 'Due_Date',
        'Late_Days', 'Return_Date', 'Fine_Amount'
    ]

    df2 = data[cols_to_keep]
    return df2, df2.head(), df2.describe()

# Plot functions
def department_plot(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(x="Department", data=df, kde=True)
    plt.title("Department vs Fine Amount")
    plt.xlabel("Department")
    plt.ylabel("Fine Amount")
    return plt

def late_days_plot(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(x="Late_Days", data=df, kde=True)
    plt.title("Late Days vs Fine Amount")
    plt.xlabel("Late Days")
    plt.ylabel("Fine Amount")
    return plt

def box_plot(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Department", y="Fine_Amount", data=df)
    plt.title("Department vs Fine Amount")
    return plt

# Gradio UI
with gr.Blocks(title="College Library Late Fee Analysis") as demo:
    gr.Markdown("## College Library Late Fee Analysis")

    file_input = gr.File(label="Upload CSV File")
    df_state = gr.State()

    load_btn = gr.Button("Load Data")

    data_out = gr.Dataframe(label="Dataset Preview")
    desc_out = gr.Dataframe(label="Data Summary")

    load_btn.click(
        load_csv,
        inputs=file_input,
        outputs=[df_state, data_out, desc_out]
    )

    with gr.Tab("Plots"):
        btn1 = gr.Button("Department Plot")
        btn2 = gr.Button("Late Days Plot")
        btn3 = gr.Button("Box Plot")

        plot_out = gr.Plot()

        btn1.click(department_plot, inputs=df_state, outputs=plot_out)
        btn2.click(late_days_plot, inputs=df_state, outputs=plot_out)
        btn3.click(box_plot, inputs=df_state, outputs=plot_out)

demo.launch()