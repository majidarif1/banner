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
    
    # Resize the uploaded image
    uploaded_img = uploaded_img.resize((360, 335))  # Change dimensions as needed
    
    # Create a round mask
    mask = Image.new("L", uploaded_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, uploaded_img.size[0], uploaded_img.size[1]), fill=255)
    
    # Apply the round mask to the uploaded image
    uploaded_img.putalpha(mask)
    
    # Calculate the position to place the uploaded image
    position = (1120, 135)  # Change position as needed
    
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
    st.image("KAI-MEETUP-ATTEND-SHARE.jpeg", use_column_width=True)

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
            add_image_to_certificate('KAI-MEETUP-ATTEND-SHARE.jpeg', temp_image_path, text, 'generated_certificate.png')
            
            st.divider()

            # Display the edited certificate
            st.image('generated_certificate.png', use_column_width=True)
            
            st.divider()
            
            st.markdown(confirmation_message.format(name=text)

            st.divider()

            st.markdown('Copy the LinkedIn post below and share it with your professional network and Facebook friends!')

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
