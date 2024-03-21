import pandas as pd
import streamlit as st
import librosa
st.set_page_config(layout="wide")

# import matplotlib.pyplot as plt
# Function to process the uploaded CSV file
df2 = pd.read_csv('./output_matrics (4).csv')
st.title('Blipper v1.0')
st.title('Blipper v1.0')
import streamlit as st
import pandas as pd
import librosa
from  IPython.display import display,Audio
import re
import os
import re
import os
from pydub.playback import play
import librosa
import requests
from io import BytesIO
from pydub import AudioSegment
from IPython.display import Audio,display
import numpy as np
def audio_segment_from_url(audio_url):
    response = requests.get(audio_url)

    response.raise_for_status()
    audio_data = BytesIO(response.content)
    #print(f"{audio_url} Audio Downloaded")
    return AudioSegment.from_file(audio_data)
def audio_file(file):
  pattern = re.compile(r'https://s3-ap-southeast-1\.amazonaws\.com/exotelrecordings/futwork1/|\.mp3$')
  cleaned_url = re.sub(pattern, '', file)
  stereo_audio = audio_segment_from_url(file)

  mono_audio = stereo_audio.split_to_mono()
  mono_left = mono_audio[0]
  mono_right = mono_audio[1]

  files_directory = 'output_files'
  os.makedirs(files_directory, exist_ok=True)

  mono_file = f"{cleaned_url}.mp3"

  if not os.path.exists(os.path.join(files_directory, mono_file)):
    stereo_audio.export(os.path.join(files_directory, mono_file))

  #mono_file=(cleaned_url+".mp3")
  mono_left_file= f"{cleaned_url}_left.mp3"

  mono_right_file= f"{cleaned_url}_right.mp3"
  stereo_audio.export(os.path.join(files_directory, mono_file))

  mono_audios = stereo_audio.split_to_mono()
  #mono_left, mono_right = mono_audios[0].export(os.path.join(files_directory, mono_left_file) ), mono_audios[1].export(os.path.join(files_directory, mono_right_file))
  if not os.path.exists(os.path.join(files_directory, mono_left_file)):
    mono_audios[0].export(os.path.join(files_directory, mono_left_file))

  if not os.path.exists(os.path.join(files_directory, mono_right_file)):
      mono_audios[1].export(os.path.join(files_directory, mono_right_file))


def main():
    st.title("CSV File Viewer")

    # File upload section
    st.sidebar.title("Upload CSV")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        
        if st.button("Download and Process Audio Files (For New Calls)"):
            st.write("Files Downloading. Please Wait 5 Minutes.")
            unique_urls = df['url'].unique()
            for url in  unique_urls:
                pattern = re.compile(r'https://s3-ap-southeast-1\.amazonaws\.com/exotelrecordings/futwork1/|\.mp3$')
                cleaned_url = re.sub(pattern, '', url)
                audio_file(url)
                st.write(f"File {cleaned_url}.mp3 Downloaded!")
                print()


# import pandas as pd
# import streamlit as st
# import librosa
# import re
# import re
# import os
# from pydub.playback import play
# import librosa
# import requests
# from io import BytesIO
# from pydub import AudioSegment
# from IPython.display import Audio,display
# import numpy as np
# st.set_page_config(layout="wide")

# import matplotlib.pyplot as plt
# st.title("Blipper v1.0 Test")

# def audio_segment_from_url(audio_url):
#     response = requests.get(audio_url)

#     response.raise_for_status()
#     audio_data = BytesIO(response.content)
#     #print(f"{audio_url} Audio Downloaded")
#     return AudioSegment.from_file(audio_data)
# def audio_file(file):
#   pattern = re.compile(r'https://s3-ap-southeast-1\.amazonaws\.com/exotelrecordings/futwork1/|\.mp3$')
#   cleaned_url = re.sub(pattern, '', file)
#   stereo_audio = audio_segment_from_url(file)

