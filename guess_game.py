import streamlit as st

if 'num_to_be_guessed' not in st.session_state:
    st.session_state['num_to_be_guessed'] = 10
if 'count' not in st.session_state:
    st.session_state['count'] = 1
st.header("GUESSING GAME")
st.header("\n\nYOU HAVE 5 CHANCE")
if st.session_state['count']<6:
    guessed_number=st.text_input(label='ENTER YOUR GUESSED NUMBER between 1 to 50:',key='num_input')
    if guessed_number:
            guessed_number = int(guessed_number)
            if guessed_number > 50 or guessed_number<0 :
                st.write("INVALID INPUT") 
            if guessed_number == st.session_state['num_to_be_guessed']:
                st.write("CONGRATULATIONS, YOU WIN!")
                st.session_state['count'] = 1
            else:
                st.write('ATTEMPT:',st.session_state['count'])
                st.write("SORRY,TRY AGAIN BY CLEARING THE GIVEN PREVIOUS INPUT ")
                st.session_state['count'] += 1
        
else:
    st.write("SORRY, YOU FAILED. The number was:", st.session_state['num_to_be_guessed'])
    if st.button("Play Again"):
        st.session_state['count'] = 1
