import pandas as pd
import matplotlib.pyplot as plt

# TODO: filter >10min videos
def main():
    df = pd.read_csv('./src/output/output.csv')

    # Sort the data in descending order based on the 'count' column
    df = df.sort_values(by='count', ascending=False)

    # Extract the data for plotting
    categories = df['category']
    counts = df['count']

    # Calculate the maximum count to set the y-axis limit
    max_count = max(counts)

    # Define custom y-axis ticks in millions
    y_ticks = [0, 1, 2, 3, 4, 5]

    # Plotting the data using a bar chart
    plt.figure(figsize=(12, 6))
    bars = plt.bar(categories, counts, color='b')
    plt.xlabel('Categories')
    plt.ylabel('Count (Millions)')
    plt.title('Category Counts')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility

    # Set y-axis limit to fit the custom ticks range
    plt.ylim(0, max_count)

    # Set custom y-axis ticks and labels
    plt.yticks([tick * 1_000_000 for tick in y_ticks], y_ticks)

    # Display the actual count on top of each bar
    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count),
                ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()