#   mono_audio = stereo_audio.split_to_mono()
#   mono_left = mono_audio[0]
#   mono_right = mono_audio[1]

#   files_directory = 'output_files'
#   os.makedirs(files_directory, exist_ok=True)

#   mono_file = f"{cleaned_url}.mp3"

#   if not os.path.exists(os.path.join(files_directory, mono_file)):
#     stereo_audio.export(os.path.join(files_directory, mono_file))

#   #mono_file=(cleaned_url+".mp3")
#   mono_left_file= f"{cleaned_url}_left.mp3"

#   mono_right_file= f"{cleaned_url}_right.mp3"
#   stereo_audio.export(os.path.join(files_directory, mono_file))

#   mono_audios = stereo_audio.split_to_mono()
#   #mono_left, mono_right = mono_audios[0].export(os.path.join(files_directory, mono_left_file) ), mono_audios[1].export(os.path.join(files_directory, mono_right_file))
#   if not os.path.exists(os.path.join(files_directory, mono_left_file)):
#     mono_audios[0].export(os.path.join(files_directory, mono_left_file))

#   if not os.path.exists(os.path.join(files_directory, mono_right_file)):
#       mono_audios[1].export(os.path.join(files_directory, mono_right_file))

# # Function to process the uploaded CSV file
# # df2 = pd.read_csv('./output_matrics (4).csv')

# # def process_csv(file):
# #     if file is not None:
# #         # Read the CSV file
# #         df = pd.read_csv(file)

# #         # Extract unique URLs
# #         unique_urls = df['url'].unique()
# #         return df, unique_urls
# #     else:
# #         return None, None

# # # Function to navigate to a new page with selected URL
# # def navigate_to_url_page(selected_url, df):
# #     # Filter DataFrame based on selected URL
# #     filtered_df = df[df['url'] == selected_url]
    
# #     # Display filtered DataFrame
# #     st.write(filtered_df)

# #     filtered_df2=df2[df2['Link'] == selected_url]
# #     st.write(filtered_df2)


# #     st.title('Call Analysis')
    
# #     # Print other details
# #     columns_to_display = [
# #     "Total Call Duration",
# #     "Total Effective Talk Duration",
# #     "Total Effective Talk Percent",
# #     "Talk Duration (Mono Right)",
# #     "Talk Duration (Mono Left)",
# #     "Talk Percent (Mono Right)",
# #     "Talk Percent (Mono Left)",
# #     "Overlaps Count (Total)",
# #     "Overlaps Count (Mono Right)",
# #     "Overlaps Count (Mono Left)",
# #     "Overlaps Duration (Total)",
# #     "Overlaps Duration (Mono Right)",
# #     "Overlaps Duration (Mono Left)",
# #     "Overlaps Percent (Total)",
# #     "Overlaps Percent (Mono Right)",
# #     "Overlaps Percent (Mono Left)"
# # ]

# #     for column in columns_to_display:
# #         st.write(column + ":", filtered_df2[column].iloc[0])


# #     unique_urls = df['url'].unique()
# #     for i in unique_urls:


# #     dataframes=empty_response_time_df[empty_response_time_df['url']==i]
# #     mono_left_df = dataframes[dataframes['channel'] == 'Mono_Left']
# #     first_start_timestamp_mono_left = mono_left_df['start'].iloc[0]
# #     call_duration = pd.to_numeric(mono_left_df['call_duration'].iloc[0])
# #     # print(call_duration)
# #     # print(first_start_timestamp_mono_left)

# #     if first_start_timestamp_mono_left>10 and call_duration > 10:

# #         print(f"id_1_1_Fail")
# #         print(f"(Reason - call is over 10 sec and Agent Started Speaking after 10 sec)")
# #         print(f"Agent Started At {first_start_timestamp_mono_left}")

# #         print("Playing First 15 seconds of audio")
# #         print()
# #         play_from=0
# #         play_till=15


