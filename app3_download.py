import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

confirmation_message="""
Dear {name},

We are thrilled to confirm your participation in the exciting upcoming event: *Karachi AI Meetup #23: Applied AI in Personalized Healthcare & Sport Analytics / Wellbeing*! 🎉

Please note that *100 Certificates* will be available on a first-come, first-serve basis for registered participants. Make sure to get your name noted!

*Event Details*:
- *Date:* Saturday, 17th May 2025  
- *Time:* 1:00 PM - 6:00 PM Sharp  
- *Venue:* Ziauddin University, Clifton, Karachi    

*Registration Link:* [Register here](https://www.karachidotai.com/community#meetups)

Stay updated: [Follow us on Facebook](https://www.facebook.com/groups/karachidotai)

Best Regards,  
Team Karachi AI
"""

social_share ="""
🚀 Exciting News! I'm thrilled to share an extraordinary upcoming event: *Karachi AI Meetup #23: Applied AI in Personalized Healthcare & Sport Analytics / Wellbeing*! 🧠🏥⚽

*📅 Event Details*:  
- *📍 Venue:* Ziauddin University, Clifton, Karachi  
- *🗓️ Date:* Saturday, 17th May 2025  
- *🕐 Time:* 1:00 PM - 6:00 PM  

🎯 *Theme:* AI in Personalized Healthcare & Sport Analytics  

Join us to explore how AI is revolutionizing health, medicine, and athletic performance. This meetup will dive deep into:  
- *AI-Driven Personalized Treatment Planning*  
- *Generative AI in Medical Imaging*  
- *Virtual Health Assistants & Chatbots*  
- *AI-Powered Athlete Performance Analysis*  
- *Injury Prevention & Recovery using AI*  
- *Wearable Tech for Fitness & Wellbeing*

👩‍⚕️ *Who Should Attend?*  
Doctors, nurses, pharmacists, radiologists, physiotherapists, athletes, fitness professionals, sports enthusiasts, and curious minds — **students and professionals welcome!**

🧠 No tech background required. Just curiosity and a passion for innovation!

👉 *Registration Deadline:* Register now to secure your spot: [karachidotai.com/community#meetups](https://www.karachidotai.com/community#meetups)  

Let’s shape the future of healthcare and wellbeing through AI! 💡 
"""

def add_image_to_certificate(certificate_path, uploaded_image, text, output_path):
    # Open the certificate image
    certificate_img = Image.open(certificate_path)
    
    # Open the uploaded image
    uploaded_img = Image.open(uploaded_image)
    
    uploaded_img = uploaded_img.resize((400, 400))  # Change dimensions as needed
    
    # Create a round mask with the same size as the uploaded image
    mask = Image.new("L", uploaded_img.size, 0)  # "L" mode for grayscale (alpha channel mask)
    draw = ImageDraw.Draw(mask)

    # Define the radius (adjust as needed)
    radius = 140  # Smaller radius value to make the circle smaller

    # Calculate the bounding box for the ellipse based on the radius
    left = (uploaded_img.size[0] - radius * 2) / 2
    top = (uploaded_img.size[1] - radius * 2) / 2
    right = left + radius * 2
    bottom = top + radius * 2

    # Draw a white circle (255) on the mask
    draw.ellipse((left, top, right, bottom), fill=255)

    # Apply the round mask to the uploaded image (to make the image circular)
    uploaded_img.putalpha(mask)

    # Calculate the position to place the uploaded image on the certificate
    center_point_image = (1105, 190)  # Change position as needed
    
    # Paste the uploaded image onto the certificate image
    certificate_img.paste(uploaded_img, center_point_image, uploaded_img)
    
    # Create a drawing context
    draw = ImageDraw.Draw(certificate_img)
    
    # Custom font style and font size for text
    font = ImageFont.truetype('arial.ttf', 40)
    
    center_point_text = (1306,548)  # This is the center point where we want the text to be centered

    # Calculate the width and height of the text
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the position of the text so that its center aligns with the center_point
    x_position = center_point_text[0] - text_width // 2
    y_position = center_point_text[1] - text_height // 2

    # Draw the text on the image
    draw.text((x_position, y_position), text, fill="black", font=font)
    
    # Save the edited image
    certificate_img.save(output_path)

def main():
    st.header("Karachi AI - Attendee Shoutout Creator")
    
    st.text("Generate your banner and share on LinkedIn to build your raport in connections!")

    st.text("")    
    st.text("Sample Output")    
    # Display an image
    st.image("KAI-MEETUP-ATTEND-SHARE.jpeg", use_column_width=True)

    st.text("")    
    st.text("")    

    # User input for uploading image
    uploaded_image = st.file_uploader("Please Upload your Headshot Picture with Solid Background", type=["jpg", "jpeg", "png"])
    
    # User input for text
    text = st.text_input("Please Enter Full Name (2-3 Words Max) ")

    text = (text[:15])
    
    if st.button("Click Here to Generate Event Confirmation"):
        if uploaded_image:
            # Save the uploaded image temporarily
            temp_image_path = "temp_image.png"
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_image.getvalue())
            
            # Call function to add image to the certificate
            add_image_to_certificate('KAI-MEETUP-ATTEND-SHARE.jpeg', temp_image_path, text, 'generated_certificate.png')
            
            st.divider()

            # Display the edited certificate
            st.image('generated_certificate.png', use_column_width=True)
            
            st.divider()
            
            st.markdown(confirmation_message.format(name=text))

            st.divider()

            st.markdown('*Copy the LinkedIn post below and share it with your professional network and Facebook friends!*')

            st.markdown(social_share)

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
