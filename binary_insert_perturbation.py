import numpy as np
import matplotlib.pyplot as plt
import cv2

class AdversarialPerturbation:
    """
    Class for creating and applying adversarial perturbations to images.
    """

    def __init__(self, image_shape, intensity=0.05, pattern='stripes'):
        """
        Initialize the AdversarialPerturbation object.

        Args:
        - image_shape (tuple): The shape of the image (height, width, channels)
        - intensity (float): The intensity of the perturbation
        - pattern (str): The pattern type ('stripes', 'circles', etc.)
        """
        self.image_shape = image_shape
        self.intensity = intensity
        self.pattern = pattern

    def create_perturbation(self):
        """
        Create a complex adversarial perturbation with a specific pattern.

        Returns:
        - numpy.ndarray: An array representing the adversarial perturbation
        """
        perturbation = np.zeros(self.image_shape, dtype=np.float32)
        height, width, _ = self.image_shape

        if self.pattern == 'stripes':
            for i in range(0, width, 4):
                perturbation[:, i:i+2, :] = self.intensity
        elif self.pattern == 'circles':
            for i in range(40, min(height, width), 80):
                cv2.circle(perturbation, (width // 2, height // 2), i, (self.intensity, self.intensity, self.intensity), -1)

        return perturbation

    @staticmethod
    def binary_insert(image, perturbation):
        """
        Insert adversarial perturbation into an image using binary operation.

        Args:
        - image (numpy.ndarray): The original image
        - perturbation (numpy.ndarray): The adversarial perturbation

        Returns:
        - numpy.ndarray: The image with the perturbation inserted
        """
        perturbed_image = np.clip(image.astype(np.float32) + perturbation, 0, 255)
        return perturbed_image.astype(np.uint8)


# Generate a random sample image
image_shape = (224, 224, 3)
sample_image = np.random.randint(0, 255, image_shape, dtype=np.uint8)

# Create an instance of the AdversarialPerturbation class
perturbation_creator = AdversarialPerturbation(sample_image.shape, pattern='circles')

# Create a complex perturbation
perturbation = perturbation_creator.create_perturbation()

# Apply the binary insert
perturbed_image = AdversarialPerturbation.binary_insert(sample_image, perturbation)

# Show the original and perturbed images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(sample_image)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(perturbed_image)
plt.title("Perturbed Image")
plt.axis('off')

plt.show()

