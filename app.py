import streamlit as st
import time 
import streamlit.components.v1 as components
import requests
api_key = 'kdtA2aRiPrkvjAh03qWbnwikAerNqpXZM8GAE0ypVgo'

st.set_page_config(page_icon=':credit_card:',page_title='BTC Bill Board')

st.title("Bitcoin Bill Board")

if 'count' not in st.session_state:
    st.session_state.count = 0
    count = st.session_state.count
if 'oldbid' not in st.session_state:
    st.session_state.oldbid = 0


billboard = st.empty()
billboard.write("This is where your message will be displayed")

def payment():
    url = 'https://www.blockonomics.co/api/new_address'
    headers = {'Authorization': "Bearer " + api_key}
    r = requests.post(url, headers=headers)
    if r.status_code == 200:
        address = r.json()
        print(address)
        # print ('Payment receiving address ' + address)
    else:
        print(r.status_code, r.text)


def msgfn():
    billboard.write(msg)
    expander = st.expander("Details")
    expander.write('Current Owner : '+username)
    expander.write('Bid : '+str(new_bid))
    st.balloons()
    

def print_msg():
    if 'oldmsg' not in st.session_state:
        st.session_state.oldmsg = msg
    if st.session_state.count == 0 and new_bid >= 0.0001:
        st.session_state.oldbid = new_bid
        print(st.session_state.oldbid)
        print('count' + str(st.session_state.count))
        st.session_state.count+=1
        msgfn()
    elif st.session_state.count > 0 and new_bid > st.session_state.oldbid:
        print('count' + str(st.session_state.count))
        print(st.session_state.oldbid)
        st.session_state.oldbid = new_bid
        msgfn()
    elif new_bid < st.session_state.oldbid and st.session_state.count > 0:
        billboard.write(st.session_state.oldmsg)
        
        st.error('Your bid is lower than the previous one. Please Update !!!', icon="🚨")
    else:
        
        st.error('Bid should be atleast 0.0001')

with st.sidebar:
    with st.form(key='my_form'):
        username = st.text_input('Name')
        msg = st.text_area('Message')
        new_bid = st.number_input(label='Bid')
        # link='[Pay here](https://www.blockonomics.co/pay-url/9a624dfa3e1e49d9)'
        # st.markdown(link,unsafe_allow_html=True)
        if username == '':
            username = 'Anonymous'
        if st.form_submit_button('Claim',on_click=payment):
            print_msg()
            
                
                
              
            


        





# Todo:

#1. Add api checks to see if the transaction went thruigh
#2. or else show progress bar 
#3. 
