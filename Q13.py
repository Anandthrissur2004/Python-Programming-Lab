import numpy as np

def main() -> None:
    image = np.array(
        [
            [0, 40, 80, 120],
            [30, 70, 110, 150],
            [60, 100, 140, 180],
            [90, 130, 170, 220],
        ],
        dtype=np.uint8,
    )

    reshaped_image = image.reshape(2, 8)
    image_region = image[1:3, 1:3]
    brightened_image = np.clip(image + 30, 0, 255)

    transformation_matrix = np.array(
        [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
        ]
    )
    transformed_image = np.matmul(brightened_image, transformation_matrix)

    print("Original image matrix:")
    print(image)
    print("\nReshaped image (2 x 8):")
    print(reshaped_image)
    print("\nSliced image region (rows 1-2, columns 1-2):")
    print(image_region)
    print("\nBrightened image (clipped to 0-255):")
    print(brightened_image)
    print("\nTransformed image (columns reversed):")
    print(transformed_image)


if __name__ == "__main__":
    main()