import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()


cursor.execute('''
      CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL       
       )
  ''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)", (name,time))
    conn.commit()

def update_video(id,newName,newTime):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(newName,newTime,id))
    conn.commit();

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(id),);
    conn.commit()


def main():
    while True:
        print("\n Youtube manager app with DB");
        print("1. List Videos");
        print("2. Add Videos");
        print("3. Update Videos");
        print("4. Delete Videos");
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1": 
                list_all_videos()
            case "2":
                name = input("Enter the name of the video: ")
                time = input("Enter the time of the video: ")
                add_video(name,time)
            case "3":
                videoId = input("Enter the id of the video to update: ")
                newName = input("Enter the new name of the video: ")
                newTime = input("Enter the new time of the video: ")
                update_video(videoId,newName,newTime)
            case "4":
                id = input("Enter the id of the video: ")
                delete_video(id) 
            case "5":
                break;
    
    conn.close()   

if __name__ == "__main__":
    main()