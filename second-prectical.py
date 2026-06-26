# import module

import streamlit as st

#text
st.text("welcome to my profile !!!")





# success info warning error exception.
#import module
import streamlit as st

#success
st.success("success")

#success
st.info("information")

#success
st.warning("warning")

#success
st.error("error")

#exception - this has been added later
exp = ZeroDivisionError("trying to division by zero")
st.exception(exp)




#5.write

#import module
import  streamlit as st

#write text
st.write("text with write")

#writtingg python inbuilt function range()
st.write(range(10))





#6.display imagea:
#import module
import streamlit as st

# display images

#import image from pillow to open images
from PIL import image 
image = image.open("imade1.jpg")
#display image using streamlit
#width is used to set the wisth of the image

st.image(image, width=200)



#7.checkbox:

#import module
import streamlit as st

#checkbox
#check if the checkbox is checked
#title of the checkbox is'show/hide
if st.checkbox("show/hide"):

    #display the text if the checjbox return true value
    st.text("showing the widget")








