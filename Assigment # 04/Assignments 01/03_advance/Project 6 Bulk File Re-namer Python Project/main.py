import os

def main(path):
    i = 0
    # path = 'F:/python-project/project-4/Assignments 01/03_advance/'

    for item in os.listdir(path):
        my_source = os.path.join(path, item)

        #  Check if it is a file or a folder
        if os.path.isfile(my_source):
            my_dest_name = "file_" + str(i)
            my_dest = os.path.join(path, my_dest_name)

        elif os.path.isdir(my_source):
            my_dest_name = "folder_" + str(i)
            my_dest = os.path.join(path, my_dest_name)

        else:
            continue  # If it's neither file nor folder, skip

        #  Check if destination already exists
        if not os.path.exists(my_dest):
            os.rename(my_source, my_dest)
            print(f"Renamed {item} -> {my_dest_name}")
            i += 1
        else:
            print(f"Skipping (already exists): {my_dest_name}")

if __name__ == "__main__":
    input_path = input("Enter the path to the directory:")
    path = input_path
    main(path)
