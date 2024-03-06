import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

def add_image_to_certificate(certificate_path, uploaded_image, text, output_path):
    # Open the certificate image
    certificate_img = Image.open(certificate_path)
    
    # Open the uploaded image
    uploaded_img = Image.open(uploaded_image)
    
    # Resize the uploaded image
    uploaded_img = uploaded_img.resize((450, 475))  # Change dimensions as needed
    
    # Create a round mask
    mask = Image.new("L", uploaded_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, uploaded_img.size[0], uploaded_img.size[1]), fill=255)
    
    # Apply the round mask to the uploaded image
    uploaded_img.putalpha(mask)
    
    # Calculate the position to place the uploaded image
    position = (1107, 5)  # Change position as needed
    
    # Paste the uploaded image onto the certificate image
    certificate_img.paste(uploaded_img, position, uploaded_img)
    
    # Create a drawing context
    draw = ImageDraw.Draw(certificate_img)
    
    # Custom font style and font size for text
    font = ImageFont.truetype('arial.ttf', 40)
    
    text_position = (1200, 465)

    # Calculate the position to place the text
    # if len(text) <= 5:
    #     text_position = (1250, 450)
    # elif len(text) <= 10:
    #     text_position = (1200, 450)
    # elif len(text) >= 15:
    #     text_position = (1120, 450)
    # else:
    #     # Default position if text length is not 5 or 15
    #     text_position = (1200, 450)
    
    # Add text to the certificate image
    draw.text(text_position, text, fill="black", font=font)
    
    # Save the edited image
    certificate_img.save(output_path)

def main():
    st.title("Certificate Creator")
    
    # User input for uploading image
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    
    # User input for text
    text = st.text_input("Enter text:")
    
    if st.button("Generate Certificate"):
        if uploaded_image:
            # Save the uploaded image temporarily
            temp_image_path = "temp_image.png"
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_image.getvalue())
            
            # Call function to add image to the certificate
            add_image_to_certificate('Certificate.jpg', temp_image_path, text, 'generated_certificate.png')
            
            # Display the edited certificate
            st.image('generated_certificate.png', caption="Generated Certificate", use_column_width=True)
            
            # Remove the temporary image file
            os.remove(temp_image_path)
        else:
            st.warning("Please upload an image.")

if __name__ == "__main__":
    main()
