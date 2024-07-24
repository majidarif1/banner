# # import streamlit as st
# # from PIL import Image, ImageDraw, ImageFont
# # import os

# # def add_image_to_certificate(certificate_path, uploaded_image, text, output_path):
# #     # Open the certificate image
# #     certificate_img = Image.open(certificate_path)
    
# #     # Open the uploaded image
# #     uploaded_img = Image.open(uploaded_image)
    
# #     # Resize the uploaded image
# #     uploaded_img = uploaded_img.resize((400, 400))  # Change dimensions as needed
    
# #     # Calculate the position to place the uploaded image
# #     position = (1130, 38)  # Change position as needed
    
# #     # Paste the uploaded image onto the certificate image
# #     certificate_img.paste(uploaded_img, position)
    
# #     # Create a drawing context
# #     draw = ImageDraw.Draw(certificate_img)
    
# #     # Custom font style and font size for text
# #     font = ImageFont.truetype('arial.ttf', 40)
    
# #     # Calculate the position to place the text
# #     if len(text) <= 5:
# #         text_position = (1250, 450)
# #     elif len(text) <= 10:
# #         text_position = (1200, 450)
# #     elif len(text) >= 15:
# #         text_position = (1120, 450)
# #     else:
# #         # Default position if text length is not 5 or 15
# #         text_position = (1200, 450)
    
# #     # Add text to the certificate image
# #     draw.text(text_position, text, fill="black", font=font)
    
# #     # Save the edited image
# #     certificate_img.save(output_path)

# # def main():
# #     st.title("Certificate Creator")
    
# #     # User input for uploading image
# #     uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    
# #     # User input for text
# #     text = st.text_input("Enter text:")
    
# #     if st.button("Generate Certificate"):
# #         if uploaded_image:
# #             # Save the uploaded image temporarily
# #             temp_image_path = "temp_image.png"
# #             with open(temp_image_path, "wb") as f:
# #                 f.write(uploaded_image.getvalue())
            
# #             # Call function to add image to the certificate
# #             add_image_to_certificate('Certificate.jpg', temp_image_path, text, 'generated_certificate.png')
            
# #             # Display the edited certificate
# #             st.image('generated_certificate.png', caption="Generated Certificate", use_column_width=True)
            
# #             # Add download button
# #             st.download_button(
# #                 label="Download Certificate",
# #                 data=open('generated_certificate.png', 'rb').read(),
# #                 file_name='generated_certificate.png',
# #                 mime='image/png'
# #             )
            
# #             # Remove the temporary image file
# #             os.remove(temp_image_path)
# #         else:
# #             st.warning("Please upload an image.")

# # if __name__ == "__main__":
# #     main()


# import streamlit as st
# from PIL import Image, ImageDraw, ImageFont
# import os

# def add_image_to_certificate(certificate_path, uploaded_image, text, output_path):
#     # Open the certificate image
#     certificate_img = Image.open(certificate_path)
    
#     # Open the uploaded image
#     uploaded_img = Image.open(uploaded_image)
    
#     # Resize the uploaded image
#     uploaded_img = uploaded_img.resize((360, 330))  # Change dimensions as needed
    
#     # Create a round mask
#     mask = Image.new("L", uploaded_img.size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((0, 0, uploaded_img.size[0], uploaded_img.size[1]), fill=255)
    
#     # Apply the round mask to the uploaded image
#     uploaded_img.putalpha(mask)
    
#     # Calculate the position to place the uploaded image
#     position = (1150, 105)  # Change position as needed
    
#     # Paste the uploaded image onto the certificate image
#     certificate_img.paste(uploaded_img, position, uploaded_img)
    
#     # Create a drawing context
#     draw = ImageDraw.Draw(certificate_img)
    
#     # Custom font style and font size for text
#     font = ImageFont.truetype('arial.ttf', 38)
    
#     # text_position = (1200, 465)

