import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


image = Image.open("dna-logo.jpg")
st.image(image, use_container_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

st.header("Enter DNA sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write("""***""")

st.header('INPUT (DNA Query)')
st.write(sequence)

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader("1. Print dictionary")


def dna_nucleotide_count(seq):
    return dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])


x = dna_nucleotide_count(sequence)
st.write(x)

st.subheader("2. Print text")
st.write("There are "+ str(x["A"]) + " adenine (A)")
st.write("There are "+ str(x["T"]) + " adenine (T)")
st.write("There are "+ str(x["G"]) + " adenine (G)")
st.write("There are "+ str(x["C"]) + " adenine (C)")

st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(x, orient="index")
df = df.rename(mapper={0: "count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index": "nucleotide"})
st.dataframe(df)

st.subheader("4. Display Bar chart")
p = alt.Chart(df).mark_bar().encode(
    x="nucleotide", y="count"
)
p = p.properties(width=alt.Step(80))
st.write(p)
