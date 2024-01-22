import pandas as pd
import streamlit as st
from imdb import IMDb

links_df = pd.read_csv(r"C:\Users\shahi\Downloads\wbsflix-dataset\ml-latest-small\links.csv")
movies_df = pd.read_csv(r"C:\Users\shahi\Downloads\wbsflix-dataset\ml-latest-small\movies.csv")
ratings_df = pd.read_csv(r"C:\Users\shahi\Downloads\wbsflix-dataset\ml-latest-small\ratings.csv")
tags_df = pd.read_csv(r"C:\Users\shahi\Downloads\wbsflix-dataset\ml-latest-small\tags.csv")
top_scores_df = pd.read_csv(r"C:\Users\shahi\Downloads\top_score_df.csv")
top_5_scores_df = pd.read_csv(r"C:\Users\shahi\Downloads\top_5_score_df.csv")
pulp_df = pd.read_csv(https://github.com/AfsheenShahid/streamlit_app_1/blob/main/pulp_df.csv)
shaw_df = pd.read_csv(r"C:\Users\shahi\Downloads\shaw_df.csv")
In_b_df = pd.read_csv(r"C:\Users\shahi\Downloads\In_b_df.csv")

df_62_s= pd.read_csv(r"C:\Users\shahi\Downloads\df_62_s.csv")
df_62_i= pd.read_csv(r"C:\Users\shahi\Downloads\df_62_i.csv")
df_610_s= pd.read_csv(r"C:\Users\shahi\Downloads\df_610_s.csv")
df_610_i= pd.read_csv(r"C:\Users\shahi\Downloads\df_610_i.csv")
df =top_5_scores_df


st.title("Welcome to WBSFLIX!")


st.header("Top Picks from Our Store!")
# Number of posters to display in one row
posters_per_row = 5



# Calculate the number of rows needed
num_rows = len(df) // posters_per_row + (len(df) % posters_per_row > 0)

# Create layout columns
for row in range(num_rows):
    cols = st.columns(posters_per_row)  # Use st.columns for Streamlit versions prior to 1.0

    for col_num in range(posters_per_row):
        index = row * posters_per_row + col_num
        if index < len(df):
            with cols[col_num]:
                # Display poster and title in each column
                st.image(df['poster_url'].iloc[index], caption=df['title'].iloc[index], use_column_width=True)
    
    
genres = top_scores_df['new_tag'].unique()
popular_dict = {genre: top_scores_df[top_scores_df['new_tag'] == genre].copy() for genre in genres}

dataframes_dict = {}
for genre, data in popular_dict.items():
    dataframes_dict[genre] = pd.DataFrame(data).sort_values(by ='pop_score', ascending =False)

Comedy_df=dataframes_dict['Comedy']
Drama_df = dataframes_dict['Drama']
Thriller_df =dataframes_dict['Thriller']
Adventure_df =dataframes_dict['Adventure']
Crime_df=dataframes_dict['Crime']
Action_df=dataframes_dict['Action']
Documentary_df=dataframes_dict['Documentary']
Children_df=dataframes_dict['Children']
Horror_df=dataframes_dict['Horror']
Musical_df=dataframes_dict['Musical']
Fantasy_df=dataframes_dict['Fantasy']
Animation_df=dataframes_dict['Animation']
Sci_fi_df=dataframes_dict['Sci-Fi']
Mystery_df=dataframes_dict['Mystery']
Romance_df=dataframes_dict['Romance']

st.header("What's on your mind!")
chosen_item = st.selectbox("Choose a movie genre",
             key='popularity-based',
             options=top_scores_df['new_tag'].unique(),
             index=None,
             placeholder="Browse our library..."
)

placeholder_image_url = 'https://wallpapercave.com/wp/wp3160287.jpg'

chosen_item_df = globals().get(f"{chosen_item}_df")
                
if chosen_item_df is None:
    st.write("Please choose a movie genre to see the top recommendations!")
    st.image(placeholder_image_url, use_column_width=True)
else:
    st.write(f"Top {chosen_item} movies...")  
    
    posters_per_row = 5

    num_rows = len(df) // posters_per_row + (len(df) % posters_per_row > 0)

    for row in range(num_rows):
        cols = st.columns(posters_per_row)  
    
        for col_num in range(posters_per_row):
            index = row * posters_per_row + col_num
            if index < len(df):
                with cols[col_num]:
                    st.image(chosen_item_df['poster_url'].iloc[index], caption=chosen_item_df['title'].iloc[index], use_column_width=True)

                

st.header("People who liked 'The Shawshank Redemption (1994)' also liked...!")
posters_per_row = 5


num_rows = len(df) // posters_per_row + (len(df) % posters_per_row > 0)

for row in range(num_rows):
    cols = st.columns(posters_per_row)  
    
    for col_num in range(posters_per_row):
        index = row * posters_per_row + col_num
        if index < len(df):
            with cols[col_num]:
                st.image(shaw_df['poster_url'].iloc[index], caption=shaw_df['title'].iloc[index], use_column_width=True)          
                

st.header("People who liked 'In Bruges (2008)' also liked...!")
posters_per_row = 5


num_rows = len(df) // posters_per_row + (len(df) % posters_per_row > 0)

for row in range(num_rows):
    cols = st.columns(posters_per_row)  
    
    for col_num in range(posters_per_row):
        index = row * posters_per_row + col_num
        if index < len(df):
            with cols[col_num]:
                st.image(In_b_df['poster_url'].iloc[index], caption=In_b_df['title'].iloc[index], use_column_width=True)


                
st.header("Are you a WBSFLIXer!")

main_choice = st.radio("Please choose one option!", ["Yes", "No"])

# Conditionally show another option menu if "Yes" is selected
if main_choice == "Yes":
    user_input_id = st.text_input("Please enter your WBSFLIX-ID:")
       
    ui = 0

    if st.button("Submit"):
    
        ui=int(user_input_id)

    if ui == 610:
        selected_df = df_610_i
        st.header("Because you enjoyed watching: Get Out (2017)")

        
        posters_per_row = 5
        num_rows = len(selected_df) // posters_per_row + (len(selected_df) % posters_per_row > 0)

        for row in range(num_rows):
            cols = st.columns(posters_per_row)

            for col_num in range(posters_per_row):
                index = row * posters_per_row + col_num
                if index < len(selected_df):
                    with cols[col_num]:
                        st.image(selected_df['poster_url'].iloc[index], caption=selected_df['title'].iloc[index], use_column_width=True)

        st.header("Specially for you!")     
        selected_df = df_610_s
    
        
        posters_per_row = 5
        num_rows = len(selected_df) // posters_per_row + (len(selected_df) % posters_per_row > 0)

        for row in range(num_rows):
            cols = st.columns(posters_per_row)

            for col_num in range(posters_per_row):
                index = row * posters_per_row + col_num
                if index < len(selected_df):
                    with cols[col_num]:
                        st.image(selected_df['poster_url'].iloc[index], caption=selected_df['title'].iloc[index], use_column_width=True)



    elif ui == 62:
        selected_df = df_62_i
        st.header("Because you enjoyed watching: Sherlock- A study in Pink(2010)")

        
        posters_per_row = 5
        num_rows = len(selected_df) // posters_per_row + (len(selected_df) % posters_per_row > 0)

        for row in range(num_rows):
            cols = st.columns(posters_per_row)

            for col_num in range(posters_per_row):
                index = row * posters_per_row + col_num
                if index < len(selected_df):
                    with cols[col_num]:
                        st.image(selected_df['poster_url'].iloc[index], caption=selected_df['title'].iloc[index], use_column_width=True)

        st.header("Specially for you!")     
        selected_df = df_62_s
    
        
        posters_per_row = 5
        num_rows = len(selected_df) // posters_per_row + (len(selected_df) % posters_per_row > 0)

        for row in range(num_rows):
            cols = st.columns(posters_per_row)

            for col_num in range(posters_per_row):
                index = row * posters_per_row + col_num
                if index < len(selected_df):
                    with cols[col_num]:
                        st.image(selected_df['poster_url'].iloc[index], caption=selected_df['title'].iloc[index], use_column_width=True)
else:
    st.header("Would you like to become a registered customer?")
    st.write("While you are deciding, here are some top featured movies from our store!")
    st.header("Top Picks from Our Store!")

    posters_per_row = 5
    num_rows = len(df) // posters_per_row + (len(df) % posters_per_row > 0)


    for row in range(num_rows):
        cols = st.columns(posters_per_row)  # Use st.columns for Streamlit versions prior to 1.0

        for col_num in range(posters_per_row):
            index = row * posters_per_row + col_num
            if index < len(df):
                with cols[col_num]:
                    st.image(df['poster_url'].iloc[index], caption=df['title'].iloc[index], use_column_width=True)
    
    
    
