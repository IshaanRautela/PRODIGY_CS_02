from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("280x180")
root.title("Image Encryptor/Decryptor")

def process_image(mode):
    # Select file
    file1 = filedialog.askopenfile(mode='rb', filetypes=[('Image Files', '*.jpg;*.png;*.jpeg')])
    if file1 is not None:
        file_name = file1.name
        print("Selected file:", file_name)
        file1.close()

        # Get key
        key = entry1.get()
        if not key.isdigit():
            print("Key must be a number!")
            return
        key = int(key)

        # Read image as bytes
        with open(file_name, 'rb') as f:
            image = bytearray(f.read())

        # XOR encryption/decryption
        for index, value in enumerate(image):
            image[index] = value ^ key

        # Decide output file name
        if mode == "encrypt":
            output_file = file_name.rsplit('.', 1)[0] + "_encrypted." + file_name.rsplit('.', 1)[1]
        else:
            output_file = file_name.rsplit('.', 1)[0] + "_decrypted." + file_name.rsplit('.', 1)[1]

        # Save file
        with open(output_file, 'wb') as f:
            f.write(image)

        print(f"Image {mode}ed and saved as {output_file}")


# Buttons
b1 = Button(root, text="Encrypt Image", command=lambda: process_image("encrypt"))
b1.place(x=50, y=20)

b2 = Button(root, text="Decrypt Image", command=lambda: process_image("decrypt"))
b2.place(x=160, y=20)

# Key entry
Label(root, text="Enter Key:").place(x=30, y=80)
entry1 = Entry(root, width=10)
entry1.place(x=120, y=80)

root.mainloop()
