import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def analyze_scatter_plot(image_path):
    # Load the image
    img = mpimg.imread(image_path)

    # Display the image
    plt.imshow(img)
    plt.show()

    # Manually input the data points from the scatter plot
    data_points = [
        # Example data points, replace these with the actual points from your scatter plot
        (500, 200), (1000, 250), (1500, 300), (2000, 350), (2500, 400),
        (3000, 450), (3500, 500), (4000, 550), (4500, 600)
    ]

    # Extract x and y coordinates
    x, y = zip(*data_points)

    # Calculate the center (mean of x and y)
    center_x = np.mean(x)
    center_y = np.mean(y)

    # Plot the scatter plot and the center point
    plt.scatter(x, y, color='red')
    plt.scatter(center_x, center_y, color='green', marker='o', s=100)  # Center point

    # Add labels and title
    plt.xlabel('size in feet²')
    plt.ylabel('price in $1000\'s')
    plt.title('Scatter Plot with Center Point')
    plt.show()

    return center_x, center_y

# Example usage
# Update this path to the correct location of your image
image_path = './image.png'
center_x, center_y = analyze_scatter_plot(image_path)
print(f"Center of data points: size = {center_x:.2f} square feet, price = ${center_y:.2f} thousand")
