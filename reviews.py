import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Glassdoor Reviews',
                   page_icon='Resources\APRO_Logo-A.png',
                   layout='wide'
                  )

st.image('Resources\APRO_Logo-A.png', width=100, output_format='PNG')
st.title('RTO Glassdoor Reviews ')

df = pd.read_excel(
    io='Data\ALL GS Data.xlsx',
    engine='openpyxl',
    skiprows=0,
    usecols='C:T',
    nrows=4094
)

st.sidebar.header("Filters:")
st.sidebar.markdown('Please fill in **all** filters for results!')
year = st.sidebar.multiselect(
    "Select the year:",
    options = df['year'].unique(),
    default = df['year'].unique()
)

rating = st.sidebar.multiselect(
    "Select the overall rating:",
    options = df["rating"].unique(),
    default = df["rating"].unique()
)

employee_status = st.sidebar.multiselect(
    "Select current or former employees:",
    options = df["employee_status"].unique(),
    default = df["employee_status"].unique()
)

employee_position = st.sidebar.multiselect(
    "Select job position(s):",
    options = df["reviewer_role"].sort_values().unique(),
    default = 'Store Manager'
)

df_selection = df.query(
    "year == @year & rating == @rating & employee_status == @employee_status & reviewer_role == @employee_position"
)

wl_star = ':star:' * round(df_selection['work-life_balance'].mean())
cv_star = ':star:' * round(df_selection['culture_and_values'].mean())
di_star = ':star:' * round(df_selection['diversity_and_inclusion'].mean())
co_star = ':star:' * round(df_selection['career_opportunities'].mean())
cb_star = ':star:' * round(df_selection['compensation_and_benefits'].mean())
sm_star = ':star:' * round(df_selection['senior_management'].mean())

wl_rating = round(float(df_selection['work-life_balance'].mean()), 2)
cv_rating = round(float(df_selection['culture_and_values'].mean()), 2)
di_rating = round(float(df_selection['diversity_and_inclusion'].mean()), 2)
co_rating = round(float(df_selection['career_opportunities'].mean()), 2)
cb_rating = round(float(df_selection['compensation_and_benefits'].mean()), 2)
sm_rating = round(float(df_selection['senior_management'].mean()), 2)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.subheader('Work-Life Balance Rating')
    st.caption(f'{wl_star}')
    st.text(f'{wl_rating}/5')
with col2:
    st.subheader('Culture and Values Rating')
    st.caption(f'{cv_star}')
    st.text(f'{cv_rating}/5')
with col3:
    st.subheader('Diversity and Inclusion Rating')
    st.caption(f'{di_star}')
    st.text(f'{di_rating}/5')
with col4:
    st.subheader('Career Opportunitues Rating')
    st.caption(f'{co_star}')
    st.text(f'{co_rating}/5')
with col5:
    st.subheader('Compensation and Benefits Rating')
    st.caption(f'{cb_star}')
    st.text(f'{cb_rating}/5')
with col6:
    st.subheader('Senior Management Rating')
    st.caption(f'{sm_star}')
    st.text(f'{sm_rating}/5')

rating1, rating2, rating3 = st.columns(3)

total_reviews = int(df_selection['rating'].count())
city_and_state =(df_selection['city']).nunique()
roles = df_selection['reviewer_role'].nunique()

with rating1:
    st.subheader('Total Reviews')
    st.subheader(f'{total_reviews}')
with rating2:
    st.subheader('Total Unique Cities:')
    st.subheader(f'{city_and_state}')
with rating3:
    st.subheader(f'Total Roles')
    st.subheader(f'{roles}')

st.dataframe(df_selection)

rating_df = df.groupby(by='year').mean()
rating_over_years = px.line(
    rating_df,
    x=rating_df.index,
    y='rating',
    title='<b>Overall Rating Through the Years</b>',
    color_discrete_sequence=['#0083B8'] * len(rating_df),
    template='plotly_white'
)
wl_over_years = px.line(
    rating_df,
    x=rating_df.index,
    y='work-life_balance',
    title='<b>Work-Life Balance Rating Through the Years</b>',
    color_discrete_sequence=['#0083B8'] * len(rating_df),
    template='plotly_white'
)
cv_over_years = px.line(
    rating_df,
    x=rating_df.index,
    y='culture_and_values',
    title='<b>Culture and Values Rating Through the Years</b>',
    color_discrete_sequence=['#0083B8'] * len(rating_df),
    template='plotly_white'
)
di_over_years = px.line(
    rating_df,
    x=rating_df.index,
    y='diversity_and_inclusion',
    title='<b>Diversity and Inclusion Rating Through the Years</b>',
    color_discrete_sequence=['#0083B8'] * len(rating_df),
    template='plotly_white'
)
co_over_years = px.line(
    rating_df,
    x=rating_df.index,
    y='career_opportunities',
    title='<b>Career Opportunities Rating Through the Years</b>',
    color_discrete_sequence=['#0083B8'] * len(rating_df),
    template='plotly_white'
)
cb_over_years = px.line(
    rating_df,
    x=rating_df.index,
    y='compensation_and_benefits',
    title='<b>Compensation and Benefits Rating Through the Years</b>',
    color_discrete_sequence=['#0083B8'] * len(rating_df),
    template='plotly_white'
)
sm_over_years = px.line(
    rating_df,
    x=rating_df.index,
    y='senior_management',
    title='<b>Senior Management Rating Through the Years</b>',
    color_discrete_sequence=['#0083B8'] * len(rating_df),
    template='plotly_white'
)

rating_over_years.update(layout_yaxis_range = [0,5])
wl_over_years.update(layout_yaxis_range = [0,5])
cv_over_years.update(layout_yaxis_range = [0,5])
di_over_years.update(layout_yaxis_range = [0,5])
co_over_years.update(layout_yaxis_range = [0,5])
cb_over_years.update(layout_yaxis_range = [0,5])
sm_over_years.update(layout_yaxis_range = [0,5])

st.plotly_chart(rating_over_years, use_container_width=True)

column1, column2 = st.columns(2)

with column1:
    st.plotly_chart(wl_over_years, use_container_width=True)
    st.plotly_chart(cv_over_years, use_container_width=True)
    st.plotly_chart(di_over_years, use_container_width=True)
with column2:
    st.plotly_chart(co_over_years, use_container_width=True)
    st.plotly_chart(cb_over_years, use_container_width=True)
    st.plotly_chart(sm_over_years, use_container_width=True)