#     # Calculate the position to place the text
#     if len(text) <= 5:
#         text_position = (1280, 460)
#     elif len(text) <= 9:
#         text_position = (1230, 460)
#     elif len(text) <= 12:
#         text_position = (1210, 460)
#     elif len(text) <= 12:
#         text_position = (1160, 460)
#     elif len(text) <= 10:
#         text_position = (1200, 460)

#     else:
#         # Default position if text length is not 5 or 15
#         text_position = (1110, 460)
    
#     # Add text to the certificate image
#     draw.text(text_position, text, fill="black", font=font)
    
#     # Save the edited image
#     certificate_img.save(output_path)

# def main():
#     st.title("Banner Creator")
    
#     # User input for uploading image
#     uploaded_image = st.file_uploader("Upload your Picture", type=["jpg", "jpeg", "png"])
    
#     # User input for text
#     text = st.text_input("Enter your name:")
    
#     if st.button("Generate Banner"):
#         if uploaded_image:
#             # Save the uploaded image temporarily
#             temp_image_path = "temp_image.png"
#             with open(temp_image_path, "wb") as f:
#                 f.write(uploaded_image.getvalue())
            
#             # Call function to add image to the certificate
#             add_image_to_certificate('KAI-MEETUP-ATTEND-SHARE.jpg', temp_image_path, text, 'generated_banner.png')
            
#             # Display the edited certificate
#             st.image('generated_banner.png', caption="Banner Generated", use_column_width=True)
            
#             st.download_button(
#                 label="Download Banner",
#                 data=open('generated_banner.png', 'rb').read(),
#                 file_name='generated_banner.png',
#                 mime='image/png'
#             )

#             # Remove the temporary image file
#             os.remove(temp_image_path)
#         else:
#             st.warning("Please upload your Picture.")

# if __name__ == "__main__":
#     main()

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

            We are thrilled to confirm your participation in the highly anticipated event: Karachi AI - Joining Google I/O Extended Karachi 2024 in partnership with GDG Kolachi! 🎉
            
            Please note 100 Certificates will be available on first come first serve basis for Registered Participants, Make sure to get your name noted!
            
            Event Details: Karachi AI Meetup # 20 : Grand Meetup -  THE NEW MULTIMODAL AND AGENTIC AI

            Date: Saturday, 27th July 2024, 10 AM - 2 PM Sharp
            
            Stay Updated : https://www.facebook.com/groups/karachidotai
            
            Best Regards,
            **Team Karachi AI**
            """)
            
            st.divider()
            
            st.markdown('**Copy Below LinkedIn Post and Share with Professional Network and Facebook Friends**')
            
            st.markdown(
            """
            🚀 Hey everyone! I'm thrilled to share an extraordinary event: Karachi AI - Joining Google I/O Extended Karachi 2024 in partnership with GDG Kolachi! 🌐✨
            
            Event Name : Karachi AI Meetup # 20 : Grand Meetup -  THE NEW MULTIMODAL AND AGENTIC AI

            📅 Event Details:
            - 📍 Location: Institute of Business Administration, Main Campus, Karachi
            - 🗓️ Date: Saturday, 27th July 2024
            - 🕐 Time: 10:30 AM - 2:00 PM

            🎯 Theme: THE NEW MULTIMODAL AND AGENTIC AI

            Join us for an incredible journey into the future of artificial intelligence. This Grand Meetup will dive deep into transformative advancements, covering:

            Artificial General Intelligence (AGI)
            Multimodal AI featuring GPT-4o & Google's Project Astra
            Agentic AI Planning Workflows with MS Co-Pilot & Crew AI
            🔍 Discover cutting-edge innovations and gain insights from AI experts about AGI's potential and challenges, the integration of various data types for comprehensive AI, and the future of autonomous goal achievement with Agentic AI.

            Don't miss out on this opportunity to explore the future of AI! 🚀

            👉 Follow me to stay updated and get more details about this groundbreaking event. Let’s embark on this AI journey together! Learn more about Karachi AI - https://www.karachidotai.com/community
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