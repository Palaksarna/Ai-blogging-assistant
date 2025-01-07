import streamlit as st
from langchain_community.llms import Ollama 

# Set up the LLaMA model
llm = Ollama(model="llama3.1:8b")  # Changed to llama3.1:8b

sample_prompt = """
You are a professional blog writer. Write a detailed and engaging blog on the provided topic, keeping the keywords in mind. 
Ensure the content is informative, creative, and suitable for a general audience. 

Details:
Topic: {topic}
Keywords: {keywords}
Word Count: Approximately {num_words}

Please write the blog below:
"""

st.title("AI Blog Generator")
st.subheader("Create a detailed and engaging blog with AI assistance!")

with st.sidebar:
    st.header("Blog Parameters")
    
    # User input fields for blog parameters
    blog_topic = st.text_input("Enter the topic of your blog")
    keywords = st.text_area("Enter keywords (comma-separated)")
    num_words = st.slider("Desired word count", min_value=300, max_value=2000, step=100)

    generate_blog_button = st.button("Generate Blog")

def generate_blog(topic, keywords, num_words):
    # Format the prompt with user input
    prompt = sample_prompt.format(topic=topic, keywords=keywords, num_words=num_words)
    
    try:
        response = llm(prompt)  # Call the LLaMA 3.1 model with the prompt
        if isinstance(response, str):
            formatted_response = f"### Blog Content\n\n{response}\n\n_Disclaimer: Ensure factual accuracy before publishing._"
        else:
            formatted_response = "Error: The model returned an unexpected response."

    except Exception as e:
        formatted_response = f"Error: {str(e)}"
    
    return formatted_response

# Generate blog content if button is clicked
if generate_blog_button and blog_topic and keywords:
    with st.spinner("Generating blog..."):
        blog_content = generate_blog(blog_topic, keywords, num_words)
        st.markdown(blog_content)
