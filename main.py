import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def analyze_scatter_plot(image_path):
    # Load the image
    img = mpimg.imread(image_path)
    
    # Display the image
    plt.imshow(img)
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()
    
    # Define the data points (this step is manual and needs adjustment for each specific image)
    x = np.array([600, 700, 1000, 1200, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000])
    y = np.array([250, 300, 200, 300, 150, 100, 250, 350, 300, 400, 300, 400, 350, 450, 250, 350, 400, 300, 500, 450, 400, 500, 550, 500, 600, 400, 500, 550, 600, 650, 600])
    
    # Calculate the center (mean of x and y)
    center_x = np.mean(x)
    center_y = np.mean(y)
    
    # Plot the scatter plot and the center point
    plt.scatter(x, y, color='red')
    plt.axhline(y=400, color='blue', linestyle='-')
    plt.scatter(center_x, center_y, color='green', marker='o', s=100)  # Center point
    
    # Add labels and title
    plt.xlabel('size in feet²')
    plt.ylabel('price in $1000\'s')
    plt.title('Scatter Plot with Center Point')
    plt.show()
    
    return center_x, center_y

# Example usage
image_path = '/path/to/your/image.png'
center_x, center_y = analyze_scatter_plot(image_path)
print(f"Center of data points: size = {center_x:.2f} square feet, price = ${center_y:.2f} thousand")
