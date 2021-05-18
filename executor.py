import streamlit as st


def execute(command):
    from subprocess import PIPE, Popen
    process = Popen(
        command, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True
    )
    out, error = process.communicate()
    return out, error


def format_output(out, error):
    st.write("output:")
    st.markdown(f"""
```
{out}
```""")
    st.write("errors:")
    st.markdown(f"""
```
{error}
```""")


with st.form("myform"):
    st.write("Executor sample")
    text = st.text_input("Command", "echo Hello, World!")
    submitted = st.form_submit_button("Execute")

    if submitted:
        out, error = execute(text)
        format_output(out, error)
