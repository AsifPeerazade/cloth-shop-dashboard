mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
base='light'\n\
primaryColor='#4CAF50'\n\
backgroundColor='#f5f5f5'\n\
secondaryBackgroundColor='#ffffff'\n\
textColor='#262730'\n\
font='sans serif'\n\
" > ~/.streamlit/config.toml
