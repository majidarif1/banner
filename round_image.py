import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

def add_image_to_certificate(certificate_path, uploaded_image, text, output_path):
    # Open the certificate image
    certificate_img = Image.open(certificate_path)
    
    # Open the uploaded image
    uploaded_img = Image.open(uploaded_image)
    
    # Resize the uploaded image
    uploaded_img = uploaded_img.resize((360, 330))  # Change dimensions as needed
    
    # Create a round mask
    mask = Image.new("L", uploaded_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, uploaded_img.size[0], uploaded_img.size[1]), fill=255)
    
    # Apply the round mask to the uploaded image
    uploaded_img.putalpha(mask)
    
    # Calculate the position to place the uploaded image
    position = (1150, 105)  # Change position as needed
    
    # Paste the uploaded image onto the certificate image
    certificate_img.paste(uploaded_img, position, uploaded_img)
    
    # Create a drawing context
    draw = ImageDraw.Draw(certificate_img)
    
    # Custom font style and font size for text
    font = ImageFont.truetype('arial.ttf', 38)
    
    # text_position = (1200, 465)

    # Calculate the position to place the text
    if len(text) <= 5:
        text_position = (1250, 460)
    elif len(text) <= 10:
        text_position = (1200, 460)
    elif len(text) >= 15:
        text_position = (1120, 460)
    else:
        # Default position if text length is not 5 or 15
        text_position = (1200, 460)
    
    # Add text to the certificate image
    draw.text(text_position, text, fill="black", font=font)
    
    # Save the edited image
    certificate_img.save(output_path)

def main():
    st.title("Banner Creator")
    
    # User input for uploading image
    uploaded_image = st.file_uploader("Upload your Picture", type=["jpg", "jpeg", "png"])
    
    # User input for text
    text = st.text_input("Enter your name:")
    
    if st.button("Generate Banner"):
        if uploaded_image:
            # Save the uploaded image temporarily
            temp_image_path = "temp_image.png"
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_image.getvalue())
            
            # Call function to add image to the certificate
            add_image_to_certificate('KAI-MEETUP-ATTEND-SHARE.jpg', temp_image_path, text, 'generated_banner.png')
            
            # Display the edited certificate
            st.image('generated_banner.png', caption="Banner Generated", use_column_width=True)
            
            st.download_button(
                label="Download Banner",
                data=open('generated_banner.png', 'rb').read(),
                file_name='generated_banner.png',
                mime='image/png'
            )

            # Remove the temporary image file
            os.remove(temp_image_path)
        else:
            st.warning("Please upload your Picture.")

if __name__ == "__main__":
    main()
