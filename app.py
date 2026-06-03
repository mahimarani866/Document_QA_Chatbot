import streamlit as st

st.set_page_config(page_title='Document Q&A Chatbot', page_icon='🤖', layout='wide')

with st.sidebar:
    st.title('📂 Upload Document')
    st.markdown('---')
    uploaded_file = st.file_uploader(label='Upload a PDF file', type=['pdf'])
    st.markdown('---')
    if st.button('🗑️ Clear Chat', use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.caption('Built with LangChain + Gemini')

col1, col2 = st.columns([3, 1])
with col1:
    st.title('🤖 Document Q&A Chatbot')
    st.markdown('Ask questions about your uploaded PDF document.')
with col2:
    if uploaded_file:
        st.success('✅ Document Ready')
    else:
        st.info('📄 No document uploaded')

st.markdown('---')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

user_query = st.chat_input(placeholder='Ask a question...', disabled=not uploaded_file)

if user_query:
    st.session_state.messages.append({'role': 'user', 'content': user_query})
    with st.chat_message('user'):
        st.markdown(user_query)
    with st.chat_message('assistant'):
        with st.spinner('Thinking...'):
            bot_response = f'Pipeline not connected yet. You asked: {user_query}'
        st.markdown(bot_response)
    st.session_state.messages.append({'role': 'assistant', 'content': bot_response})
