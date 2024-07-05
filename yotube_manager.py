import json

def load_data():
        try:
                with open('youtube.txt', 'r') as file:
                        test =json.load(file)
                        # print(type(test))
                        return test
        except FileNotFoundError:
                return[]

def save_helper(videos):
        with open('youtube.txt', 'w') as file:
                json.dump(videos,file)

def list_all_videos(videos):
        for index,vedio in enumerate(videos,start=1):
                print(f"{index}.{vedio['name']},Duration:{vedio['time']}")

def add_video(videos):
        name = input("Enter the name of your video : ")
        time = input("Enter the time of your video : ")
        videos.append ({'name':name ,'time':time})
        save_helper(videos)

def update_video(videos):
        list_all_videos(videos)
        index =int(input("Enter which vedio you want to update : "))
        if 1 <= index <= len(videos):
                name = input(" Enter your vedio New name : ")
                time = input(" Enter your vedio New time : ")
                videos[index-1] = {'name':name ,'time':time}
                save_helper(videos)
        else:
                print("You have invalid index number")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")





def main():
        videos = load_data()
        while True:
                
                print("\n Youtube Manager | choose an option ")
                print("1. List all youtube videos ")
                print("2. Add a youtube video ")
                print("3. Update a youtube video details ")
                print("4. Delete a youtube video ")
                print("5. Exit the app ")
                choice = input("Enter your choice: ")


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

                        case _:
                                print("invaild syntax")




if __name__ ==  "__main__":
    main()