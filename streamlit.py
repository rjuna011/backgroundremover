import streamlit as st
import rembg
from PIL import Image
from io import BytesIO
import os

def remove_background(input_image):
    with open(input_image, "rb") as input_file:
        input_data = input_file.read()

    output_data = rembg.remove(input_data)

    output_image = Image.open(BytesIO(output_data))
    return output_image

def main():
    st.title("Background Remover App")
    st.write("Upload an image with a background and remove it!")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Original Image", use_column_width=True)

        if st.button("Remove Background"):
            # Convert the uploaded image to a PIL Image
            image = Image.open(uploaded_image)
            
            # Save the uploaded image to a temporary file
            temp_image_path = f"temp_{uploaded_image.name}"
            image.save(temp_image_path)

            # Remove the background
            removed_background_image = remove_background(temp_image_path)

            # Display the result
            st.image(removed_background_image, caption="Image without Background", use_column_width=True)

            # Clean up temporary file
            os.remove(temp_image_path)

if __name__ == "__main__":
    main()