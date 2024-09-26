import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

def add_image_to_certificate(certificate_path, uploaded_image, text, output_path):
    # Open the certificate image
    certificate_img = Image.open(certificate_path)
    
    # Open the uploaded image
    uploaded_img = Image.open(uploaded_image)
    
    # Resize the uploaded image
    uploaded_img = uploaded_img.resize((360, 335))  # Change dimensions as needed
    
    # Create a round mask
    mask = Image.new("L", uploaded_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, uploaded_img.size[0], uploaded_img.size[1]), fill=255)
    
    # Apply the round mask to the uploaded image
    uploaded_img.putalpha(mask)
    
    # Calculate the position to place the uploaded image
    position = (1150, 135)  # Change position as needed
    
    # Paste the uploaded image onto the certificate image
    certificate_img.paste(uploaded_img, position, uploaded_img)
    
    # Create a drawing context
    draw = ImageDraw.Draw(certificate_img)
    
    # Custom font style and font size for text
    font = ImageFont.truetype('arial.ttf', 40)
    
    # text_position = (1200, 465)

    # Calculate the position to place the text
    if len(text) <= 5:
        text_position = (1280, 485)
    elif len(text) <= 9:        
        text_position = (1230, 485)
    elif len(text) <= 12:       
        text_position = (1210, 485)
    elif len(text) <= 12:       
        text_position = (1160, 485)
    elif len(text) <= 10:       
        text_position = (1200, 485)

    else:
        # Default position if text length is not 5 or 15
        text_position = (1110, 485)
    
    # Add text to the certificate image
    draw.text(text_position, text, fill="black", font=font)
    
    # Save the edited image
    certificate_img.save(output_path)

def main():
    st.header("Karachi AI - Attendee Shoutout Creator")
    
    st.text("Generate your banner and share on LinkedIn to build your raport in connections!")

    st.text("")    
    st.text("Sample Output")    
    # Display an image
    st.image("https://gcdnb.pbrd.co/images/lXEhnUMkBals.jpg", use_column_width=True)

    st.text("")    
    st.text("")    

    # User input for uploading image
    uploaded_image = st.file_uploader("Please Upload your Headshot Picture with Solid Background", type=["jpg", "jpeg", "png"])
    
    # User input for text
    text = st.text_input("Please Enter Full Name (2-3 Words Max) ")
    
    if st.button("Click Here to Generate Event Confirmation"):
        if uploaded_image:
            # Save the uploaded image temporarily
            temp_image_path = "temp_image.png"
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_image.getvalue())
            
            # Call function to add image to the certificate
            add_image_to_certificate('KAI-MEETUP-ATTEND-SHARE.jpg', temp_image_path, text, 'generated_certificate.png')
            
            st.divider()

            # Display the edited certificate
            st.image('generated_certificate.png', use_column_width=True)
            
            st.divider()

            
            st.markdown(
            f"""
            Dear {text},

            We are thrilled to confirm your participation in the highly anticipated event : Karachi AI Meetup # 21 : Applied AI in Media / Entertainment Industry and Game Development with AI
            
            Please note 100 Certificates will be available on first come first serve basis for Registered Participants, Make sure to get your name noted!
            
            📅 Event Details:
            - 📍 Location: Work More, 9th Floor, Fortune Towers, Shahra e Faisal, Karachi
            - 🗓️ Date: Sunday, 29 Sept 2024
            - 🕐 Time: 02:00 PM - 6:00 PM (Check-in for Certificates at 1.15 PM)
            
            You're request to generated below banner for you and share on LinkedIn.
            
            Best Regards,
            **Team Karachi AI**
            """)
            
            st.divider()
            
            st.markdown('**Copy Below LinkedIn Post and Share with Professional Network and Facebook Friends**')
            
            st.markdown(
            """
            🚀 Hey everyone! I'm thrilled to share an extraordinary event Karachi AI Meetup # 21 : Applied AI in Media / Entertainment Industry and Game Development with AI

            📅 Event Details:
            - 📍 Location: Work More, 9th Floor, Fortune Towers, Shahra e Faisal, Karachi
            - 🗓️ Date: Sunday, 29 Sept 2024
            - 🕐 Time: 02:00 PM - 6:00 PM
            
            Join me to learn :
            
            1. AI in Media: Dive into how AI is transforming scriptwriting, scene generation, and post-production with tools like VFX, captions, and translations.
            
            2. AI in Gaming: Explore AI’s role in character creation, world-building, and game development, including personalized NPCs and AI-assisted testing.
            
            🎬 Let’s embark on this AI journey together! Don’t miss this chance to explore the next big thing in media and meet fellow creators and innovators!
            
            👉 Follow me to stay updated and get more details about this groundbreaking event. 
            
            Learn more about Karachi AI - https://www.karachidotai.com/community#meetups
            
            #GenerativeAI #FutureOfGaming #AIinGames #GameDevCommunity #NextGenGaming

            """)
            
            st.divider()

            
            # Add download button
            st.download_button(
                label="Download My Shoutout Banner",
                data=open('generated_certificate.png', 'rb').read(),
                file_name='generated_certificate.png',
                mime='image/png'
            )
            
            # Remove the temporary image file
            os.remove(temp_image_path)
        else:
            st.warning("Please upload an image.")

if __name__ == "__main__":
    main()
