from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path):
    try:
        # Open the image
        image = Image.open(input_image_path)
        # Convert image to numpy array
        data = np.array(image)

        # Perform pixel manipulation for encryption
        encrypted_data = np.copy(data)
        height, width, channels = encrypted_data.shape

        for i in range(height):
            for j in range(width):
                # Swap pixel values with the next pixel
                if j < width - 1:
                    encrypted_data[i, j], encrypted_data[i, j + 1] = encrypted_data[i, j + 1], encrypted_data[i, j]
                # Add a constant value to each pixel and ensure it stays within 0-255
                encrypted_data[i, j] = np.clip(encrypted_data[i, j] + 50, 0, 255)  # Ensure values stay within 0-255

        # Save the encrypted image
        encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
        encrypted_image.save(output_image_path)
        print(f"Image encrypted and saved as {output_image_path}")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(input_image_path, output_image_path):
    try:
        # Open the encrypted image
        image = Image.open(input_image_path)
        # Convert image to numpy array
        data = np.array(image)

        # Perform pixel manipulation for decryption
        decrypted_data = np.copy(data)
        height, width, channels = decrypted_data.shape

        for i in range(height):
            for j in range(width):
                # Subtract the constant value from each pixel and ensure it stays within 0-255
                decrypted_data[i, j] = np.clip(decrypted_data[i, j] - 50, 0, 255)  # Ensure values stay within 0-255
                # Swap pixel values back
                if j < width - 1:
                    decrypted_data[i, j], decrypted_data[i, j + 1] = decrypted_data[i, j + 1], decrypted_data[i, j]

        # Save the decrypted image
        decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
        decrypted_image.save(output_image_path)
        print(f"Image decrypted and saved as {output_image_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == "__main__":
    input_image_path = 'input_image.png'  
    encrypted_image_path = 'encrypted_image.png'
    decrypted_image_path = 'decrypted_image.png'

    encrypt_image(input_image_path, encrypted_image_path)
    decrypt_image(encrypted_image_path, decrypted_image_path)
