# import json


# def list_all_videos(videos):
#     for index, video in enumerate(videos,start=1):
#         print(f"{index}.")

# def add_vedio(videos):
#     name = input("Enter Video Name : ")
#     time = input("Enter video time : ")
#     videos.append({'name':name,'time':time})
#     save_data_helper(videos)

# def update_video(videos):
#     pass

# def delete_vedio(videos):
#     pass

# def load_data(videos):
#     try:
#         with open('youtube.txt','r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return[]
        
# def save_data_helper(videos):
#     with open('youtube.txt' , 'w') as file:
#         json.dump(videos ,file)


# def main():
#     videos = load_data()

#     while True:
#         print("\n Youtube Manager")
#         print("1.List a favourite Video")
#         print("2.Add a youtube Vedio")
#         print("3. Update a Youtube vedio details")
#         print("4. Delete a Youtube vedio")
#         print("5 Exit the app")
#         print(videos)
#         choice = input("Enter you Choice")

#         match choice:
#             case '1':
#                 list_all_videos(videos)

#             case '2':
#                 add_vedio(videos)

#             case '3':
#                 update_video(videos)
            
#             case '4':
#                 delete_vedio(videos)

#             case '5':
#                 break


# if __name__ == "__main__":
#     main()







import json

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} ({video['time']})")

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    # Implement the update functionality here
    pass

def delete_video(videos):
    # Implement the delete functionality here
    pass

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def main():
    videos = load_data()

    while True:
        print("\nYouTube Manager")
        print("1. List favorite Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your Choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            
if __name__ == "__main__":
    main()























