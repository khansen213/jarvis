import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

def record_text():
    """
    Allow the python program to use the microphone
    to listen for audio input.

    Parameters:
    None

    Return:
    String to be used in file.
    """
    # Loop in case of errors
    while(1):
        try:
            
            # Use microphone as input source.
            with sr.Microphone(device_index=1) as source2:
                # prepare recognizer to recive input.
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                # Listen for user's input
                audio2 = r.listen(source2)

                # Using Google to recognize audio
                mytext = r.recognize_google(audio2)

                return mytext

        except sr.RequestError as e:
            print(f'Could not request results; {e}')

        except sr.UnknownValueError:
            print('Unknown error occured!')
    

def output_text(text):
    """
    Take the string recored from the microphone audio
    and save it as a string to a file to use later.

    Parameters:
    recorded_text

    Return:
    None.
    """
    with open('audio_output.txt', 'a') as f:
        timeStamp()
        f.write(f'{text}\n')
    return

def timeStamp():
    from datetime import datetime, timedelta

    # Define the file name where you want to append the timestamps
    file_name = "audio_output.txt"

    # Read the last timestamp from the file (if it exists)
    try:
        with open(file_name, "r") as f:
            last_timestamp = f.readline().strip()
            if last_timestamp:
                last_timestamp = datetime.strptime(last_timestamp, "%m-%d-%Y %H:%M:%S.%f")
    except FileNotFoundError:
        last_timestamp = None

    # Get the current date and time
    current_datetime = datetime.now()

    # Calculate the next day and an hour from the last timestamp (if available)
    if last_timestamp:
        next_day = last_timestamp + timedelta(days=1)
        next_hour = last_timestamp + timedelta(hours=1)

        # Check if the current time is either the next day or has increased by an hour
        if current_datetime >= next_day or current_datetime >= next_hour:
            # Append the current timestamp to the file
            with open(file_name, "a") as f:
                f.write(current_datetime.strftime("%m-%d-%Y %H:%M:%S.%f") + "\n")
    else:
        # If the file is empty or doesn't exist, simply write the current timestamp
        with open(file_name, "a") as f:
            f.write(current_datetime.strftime("%m-%d-%Y %H:%M:%S.%f") + "\n")



def main():
    while True:
        text = record_text()
        output_text(text=text)
        print(text)

if __name__ == "__main__":
    main()
