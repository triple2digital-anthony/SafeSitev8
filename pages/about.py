import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About")
st.sidebar.header("About")

# About content
st.markdown("""
## Safe Site - Security Analysis Tool

Safe Site is a comprehensive security analysis tool designed to help identify and mitigate potential security vulnerabilities in web applications.

### Features
- 🔍 Real-time security scanning
- 🛡️ Vulnerability assessment
- 📊 Detailed reporting
- 🔄 Continuous monitoring

### Version
- Current Version: 1.0.0
- Last Updated: 2024

### Contact
For support or inquiries:
- 📧 Email: support@safesite.com
- 💬 Discord: SafeSite Community
- 🐦 Twitter: @SafeSite

### Credits
Built with:
- Streamlit
- Python
- OpenCV
- And other open-source technologies

### License
This project is licensed under the MIT License - see the LICENSE file for details.
""")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by the Safe Site Team") 