import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('temp_dir/study_data.csv', sep=';')


def sanitized_col_names(col_names: list) -> list:
    new_col_names = []
    for column in col_names:
        column = column.replace(' ', '_')
        column = column.lower()
        new_col_names.append(column)
    return new_col_names


def drop_columns():
    col_del = ['difficulty', 'temp1', 'temp2']
    data.drop(columns=col_del, inplace=True)


def replace_null_data(col_names: list) -> None:
    for col in col_names:
        data[col] = data[col].fillna(value=0)


def plot_graphs():
    plt.figure(figsize=(24, 10), dpi=300)

    sns.set_context("talk")

    sequential_colors = sns.color_palette("Blues", 3)

    g = sns.histplot(
        data,
        x="date",
        hue="type",
        bins=9,
        palette=sequential_colors,
        hue_order=["Pairing", "Coding", "Studying"],
        multiple="stack",
        linewidth=.5,
    )

    g.figure.suptitle("Progress since 2 January 2022", y=0.92)

    plt.xticks(rotation=70)

    plt.savefig("temp_dir/graph_1.png", bbox_inches='tight')
    plt.close()


def main():
    print("Loading data")
    data.columns = sanitized_col_names(data.columns)
    drop_columns()
    replace_null_data(['date', 'time_start', 'time_end'])
    data['date'] = pd.to_datetime(data.date, format='%d/%m/%Y')
    data["cumulative_units"] = data["units"].cumsum()
    plot_graphs()


if __name__ == "__main__":
    main()
