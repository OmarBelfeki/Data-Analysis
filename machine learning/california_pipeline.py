from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
import time

def load_data(console):
    console.print("[bold blue]Loading California Housing Dataset...[/bold blue]")
    california = fetch_california_housing(as_frame=True)
    data = california.frame

    table = Table(title="Dataset Preview")
    for column in data.columns:
        table.add_column(column)
    for _, row in data.head().iterrows():
        table.add_row(*[str(x) for x in row])
    console.print(table)
    return data

def create_pipeline():
    return Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', LinearRegression())
    ])

def train_and_evaluate(pipeline, X_train, X_test, y_train, y_test, console):
    console.print("\n[bold green]Training the Model[/bold green]")

    start_time = time.time()

    with Progress() as progress:
        task = progress.add_task("[cyan]Training...", total=100)

        for i in range(100):
            time.sleep(0.05)  # Simulate training time
            progress.update(task, advance=1)

        pipeline.fit(X_train, y_train)

    end_time = time.time()
    duration = end_time - start_time

    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    console.print("\n[bold yellow]Evaluation Results[/bold yellow]")
    results_table = Table(title="Evaluation Metrics")
    results_table.add_column("Metric", justify="center", style="cyan")
    results_table.add_column("Value", justify="center", style="magenta")
    results_table.add_row("Mean Squared Error", f"{mse:.2f}")
    results_table.add_row("Time Taken (s)", f"{duration:.2f}")
    console.print(results_table)


if __name__ == "__main__":
    console = Console()

    data = load_data(console)

    console.print("\n[bold yellow]Splitting Data...[/bold yellow]")
    X = data.drop(columns='MedHouseVal')
    y = data['MedHouseVal']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = create_pipeline()

    train_and_evaluate(pipeline, X_train, X_test, y_train, y_test, console)
