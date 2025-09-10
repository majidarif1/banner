import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

# Configuration Dictionary for Easy Parametrization
config = {
    'certificate_image': 'KAI-MEETUP-ATTEND-SHARE.jpeg',
    'font_path': 'arial.ttf',
    'font_size': 40,
    'circle_radius': 140,
    'image_resize': (320, 315),
    'image_position': (1115, 310),
    'text_position': (1270, 660),
    'text_max_length': 20,
    'image_shape': 'rounded_square',  # Options: 'circle', 'square', 'rounded_square'
    'rounded_radius': 25      # Corner radius for rounded square
}

confirmation_message = """
Dear {name},

We are thrilled to confirm your participation in the exciting upcoming event: *Karachi AI Meetup #24: Monetizing Applied AI Skills*! 🎉

Please note that *100 Certificates* will be available on a first-come, first-serve basis for registered participants. Make sure to get your name noted!

*Event Details*:
- *Date:* Sunday, 14th Sep 2025  
- *Time:* 1:00 PM - 6:00 PM Sharp  
- *Venue:* CS-AUDI, Block-C, Second Floor, Muhammad Ali Jinnah University, Karachi

*Location Pin:* [Register here](https://www.karachidotai.com/meetup/location)  

*Registration Link:* [Register here](https://www.karachidotai.com/community#meetups)

Stay updated: [Follow us on Facebook](https://www.facebook.com/groups/karachidotai)

Best Regards,  
Team Karachi AI
"""

social_share = """
🚀 Exciting News! I'm thrilled to share an extraordinary upcoming event: *Karachi AI Meetup #24: Monetizing Applied AI Skills*! 🧠🏥⚽

*Event Details*:
- *Date:* Sunday, 14th Sep 2025  
- *Time:* 1:00 PM - 6:00 PM Sharp  
- *Venue:* CS-AUDI, Block-C, Second Floor, Muhammad Ali Jinnah University, Karachi

🎯 *Theme:* Monetizing Applied AI Skills  

Join us to explore how we can Monetize Applied AI Skills. This meetup will dive deep into:  
- *Monetization with Coding abilities as Freelancer in Gen AI*  
- *Monetization with AI-Powered Content Creation (Media)*  
- *Monetization with Building & Selling Micro SaaS Using AI*  
- *Monetization with No-Code abilities with AI Automation*  
- *Monetization with AI Consulting (Strategy, Marketing, HR)*

👩‍⚕️ *Who Should Attend?*  
Anyone can attend the event who want to earn money with the Power of Applied AI Skills!**

🧠 No tech background required. Just curiosity and a passion for innovation!

👉 *Registration Deadline:* Register now to secure your spot: [karachidotai.com/community#meetups](https://www.karachidotai.com/community#meetups)  

💡 I am becoming Future Proof, Are you Joining Me? 
"""

def add_image_to_certificate(certificate_path, uploaded_image, text, output_path, config):
    certificate_img = Image.open(certificate_path)
    uploaded_img = Image.open(uploaded_image).convert("RGBA")
    uploaded_img = uploaded_img.resize(config['image_resize'])

    shape = config.get('image_shape', 'rounded_square')

    if shape == 'circle':
        # Circular mask
        mask = Image.new("L", uploaded_img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, uploaded_img.size[0], uploaded_img.size[1]), fill=255)
        uploaded_img.putalpha(mask)

    elif shape == 'rounded_square':
        # Rounded square mask
        mask = Image.new("L", uploaded_img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, uploaded_img.size[0], uploaded_img.size[1]),
                               radius=config.get('rounded_radius', 25), fill=255)
        uploaded_img.putalpha(mask)

    elif shape == 'square':
        # Square (no mask needed)
        uploaded_img = uploaded_img

    # Paste uploaded image
    certificate_img.paste(uploaded_img, config['image_position'], uploaded_img if shape != 'square' else None)

    draw = ImageDraw.Draw(certificate_img)
    font = ImageFont.truetype(config['font_path'], config['font_size'])

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x_position = config['text_position'][0] - text_width // 2
    y_position = config['text_position'][1] - text_height // 2

    draw.text((x_position, y_position), text, fill="black", font=font)
    certificate_img.save(output_path)

def main():
    st.header("Karachi AI - Attendee Shoutout Creator")
    
    st.text("Generate your banner and share on LinkedIn to build your rapport in connections!")

    st.text("")    
    st.text("Sample Output")    
    # Display an image
    st.image(config['certificate_image'], use_column_width=True)

    st.text("")    
    st.text("")    

    # User input for uploading image
    uploaded_image = st.file_uploader("Please Upload your Headshot Picture with Solid Background", type=["jpg", "jpeg", "png"])
    
    # User input for text
    text = st.text_input("Please Enter Full Name (2-3 Words Max) ")

    text = (text[:config['text_max_length']])
    
    if st.button("Click Here to Generate Event Confirmation"):
        if uploaded_image:
            # Save the uploaded image temporarily
            temp_image_path = "temp_image.png"
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_image.getvalue())
            
            # Call function to add image to the certificate
            add_image_to_certificate(config['certificate_image'], temp_image_path, text, 'generated_certificate.png', config)
            
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
