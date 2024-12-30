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

    # st.text("")    
    # st.text("Sample Output")    
    # Display an image
    # st.image("https://gcdnb.pbrd.co/images/lXEhnUMkBals.jpg", use_column_width=True)

    # st.text("")    
    # st.text("")    

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

            
            st.markdown(
            f"""
            Dear {text},

            We are thrilled to confirm your participation in the exciting upcoming event: *Karachi AI Meetup # 22: AI in E-Commerce and Digital Marketing*! 🎉

            Please note that *100 Certificates* will be available on a first-come, first-serve basis for registered participants. Make sure to get your name noted!

            *Event Details*:
            - *Date:* Saturday, 11th January 2025  
            - *Time:* 2:00 PM - 6:00 PM Sharp  
            - *Venue:* DHA Innovista Indus, Sunset Boulevard, Phase II Ext, Karachi    

            *Registration Link:* [Register here](https://www.karachidotai.com/community#meetups)

            Stay updated: [Follow us on Facebook](https://www.facebook.com/groups/karachidotai)

            Best Regards,  
            Team Karachi AI
            """
            )

            st.divider()

            st.markdown('Copy the LinkedIn post below and share it with your professional network and Facebook friends!')

            st.markdown(
                """
                🚀 Exciting News! I'm thrilled to share an extraordinary upcoming event: *Karachi AI Meetup # 22: AI in E-Commerce and Digital Marketing*! 🌐✨  

                *📅 Event Details*:  
                - *📍 Venue:* DHA Innovista Indus, Sunset Boulevard, Phase II Ext, Karachi  
                - *🗓️ Date:* Saturday, 11th January 2025  
                - *🕐 Time:* 2:00 PM - 6:00 PM  

                🎯 *Theme:* AI in E-Commerce and Digital Marketing  

                Join us to explore how AI is transforming the e-commerce and marketing landscapes. This meetup will dive deep into:  
                - *AI-Powered Product Sourcing & Dropshipping*  
                - *Generative AI for Product Photography & AR Displays*  
                - *The TikTok Shop Revolution in Video Commerce*  
                - *AI-Optimized Ads, SEO, and Lead Generation*  
                - *AI-Driven Websites and Content Automation*  

                🔍 Discover cutting-edge innovations, learn from experts, and network with professionals from the industry.  

                *👉 Registration Deadline:* 04th January 2025. Don't miss out! [Register now](https://www.karachidotai.com/community#meetups).  

                Let's embark on this journey into the future of AI together! 🚀  
                """
            )

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