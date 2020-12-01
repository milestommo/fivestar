import streamlit as st
import numpy as np
import pandas as pd

from fivestar.clusters import get_cluster_coords
from fivestar.lib import get_listing
# from fivestar.fivestar import FiveStar

# lists for select boxes (to be replaced by imported lists/params)
borough_list = ['Hackney', 'Westminster', 'Wimbledon']
ptype_list = ['Apartment', 'House']
bedrooms_list = ['studio', 1, 2, '3+']
price_list = ['£79 or less', '£80 - £99', '£100 - £119', '£120 - £139', '£140 or above' ]
amenities_example = ['wifi', 'toaster', 'hangers', 'parking', 'sauna', 'swimming pool']


# test dataframes
example_df = pd.DataFrame(
         [3,2,7,5,5,3,4,5,3],
         columns=['guests_to_accom'])

example_df2 = pd.DataFrame([[51.531952,0.003723],[51.508758,-0.26343],
    [51.490784,0.120272],[51.516887,-0.26769]],
        columns=['lat', 'lon'])


# title
st.title('Airbnb: 5 star predictor')
st.write('')
st.write('')

# setting the scene - host in London
city_col_left, city_col_right = st.beta_columns(2)
with city_col_left:
    opt1 = st.selectbox('Host or guest?', ['Host', 'Guest'])

with city_col_right:
    opt2 = st.selectbox('City', ['London', 'New York', 'Paris'])

'You are a',opt1.upper(),'in', opt2, '!'
st.write('')
st.header('Tell us about your property')
st.write('')
st.write('')

# def func_test(opt1, opt2):
#     return f'{opt2}, {opt1}'
# 'testing :', func_test(opt1, opt2)

# map section
map_col_left, map_col_right = st.beta_columns([1,3])
with map_col_left:
    sel1 = st.selectbox('Borough', borough_list)
    sel2 = st.selectbox('Property Type',ptype_list)
    sel3 = st.selectbox('No. Bedrooms', bedrooms_list)
    price = st.number_input('Price per night, £', min_value=20)

    # plug values in below based on returned cluster
    '5,000 listings'
    '£120 avg price/night'

with map_col_right:
    map_one = get_cluster_coords(sel1, price, 'large')
    st.map(map_one)


# review scores are important
st.write('')
st.write('')
st.header('Review scores are important')
st.write('')
st.write('Review scores vary depending on where your listing is and\
    what the attributes of your listing are.' ' Do you want to know\
    how you can improve your own review score?')
st.write('')

# I want to improve link
if st.button('Yes! I want to improve'):
    'Are you currently a host?'
    host_select = st.selectbox('',['No, I am new to hosting', 'I am a host already'])

# Asking for listing ID and storing as 'listing_id'
listing_id = st.text_input('What is your listing ID?',)
st.write('Your listing ID is', listing_id)

fivestar = FiveStar()

listing = fivestar.get_listing(listing_id)

# display information boxes depending on cluster and listing id
st.write('')
st.header('How you compare (vs similar group of properties)')
rev_one, rev_two = st.beta_columns(2)
with rev_one:
    st.write('')
    st.write('')
    st.write('')
    st.markdown("<h2 style='text-align: center; color: blue;'>Your review score: 95.4</h1>",
     unsafe_allow_html=True)
with rev_two:
    st.write('')
    st.write('')
    st.write('')
    st.markdown("<h2 style='text-align: center; color: blue;'>Avg review score: 97.4</h1>",
     unsafe_allow_html=True)


rev_three, rev_four = st.beta_columns(2)
with rev_three:
    st.write('')
    st.write('')
    st.write('')
    st.markdown("<h2 style='text-align: center; color: red;'>Your ranking: 20 percentile</h1>",
     unsafe_allow_html=True)
with rev_four:
    st.write('')
    st.write('')
    st.write('')
    st.markdown("<h2 style='text-align: center; color: black;'>Great location, clean and tidy, friendly communication...</h1>",
     unsafe_allow_html=True)

    # st.text_area('What makes visitors give great reviews', value='''
    #     It was the best of times, it was the worst of times, it was
    #     was the season of Light, it was the season of Da''', height=200, max_chars=None, key=None)


# sliders for model section
st.write('')
st.header('How you can shift your review score')

# avgs for cluster
avg_guests_accom = int(round(example_df['guests_to_accom'].mean(),0))
#
#
#
#
#
#

# sliders for model
slide_col_left, slide_col_mid, slide_col_right = st.beta_columns([1,2,1])
with slide_col_left:
    st.subheader('Averages for your group')
    st.write('')
    st.write('')
    st.write(avg_guests_accom, 'avg guests')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write(avg_guests_accom, 'avg guests')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write(avg_guests_accom, 'avg guests')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write(avg_guests_accom, 'avg guests')



with slide_col_mid:
    st.subheader('Change your offering')

    guests_accom = st.slider('Guests to accommodate', 0, 16, avg_guests_accom)
    st.write(guests_accom, 'guests')
    st.write('')

    can_strict = st.select_slider(
        'Strict cancellation policy (ie xx)',options=['No', 'Yes'])
    st.write('')
    #st.write('Strict cancellation policy:', can_strict)

    inst_book = st.select_slider(
        'Instantly bookable (ie xx)',options=['No', 'Yes'])
    st.write('')
    #st.write('Instantly bookable:', inst_book)

    host_listings_count = st.slider('No of other listings', 0, 16, 1)
    st.write(host_listings_count + 1, 'listings in total')
    st.write('')

    type_entire = st.select_slider(
        'Entire flat (vs private room)',options=['No', 'Yes'])
    st.write('')

    parking = st.select_slider(
        'Free parking on premises',options=['No', 'Yes'])
    st.write('')

    wifi = st.select_slider(
        'Wifi available',options=['No', 'Yes'])
    st.write('')

    breakfast = st.select_slider(
        'Breakfast included',options=['No', 'Yes'])
    st.write('')

    host_resp_rate = st.select_slider(
        'Response to questions',options=['Never', 'When I can', 'As much as possible'])
    st.write('')

    host_identity = st.select_slider(
        'Host identity verified',options=['No', 'Yes'])
    st.write('')

    price_ratio = st.slider('Price adjustor, £', 0, 250, price)
    st.write('£', price_ratio, )
    st.write('')

    cleanliness_delta = st.slider('Cleaning standard', 0, 10, 1)
    st.write('Expected standard of cleanliness:', cleanliness_delta )
    st.write('')

    amenity_options = st.multiselect('Amenities offered',
        amenities_example)
    st.write(len(amenity_options), 'amenities offered')
    st.write('')


with slide_col_right:
    st.subheader('Review score impact')
    st.write('')
    st.write('review score:', '+0.4')

# checkbox functionality

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#          np.random.randn(20, 3),
#          columns=['a', 'b', 'c'])
#     st.line_chart(chart_data)




