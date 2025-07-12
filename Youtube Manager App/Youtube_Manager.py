def list_all_videos(videos):
    pass


while True:
    print("\n Youtube Manager | Choose an option ")
    print("1. List all youtube videos")
    print("2. Add a youtube video")
    print("3. Update a youtube video details")
    print("4. Delete a youtube video")
    print("5. Exit the app")
    choice = input("Enter your choice")

    match choice :
        case '1':
             list_all_videos(video)