# #         pattern = re.compile(r'https://s3-ap-southeast-1\.amazonaws\.com/exotelrecordings/futwork1/|\.mp3$')
# #         cleaned_url = re.sub(pattern, '',i)
# #         audio =(f'./output_files/{cleaned_url}_left.mp3')
# #         print("Agent Clip")
# #         y, sr=librosa.load(audio)
# #         start_sample = int(play_from *sr)
# #         end_sample = int(play_till *sr)


# #         # Extract the desired segment of the audio
# #         clip = y[start_sample:end_sample]
# #         display(Audio(data=clip, rate=sr, autoplay=False))



# #         print("Orignal Clip")

# #         audio =(f'./output_files/{cleaned_url}.mp3')
# #         y, sr=librosa.load(audio)
# #         start_sample = int(play_from *sr)
# #         end_sample = int(play_till *sr)



# #         # Extract the desired segment of the audio
# #         clip = y[start_sample:end_sample]
# #         display(Audio(data=clip, rate=sr, autoplay=False))
# #     else:
# #         print("id_1_1_Pass")
# #         print()

   
#     # Additional visualization options (uncomment to enable)

#     # # Bar chart example
#     # st.bar_chart(df[selected_cols])

#     # # Text data display example
#     # st.write(df[["Overall Emotion (Total)", "Overall Emotion (Mono Right)", "Overall Emotion (Mono Left)"]])

# # Create Streamlit web app
# st.write("Upload Processed CSV")
# csv_file = st.file_uploader("upload Processed csv", type=["csv"])
# # Define variables
# empty_response_time_df = None
# unique_urls = None
# if csv_file is not None:
#     # File uploader for selecting CSV file
    
#     empty_response_time_df = pd.read_csv(csv_file)
    



#     unique_urls = empty_response_time_df['url'].unique()
#     for i in unique_urls:
#       pattern = re.compile(r'https://s3-ap-southeast-1\.amazonaws\.com/exotelrecordings/futwork1/|\.mp3$')
#       cleaned_url = re.sub(pattern, '', i)
#       audio_file(i)

    
    
#       dataframes=empty_response_time_df[empty_response_time_df['url']==i]
#       mono_left_df = dataframes[dataframes['channel'] == 'Mono_Left']
#       first_start_timestamp_mono_left = mono_left_df['start'].iloc[0]
#       call_duration = pd.to_numeric(mono_left_df['call_duration'].iloc[0])
#       # print(call_duration)
#       # print(first_start_timestamp_mono_left)
    
#       if first_start_timestamp_mono_left>10 and call_duration > 10:
    
#         st.write(f"id_1_1_Fail")
#         st.write(f"(Reason - call is over 10 sec and Agent Started Speaking after 10 sec)")
#         st.write(f"Agent Started At {first_start_timestamp_mono_left}")
    
#         st.write("Playing First 15 seconds of audio")
#         st.write("")
#         play_from=0
#         play_till=15
    
    
#         pattern = re.compile(r'https://s3-ap-southeast-1\.amazonaws\.com/exotelrecordings/futwork1/|\.mp3$')
#         cleaned_url = re.sub(pattern, '',i)
#         audio =(f'./output_files/{cleaned_url}_left.mp3')
#         st.write("Agent Clip")
#         y, sr=librosa.load(audio)
#         start_sample = int(play_from *sr)
#         end_sample = int(play_till *sr)
    
    
#         # Extract the desired segment of the audio
#         clip = y[start_sample:end_sample]
#         display(Audio(data=clip, rate=sr, autoplay=False))
    
    
    
#         st.write("Orignal Clip")
    
#         audio =(f'./output_files/{cleaned_url}.mp3')
#         y, sr=librosa.load(audio)
#         start_sample = int(play_from *sr)
#         end_sample = int(play_till *sr)
    
    
    
#         # Extract the desired segment of the audio
#         clip = y[start_sample:end_sample]
#         display(Audio(data=clip, rate=sr, autoplay=False))
#       else:
#         st.write("id_1_1_Pass")
#         st.write("")

if __name__ == "__main__":
    main()
