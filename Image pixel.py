# Import NumPy library for array operations
import numpy as np

# Define the main function
def main() -> None:

    # Create a 4 x 4 image matrix
    # Each number represents a pixel intensity (0-255)
    image = np.array(
        [
            [0, 40, 80, 120],
            [30, 70, 110, 150],
            [60, 100, 140, 180],
            [90, 130, 170, 220],
        ],
        dtype=np.uint8,  # Store pixel values as unsigned 8-bit integers
    )

    # Reshape the 4 x 4 matrix into a 2 x 8 matrix
    reshaped_image = image.reshape(2, 8)

    # Extract a region from rows 1 to 2 and columns 1 to 2
    image_region = image[1:3, 1:3]

    # Increase every pixel value by 30
    # np.clip() keeps pixel values between 0 and 255
    brightened_image = np.clip(image + 30, 0, 255)

    # Create a transformation matrix to reverse the columns
    transformation_matrix = np.array(
        [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
        ]
    )

    # Multiply the brightened image by the transformation matrix
    transformed_image = np.matmul(
        brightened_image, transformation_matrix
    )

    # Display the original image matrix
    print("Original image matrix:")
    print(image)

    # Display the reshaped image
    print("\nReshaped image (2 x 8):")
    print(reshaped_image)

    # Display the extracted image region
    print("\nSliced image region (rows 1-2, columns 1-2):")
    print(image_region)

    # Display the brightened image
    print("\nBrightened image (clipped to 0-255):")
    print(brightened_image)

    # Display the transformed image
    print("\nTransformed image (columns reversed):")
    print(transformed_image)


# Check whether the program is running directly
if __name__ == "__main__":

    # Call the main function
    main()
